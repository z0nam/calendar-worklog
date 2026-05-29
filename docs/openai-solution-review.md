# OpenAI 기반 calendar-worklog 검토 (2026-05-22, 갱신 2026-05-29)

> **갱신(2026-05-29):** 아래는 2026-05-22 공식문서 기준 검토다. 이후 실측에서
> ① **Codex 트랙 end-to-end 검증 완료**(큐레이티드 플러그인 커넥터 토글 방식 — 캘린더 읽기/쓰기·Slack·monday 모두 작동),
> ② 무료 GPT 계정에서 Slack 공식 커넥터 읽기가 됐다는 실관찰이 있어, 해당 결론을 아래에 보강했다.

목표는 ChatGPT 채팅창 또는 Codex에서 Slack / monday.com / email / AI session 등
가용한 업무 정보를 종합해, 사용자가 몇 시부터 몇 시까지 어떤 일을 했는지
캘린더에 기록할 수 있게 하는 것이다.

## 결론

- 연구원 다수에게 배포할 1차 경로는 **ChatGPT 채팅창 + 공식 Apps**가 가장 현실적이다.
- 단, 무료 티어만으로 end-to-end 자동 기록을 기대하기는 어렵다.
- 무료 티어 검증 포인트는 "캘린더 읽기/쓰기"보다 먼저 **Slack, Gmail/Calendar, monday 앱이 실제 계정에서 Connect 가능한가**이다.
- monday와 캘린더 쓰기까지 안정적으로 다루려면 **Plus 이상 또는 Business/Enterprise/Edu**가 필요할 가능성이 높다.
- Codex는 라이트 유저용 주 경로는 아니지만(데스크톱 앱 + 모델 접근 비용 필요), **2026-05-29 실측에서 end-to-end 동작이 확인**됐다. 큐레이티드 플러그인 커넥터를 토글하는 방식이라 셋업 난도는 당초 우려보다 낮다. 운영자/개발자 트랙으로 두되 "셋업이 어렵다"는 전제는 폐기한다.

## 공식 문서 기준 확인 사항

### ChatGPT Apps / Connectors

OpenAI는 기존 connectors를 Apps로 통합하고 있으며, ChatGPT 대화 안에서 외부 앱의 정보를
검색·참조하거나 일부 앱에서 작업을 수행할 수 있다.

- Apps는 ChatGPT 대화에서 외부 도구/데이터를 참고하게 해 준다.
- 일부 Apps는 write action을 지원하지만, 외부 작업 전 확인을 요구한다.
- 앱 사용 가능 여부는 플랜, 지역, workspace 설정에 따라 달라진다.
- Free/Go는 Search와 Deep Research가 제한적이며, 일부 앱은 Connect 버튼이 비활성화될 수 있다.

출처: https://help.openai.com/en/articles/11487775-connectors-in-chatgpt

### Slack

Slack app은 ChatGPT에서 Slack 메시지와 스레드를 검색·요약하는 데 쓸 수 있다.
다만 공식 Slack app 문서에는 **paid ChatGPT plan이 필요**하다고 되어 있다.
따라서 현재 목표의 핵심 데이터 소스인 Slack을 무료 티어에 의존하는 것은 위험하다.

출처: https://help.openai.com/en/articles/12525822-chatgpt-connector-for-slack

> **실관찰(갱신):** 무료 GPT 계정에서 Slack 공식 커넥터 **읽기**가 된 사례가 있어 문서의 "paid 필요"와 충돌한다. 무료 가용성은 단정하지 말고 샌드박스 테스트로 확정한다(→ `docs/openai-test-scenarios.md`).

### Google Gmail / Calendar

Google app 연결 시 Gmail, Calendar, Drive 등에서 데이터를 가져올 수 있고,
Google Calendar scope에는 `calendar.events`와 `calendar.events.readonly`가 포함되어 있다.
이는 Calendar event write/read scope가 모두 고려되어 있음을 의미한다.
다만 실제 사용 가능 여부는 앱 액션 설정, 플랜, workspace admin 설정에 영향을 받는다.

출처: https://help.openai.com/en/articles/10408842-google-app-for-chatgpt-data-controls-faq

### Custom MCP / Developer Mode

조직 내부 도구나 custom MCP app으로 read/write 동작을 안정적으로 제공하려면
현재 공식 문서상 Business / Enterprise / Edu의 developer mode 경로가 가장 명확하다.
Pro는 read/fetch MCP 연결은 가능하나, full MCP write support는 Business / Enterprise / Edu 중심이다.

출처: https://help.openai.com/en/articles/12584461-developer-mode-apps-and-full-mcp-connectors-in-chatgpt-beta

### Codex

Codex는 ChatGPT Plus / Pro / Business / Enterprise/Edu에 포함되고,
2026-05-22 기준 공식 문서에는 Free / Go도 기간 한정 포함된다고 되어 있다.
하지만 Codex는 코딩/자동화 agent이므로, 일반 연구원의 채팅창 워크플로보다는
운영자·개발자용 검증, MCP 자동화, 문서 업데이트, 배치 초안 생성에 적합하다.

출처: https://help.openai.com/en/articles/11369540-codex-in-chatgpt

> **검증(2026-05-29):** Codex 데스크톱 앱에서 큐레이티드 플러그인 커넥터(google-calendar / slack / monday-com)로 캘린더 읽기/쓰기 풀사이클·Slack 본인 메시지 검색·monday board activity 추출까지 실데이터 동작을 확인했다. npx 서드파티 MCP는 불필요. 단 monday는 `user context → board activity → updates` 순으로 도구를 명시해야 sprint 도구로 새지 않는다.

## 목표 기준 가능 작업

### ChatGPT 채팅창 경로

가능성이 높은 작업:

- 사용자가 `어제 정리해줘`라고 요청
- ChatGPT가 연결된 Slack / Gmail / Calendar / monday에서 활동 근거 수집
- 기존 캘린더 점유 시간을 읽고 빈 슬롯 추정
- 업무 블록 초안 표 생성
- 사용자가 승인하면 Calendar event 생성 또는 수정

제약:

- 공식 Slack app은 paid ChatGPT plan 필요
- monday app은 앱 디렉터리/조직 설정에 의존하며, 무료 계정에서 확정 불가
- AI session은 ChatGPT의 과거 대화 검색/메모리/Project memory로 일부 보완 가능하지만,
  Claude의 대화 검색처럼 날짜별 업무 로그 소스로 안정적으로 쓸 수 있다고 보기는 어렵다.
- 캘린더 write action은 실제 계정과 workspace 설정에서 확인해야 한다.

### Codex 경로

가능한 작업:

- 이 저장소의 prompt/config를 기준으로 업무일지 생성 로직을 테스트
- MCP 또는 Apps를 붙여 캘린더/Slack/monday 작업을 자동화
- 매일 아침 초안 생성 후 Slack DM/문서/파일로 승인 요청
- 외부 monday URL 산정 앱과 충돌하지 않도록 캘린더 description 보강만 수행

제약:

- 라이트 유저가 직접 쓰기 어렵다.
- 로컬/원격 MCP, 인증, 승인 정책 세팅이 필요하다.
- 사용자별 캘린더 ID, Slack user_id, monday board 설정이 여전히 필요하다.

## 무료 티어에서 확인할 것

무료 계정에서 바로 검증해야 할 체크리스트:

- Settings > Apps에서 Google Calendar / Gmail / Slack / monday가 보이는가
- 각 앱의 Connect 버튼이 활성화되어 있는가
- Slack 검색이 되는가
- Gmail 또는 Calendar 읽기가 되는가
- Calendar event 생성이 되는가
- monday item 검색 또는 읽기가 되는가
- `어제 정리해줘` 요청에서 여러 앱을 한 대화에서 함께 참조할 수 있는가

현재 문서 기준 예상:

- Free: 일부 Apps 또는 제한적 검색은 가능할 수 있으나, Slack은 공식 문서상 paid ChatGPT plan 필요
- Plus: 개인 연구원용 최소 유료 후보. Slack/Gmail/Calendar Apps 기반 검증 가치가 큼
- Business: 조직 배포 후보. 앱/액션을 관리자가 통제할 수 있어 사내 배포에 적합
- Enterprise/Edu: RBAC, compliance, custom MCP governance까지 필요한 경우 후보
- Codex Free: 기간 한정 가능성. 라이트 유저 주 경로는 아니지만 **기능 자체는 검증됨(2026-05-29)**. 모델 접근(구독/API)이 별도 비용이라 무료 ChatGPT 플랜 검증과는 별개 문제

## 권장 검증 순서

1. 무료 ChatGPT 계정 1개로 Apps 연결 가능성만 빠르게 확인한다.
2. Plus 계정으로 Slack + Gmail/Calendar + monday + Calendar write end-to-end를 확인한다.
3. Business workspace 데모 또는 파일럿에서 admin action control, 앱 허용, write confirmation UX를 확인한다.
4. Codex는 사용자 배포 전, 운영자용으로 매일 아침 초안 생성과 문서 업데이트 자동화 가능성을 검증한다.

## 제품 방향

연구원 라이트 유저에게는 "설치형 자동화"보다 다음 UX가 맞다.

```text
사용자: 어제 업무 정리해줘
ChatGPT: Slack/monday/email/calendar를 보고 등록 후보를 표로 제시
사용자: 10~11시는 A 과제 말고 일반 업무로 바꿔서 등록
ChatGPT: 수정된 표를 재확인하고 캘린더에 생성
```

따라서 OpenAI 기반 1차 성공 기준은 다음이다.

- 무료 티어: 배선 가능성 확인
- Plus: 개인 end-to-end 가능성 확인
- Business/Enterprise/Edu: 조직 배포와 custom MCP/write governance 확인
- Codex: 운영자 자동화와 품질 검증

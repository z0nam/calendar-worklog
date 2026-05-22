# ChatGPT 셋업 (Developer Mode + MCP)

ChatGPT에서 calendar-worklog를 돌리는 방법입니다.

> **표준 경로는 Custom GPT가 아니라 "Developer Mode + MCP 커넥터"입니다.**
> Custom GPT는 MCP 커넥터를 직접 호출하는 게 표준 경로가 아닙니다. 도구(캘린더/Slack/monday)를
> 실제로 호출하려면 **본인 ChatGPT 계정에 Developer Mode와 커넥터를 1회 설정**해야 합니다.
> 커넥터는 계정 단위라, 한 번 켜두면 일반 채팅·Project·Custom GPT 어디서나 쓰입니다.

## 사전 조건 (플랜 요건 — 검증 중)

ChatGPT엔 두 가지 다른 메커니즘이 있고, 무료 플랜 가용 여부가 다릅니다:

| 메커니즘 | 무료 플랜 | 비고 |
|---|---|---|
| **공식 커넥터** (Slack, Google Calendar 등 원클릭) | **가능할 수 있음** (실관찰: 무료 계정에서 Slack 읽기 성공) | 미확정 — 쓰기·캘린더는 별도 확인 필요 |
| **Developer Mode + 커스텀 MCP** (monday MCP URL 등록, 풀 read/write) | Plus+ 한정으로 추정 | OpenAI 문서 기준. 무료 가용성 미검증 |

> **결론 미확정.** 공식 문서는 "Developer Mode는 Plus 이상"이라고 하지만, 실제로
> 무료 계정에서 Slack 공식 커넥터로 읽기가 됐다는 실관찰이 있어 충돌함.
> **아래 "무료 플랜 샌드박스 테스트"를 직접 돌려 확정할 것.**

- monday를 쓰는 경우, 회사 어드민이 AI/MCP 커넥터 접근을 허용해 둬야 함
  (monday Admin → Permissions → AI Connectors)

### 무료 플랜 샌드박스 테스트 (확정용 체크리스트)

**권장 격리 방식**: 임시 회사 Google 계정 하나 생성(어드민이면 쉬움) → 그 계정으로
무료 ChatGPT 로그인 + 자체 테스트 캘린더 사용. 계정·데이터가 한 번에 격리되어
production(공개) 캘린더를 오염시키지 않음. Docker 불필요. 단 임시 계정은 Slack/캘린더
히스토리가 없어 *배선 검증*용임. 활동 클러스터링 *내용*까지 임시 계정으로 검증하려면,
**테스트 Slack 채널**에 임시 계정으로 메시지 몇 개를 시각 간격을 두고 남긴 뒤 그 날짜로
`정리`를 돌린다. (worklog는 `from:<본인 user_id>`로 검색하므로 테스트 메시지의 작성자가
임시 계정이어야 잡힘. 쓰기 대상은 테스트 캘린더로.)

무료 GPT 계정 하나로 다음을 순서대로 확인:

- [ ] `Settings → Connectors`에 **Google Calendar / Slack 공식 커넥터가 보이고 연결되는가**
- [ ] Slack **읽기**(메시지 검색)가 되는가  ← 이미 1건 관찰됨
- [ ] Google Calendar **읽기**(일정 조회)가 되는가
- [ ] Google Calendar **쓰기**(이벤트 생성)가 되는가  ← 이게 핵심. 읽기만 되고 쓰기는 막힐 수 있음
- [ ] `Settings → Apps → Advanced settings`에 **Developer mode 토글이 보이는가**
- [ ] monday를 **커스텀 MCP 또는 공식 커넥터로 연결**할 수 있는가
- [ ] 위가 되면 `지참 0835` / `어제 정리`까지 end-to-end 동작하는가

결과에 따라 위 표의 "무료 플랜" 칸을 사실로 확정하고, 메인 README의 트랙별
플랜 요건도 갱신한다.

## 1단계: `user-config.yaml` 준비

Claude 트랙과 **동일한 단일 소스**를 씁니다. 따로 만들지 말고 그대로 재사용:
1. `core/user-config.example.yaml`을 복사해 `user-config.yaml`로 본인 정보 채움
   (이미 Claude 트랙에서 만들었다면 그 파일 그대로)
2. 캘린더 ID 4개 / slack_user_id / monday 보드 ID / work_hours 확인

## 2단계: Developer Mode 켜기

`Settings → Apps → Advanced settings → Developer mode` 토글 ON.
(워크스페이스 계정이면 `Workspace Settings → Permissions & Roles`에서 커스텀 MCP 커넥터 허용 필요)

## 3단계: 데이터 소스 커넥터 연결

`Settings → Connectors`에서:

| 소스 | 연결 방법 | 비고 |
|---|---|---|
| Google Calendar | 공식 커넥터 → Connect (OAuth) | 이벤트 읽기/쓰기. 필수 |
| Slack | 공식 커넥터 → Connect (OAuth) | 메시지 검색. 강력 권장 |
| monday.com | 공식 커넥터가 있으면 Connect / 없으면 **Add custom connector**로 monday 공식 MCP URL 등록 | 회사에서 monday 쓰면 필수 |

**커스텀 MCP 커넥터 추가가 필요한 경우** (`Add custom connector`):
1. MCP 서버 URL 입력 (monday 공식 MCP URL — monday 문서/Admin에서 확인. URL은 임의 입력 금지)
2. 인증 진행 (OAuth 흐름 또는 토큰)
3. 사용할 도구(tools) 선택 — 필요한 것만 스코프 다운 권장

> 쓰기/수정 작업 시 ChatGPT가 실행 전 **확인 모달**을 띄웁니다. 이건 prompt.md의
> "등록 계획 표 확인 게이트"와 별개의 2차 안전장치입니다.

## 4단계: 프롬프트 + 설정 탑재

**권장: ChatGPT Project** (Instructions + 파일 + 커넥터를 함께 묶음)
1. 새 Project 생성 (예: `업무기록 도우미`)
2. Project **Instructions** 칸에 `presets/chatgpt-gpts/instructions.md` 내용 붙여넣기
3. Project 파일에 `core/prompt.md` + 본인 `user-config.yaml` 업로드

또는 **Custom GPT** (공유·패키징용):
- Instructions 칸에 `instructions.md` 붙여넣기, Knowledge에 `prompt.md` + `user-config.yaml` 업로드
- 단, Custom GPT는 MCP 커넥터 직접 호출이 표준이 아니므로 도구 호출은 위 계정 커넥터에 의존

## 5단계: 동작 확인

```
지참 0835
```
→ 근태 캘린더에 08:30~08:35 이벤트 생성 (쓰기 확인 모달 승인)

```
어제 정리
```
→ 어제 활동 종합 → **등록 계획 표** 출력 → 승인하면 빈 슬롯에 업무 블록 생성

## 트러블슈팅

| 증상 | 원인 / 해결 |
|---|---|
| Developer mode 토글이 안 보임 | 무료 플랜이라 막혔을 가능성(미확정) → 위 샌드박스 테스트로 확인 |
| `Add custom connector`가 없음 | Developer mode 미활성 / 워크스페이스 권한 제한 |
| monday 권한 오류 | 회사 어드민이 AI 커넥터 비허용 |
| 도구를 안 부르고 글로만 답함 | 커넥터 연결/인증 재확인, 새 대화로 전환 |
| 색상이 노란색 등으로 들어감 | prompt.md의 colorId 미지정 규칙 무시됨 → "색상 빼고 다시" |

## Claude 트랙과의 차이

- **과거 AI 대화 검색**은 Claude 고유 기능. ChatGPT 트랙엔 없음 → 활동 소스가 Slack/monday/캘린더로 한정
- 나머지(캘린더·Slack·monday)는 동일하게 동작

## 참고

- [Developer mode and MCP apps in ChatGPT — OpenAI Help](https://help.openai.com/en/articles/12584461-developer-mode-and-mcp-apps-in-chatgpt-beta)
- 설정 경로 등 UI는 변동될 수 있으니 위 공식 문서를 우선 확인

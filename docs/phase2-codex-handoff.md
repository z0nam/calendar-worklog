# Phase 2 핸드오프 (코드 작업 — Codex 이관용)

Phase 1(프롬프트 키트 + 4개 트랙 셋업 가이드 + 문서)이 끝났습니다.
여기서부터는 코드 작업이라 Codex CLI로 이관합니다. 이 문서만 읽고도 이어갈 수 있게 정리.

## 지금까지 (Phase 1, 완료)

- `core/prompt.md` — AI/도구 무관 워크플로 본체. 보안 모델 반영:
  - 캘린더 공개 노출 전제 + blacklist 민감도(제목 키워드)
  - 단계 F 개인정보·민감도 검토 게이트(필수), 애매하면 등록하지 말고 확인
  - 등록 계획 표 → 확인 → 생성(G) → 보고(H), 4개 캘린더 통합 점유표 기준 중복 회피
- `core/user-config.example.yaml` — 설정 템플릿 (sensitivity 블록 포함)
- 트랙 4종 셋업 가이드: `presets/{claude-projects,chatgpt-gpts,codex,claude-code}/`
- `docs/feature-matrix.md`, `docs/decision-tree.md`
- 검증: Claude 트랙 실데이터(5/21) 체크리스트 6/6 통과. **Codex 트랙 end-to-end 검증 완료(5/29)** — 캘린더 읽기/쓰기 풀사이클·Slack 본인 메시지 검색·monday board activity 추출까지 실데이터 동작 확인

## 핵심 원칙 (유지할 것)

- **prompt.md는 도구 무관** — 능력 기준 기술, 가용한 것만으로 진행
- **실제 `user-config.yaml`은 로컬 전용·gitignore** — 커밋되는 건 `.example`뿐.
  코드에 캘린더 ID/토큰 하드코딩 금지, 항상 config에서 읽기
- **colorId 미지정, 개인 일정 제외, work_hours 외 자동등록 금지**
- **캘린더는 공개 노출** — 민감 키워드(`sensitivity.title_keywords`) 과업은 세부 미기재
- 저장소 Private 유지(Phase 4에서 public 재검토)

## 남은 작업 (Phase 2)

1. **monday URL 자동 description 보강** (prompt.md 워크플로 4 구체화)
   - 캘린더 이벤트 description의 monday item URL → 현재 상태/담당자/실행 타임라인·실행 업무시간 산정 상태 조회 후 보강
   - 이미 외부 앱이 캘린더의 monday item URL을 기준으로 monday 실행 타임라인과 실행 업무시간을 산정하고 있으므로, 별도 Time Tracking 동기화 스크립트는 만들지 않음
2. **캘린더-monday 중복 전제 반영**
   - 캘린더 업무 블록과 monday item은 겹칠 수 있음
   - description에 monday URL이 있는 캘린더 이벤트는 monday 연동 대상으로 보고, URL이 없는 일반 업무는 monday에 없는 업무일 수 있음을 허용
   - 자동 정리 시 monday에 억지로 신규 item을 만들거나 URL 없는 일반 업무를 monday 시간으로 산정하지 않음
3. **매일 아침 자동 실행**
   - GitHub Actions 또는 local cron으로 "어제 정리" 자동화
   - 단, prompt.md의 확인 게이트와 충돌 → 자동 모드에선 계획을 초안으로 만들고
     사용자 승인 채널(예: Slack DM)로 보내는 식의 설계 필요

## 열린 검증 과제

- **무료 ChatGPT 플랜 가용성 미확정.** 임시 회사 계정 + 테스트 캘린더 + 테스트 Slack 채널로
  샌드박스 테스트 (`presets/chatgpt-gpts/README.md` 체크리스트). 핵심 분기점은
  *무료에서 Google Calendar 쓰기가 되는가*. 결과로 feature-matrix 표 확정.

## Codex로 작업 시작

`presets/codex/README.md` 참고. Codex 데스크톱 앱은 OpenAI **큐레이티드 플러그인
커넥터**(google-calendar / slack / monday-com)를 토글·OAuth 연결하는 방식이라
npx 서드파티 MCP는 불필요(2026-05-29 검증). `AGENTS.md`(+ `core/prompt.md`,
`user-config.yaml`)를 작업 디렉토리에 두고 진행. 쓰기는 도구 승인 프롬프트로 2차 확인됨.

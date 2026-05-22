# Phase 2 핸드오프 (코드 작업 — Codex 이관용)

Phase 1(프롬프트 키트 + 4개 트랙 셋업 가이드 + 문서)이 끝났습니다.
여기서부터는 코드 작업이라 Codex CLI로 이관합니다. 이 문서만 읽고도 이어갈 수 있게 정리.

## 지금까지 (Phase 1, 완료)

- `core/prompt.md` — AI/도구 무관 워크플로 본체. 보안 모델 반영:
  - 캘린더 공개 노출 전제 + blacklist 민감도(제목 키워드)
  - 단계 F 개인정보·민감도 검토 게이트(필수), 애매하면 박지 말고 확인
  - 등록 계획 표 → 확인 → 생성(G) → 보고(H), 4개 캘린더 통합 점유표 기준 중복 회피
- `core/user-config.example.yaml` — 설정 템플릿 (sensitivity 블록 포함)
- 트랙 4종 셋업 가이드: `presets/{claude-projects,chatgpt-gpts,codex,claude-code}/`
- `docs/feature-matrix.md`, `docs/decision-tree.md`
- 검증: Claude 트랙은 실데이터(5/21)로 체크리스트 6/6 통과 확인됨

## 핵심 원칙 (유지할 것)

- **prompt.md는 도구 무관** — 능력 기준 기술, 가용한 것만으로 진행
- **실제 `user-config.yaml`은 로컬 전용·gitignore** — 커밋되는 건 `.example`뿐.
  코드에 캘린더 ID/토큰 하드코딩 금지, 항상 config에서 읽기
- **colorId 미지정, 개인 일정 제외, work_hours 외 자동등록 금지**
- **캘린더는 공개 노출** — 민감 키워드(`sensitivity.title_keywords`) 과업은 세부 미기재
- 저장소 Private 유지(Phase 4에서 public 재검토)

## 남은 작업 (Phase 2)

1. **monday URL 자동 description 보강** (prompt.md 워크플로 3 구체화)
   - 캘린더 이벤트 description의 monday item URL → 현재 상태/담당자/Time Tracking 조회 후 보강
2. **monday Time Tracking 일괄 동기화** (코드 트랙)
   - 캘린더 업무 블록 ↔ monday Time Tracking 컬럼 동기화 스크립트
3. **매일 아침 자동 실행**
   - GitHub Actions 또는 local cron으로 "어제 정리" 자동화
   - 단, prompt.md의 확인 게이트와 충돌 → 자동 모드에선 계획을 초안으로 만들고
     사용자 승인 채널(예: Slack DM)로 보내는 식의 설계 필요

## 열린 검증 과제

- **무료 ChatGPT 플랜 가용성 미확정.** 임시 회사 계정 + 테스트 캘린더 + 테스트 Slack 채널로
  샌드박스 테스트 (`presets/chatgpt-gpts/README.md` 체크리스트). 핵심 분기점은
  *무료에서 Google Calendar 쓰기가 되는가*. 결과로 feature-matrix 표 확정.

## Codex로 작업 시작

`presets/codex/README.md` 참고 — `~/.codex/config.toml`에 MCP 서버 등록,
`AGENTS.md` 배치 후 진행. 쓰기 작업은 `default_tools_approval_mode = "prompt"` 권장.

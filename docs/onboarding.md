# 동료 사용자 인트로

JRI 동료가 calendar-worklog를 본인 워크플로에 도입할 때 읽는 1페이지.

## 한 줄 요약

Slack / monday / AI 세션의 활동 흔적을 종합해 **본인 캘린더에 시간 단위 업무일지를 사후 기록**하는 프롬프트 키트. 채팅 한 줄로 동작.

## 뭐가 되나

- `지참 0835` → 근태 캘린더에 자동 등록 (정규 출근시각 ~ 08:35)
- `어제 정리` → 어제 활동을 Slack/monday/캘린더에서 모아 시간대별 클러스터링 → 빈 슬롯에 1시간 단위 업무 블록 등록, 4개 캘린더로 자동 분류
- `5월 30일 14시 회의 등록해줘` → 명시 일정 단건 등록

모든 쓰기는 **계획표 → 사용자 승인 → 등록** 순서. 채팅에서 본 뒤 OK 해야 박힘.

## 누가 만들었나 / 누구용인가

조남운(JRI PM) 본인 워크플로 자동화로 시작. **현재는 JRI 내부 동료용** — 4 캘린더 분류(과제/근태/업무/기타)와 근태 규칙이 박혀 있음. (Phase 3에서 회사 무관하게 일반화 예정.)

## 진입 요건 — 유료 AI 구독 필수

회사가 제공하는 **monday·Slack은 그대로** 사용. **AI 구독만 개인 부담**.

| 트랙 | 적합 | 무료 가능 |
|---|---|---|
| **Claude Projects** (가장 검증됨) | Claude Pro/Max 사용자 | ❌ Pro+ 필요 |
| ChatGPT Apps/Connectors | ChatGPT Plus+ 사용자 | ❌ Plus+ 필요 (2026-05-29 확정 — 무료엔 Google Calendar 커넥터 자체가 없음) |
| Claude Code | 코드 사용자 | ❌ Pro/Max 또는 API |
| Codex | 코드/운영자 | ❌ 구독/API |

> **Gemini 사용 중이면**: 현재 키트에 Gemini 검증 트랙이 없습니다. Claude Pro / ChatGPT Plus 중 가진 걸로 가세요. Gemini Gems 트랙은 Phase 4에서 검토.

## 5–10분 셋업

1. `docs/decision-tree.md` 읽고 본인 트랙 정하기
2. `presets/<트랙>/README.md` 따라 셋업 (5–10분)
3. `core/user-config.example.yaml` 복사 → `user-config.yaml`로 본인 정보 채움 (이 파일은 gitignored — push 안 됨)
4. AI 채팅창/Project에 `core/prompt.md` + 본인 `user-config.yaml` 업로드
5. `지참 0835` 한 번 돌려서 동작 확인

## 보안 모델 (꼭 읽기)

- **캘린더는 공개 노출 전제** (`calendar.namun.net` 등이 published). 캘린더에 박히는 제목/설명은 외부 노출된다고 보고 작성됨.
- **blacklist 방식**: 기본은 공개 가능. 보안 필요 과업만 제목에 키워드 명시(`[보안]`, `대외비`, `비공개`). 키워드가 있으면 캘린더엔 일반화 제목만 기재(`[과제] 내부 검토` 등)되고 description 비움.
- monday / Drive / Meet **링크는 OAuth로 접근 통제**되므로 description에 남겨도 무방 (열람 권한자만 열림).
- 애매하면 캘린더에 박지 말고 사용자에게 확인 받음(`확인 필요`).
- 자세히는 `core/prompt.md`의 "보안/프라이버시" 섹션.

## 현재 상태 (2026-06-01)

- **Phase 1 동작** — 4 트랙(Claude Projects · ChatGPT Plus · Claude Code · Codex) end-to-end 검증 완료
- **워크플로 5 (주간 과제 보고 — 원장 보고용)** 설계 진행 중 — PM 기준, 실→구성원→과제 트리 구조 확정, 세부 TODO 남음
- **Phase 2 (코드 작업)** 예정 — monday URL description 보강, 매일 아침 자동 실행 (Codex 트랙에서 진행)

## 문의 / 막히면

조남운 (`namun@ji.re.kr`, Slack). IT/security 관련도 같이 봅니다.

# 트랙별 기능 비교표

calendar-worklog를 돌릴 수 있는 트랙(AI 환경)별 비교입니다. 셋업 전 참고하세요.

## 요약

| 트랙 | 셋업 비용 | 플랜 요건 | 무료 가능 | 주 대상 |
|---|---|---|---|---|
| **Claude Projects** | ~5분 | Claude Pro/Max/Team/Ent | ❌ | 비개발 다수 |
| **ChatGPT (Dev Mode + MCP)** | ~10분 | ChatGPT Plus+ | ⚠️ 검증 중 | 비개발 다수 |
| **Claude Code** | ~10분 | Claude Pro/Max 또는 API | ❌ | 코드 사용자 |
| **Codex CLI** | 10분+ | ChatGPT 구독 또는 API | ❌ | 코드 사용자 |

## 능력 비교

| 능력 | Claude Projects | ChatGPT | Claude Code | Codex |
|---|---|---|---|---|
| 캘린더 읽기/쓰기 | ✅ 커넥터 | ✅ 커넥터 | ✅ 커넥터/MCP | ✅ MCP |
| Slack 메시지 검색 | ✅ | ✅ | ✅ | ✅ MCP |
| monday 활동 조회 | ✅ | ✅ (Plus+) | ✅ MCP | ✅ MCP |
| 과거 AI 대화 검색 | ✅ (Claude 고유) | ❌ | ✅ (Claude 고유) | ❌ |
| 셋업 난도 | 낮음 | 중 | 중 | 높음 |
| 자동 실행(cron/CI) | ❌ | ❌ | ✅ | ✅ |

## 메모

- **과거 AI 대화 검색**은 Claude 계열 고유 기능 → 활동 소스가 하나 더 풍부 (Claude 트랙의 우위).
- **무료 가능 여부(ChatGPT)**: 공식 문서는 Plus+를 요구하지만, 무료 계정에서 Slack 공식
  커넥터 읽기가 됐다는 실관찰이 있어 충돌. **확정은 샌드박스 테스트 후**
  (`presets/chatgpt-gpts/README.md` 참고). 핵심 분기점은 *무료에서 Calendar 쓰기 가능 여부*.
- **자동 매일 실행**(Phase 2)은 코드 트랙(Claude Code/Codex)에서만 구성 가능.
- 데이터 소스(monday·Slack)는 회사가 유료 제공 → 모든 트랙에서 공통으로 커버됨.
  유일한 개인 비용은 AI 구독.

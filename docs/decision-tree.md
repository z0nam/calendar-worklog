# 나는 어느 트랙으로? (1페이지 가이드)

상세 비교는 [feature-matrix.md](./feature-matrix.md) 참고. 아래는 빠른 결정용.

## 결정 순서

**1. 터미널/코드가 익숙한가?**
- 아니오 → **2번**으로
- 예 → **3번**으로

**2. (비개발) 이미 구독 중인 AI는?**
- Claude Pro/Max 있음 → **Claude Projects** (가장 쉬움, ~5분)
- ChatGPT Plus 있음 → **ChatGPT (Developer Mode + MCP)**
- 둘 다 없음 → 무료 가능성 검증 중. 임시계정 샌드박스 테스트로 확인하거나, 구독 필요
  (데이터 소스인 monday·Slack은 회사가 이미 제공하므로 추가 비용은 AI 구독뿐)

**3. (개발) 매일 아침 자동 실행이 필요한가?**
- 아니오 → 주력 도구대로: Claude면 **Claude Code**, OpenAI면 **Codex CLI**
- 예 → **Claude Code 또는 Codex** + GitHub Actions/cron (Phase 2 영역)

## 한 줄 요약

- 가장 쉬운 길: **Claude Pro 있으면 Claude Projects**
- 회사 다수 동료: **ChatGPT Plus면 ChatGPT 트랙**
- 코드/자동화 필요: **Claude Code 또는 Codex**
- 무료로 해보고 싶다: **미확정 → 샌드박스 테스트 먼저**

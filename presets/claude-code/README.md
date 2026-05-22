# Claude Code 셋업

Claude Code(터미널/IDE) 사용자가 calendar-worklog를 돌리는 방법입니다. (코드 트랙)

## 사전 조건

- **Claude Code 설치 + Claude 구독(Pro/Max) 또는 API 크레딧**
- 커넥터: claude.ai에서 Google Calendar / Slack 커넥터를 켜두면 Claude Code에서도
  사용 가능 (Claude Code 2.1.46+). monday는 MCP로 추가.

## 1단계: `user-config.yaml` 준비

Claude/ChatGPT 트랙과 **동일한 단일 소스**를 재사용합니다.

## 2단계: 커넥터 / MCP 연결

- **Google Calendar · Slack**: claude.ai → Connectors에서 연결 (Claude Code와 공유됨)
- **monday.com**: `claude mcp add monday ...` 또는 `.mcp.json`에 monday MCP 등록
  (URL/인증은 monday 공식 문서·Admin에서 확인 — 임의 입력 금지)

## 3단계: `CLAUDE.md` 배치

`presets/claude-code/CLAUDE.md`를 작업 디렉토리 루트(또는 전역 `~/.claude/CLAUDE.md`)에
두고, `core/prompt.md` + 본인 `user-config.yaml`을 같은 디렉토리에 둡니다.

## 4단계: 동작 확인

```
지참 0835
어제 정리
```
- 쓰기 작업은 Claude Code 권한 프롬프트로 확인 (계획 게이트 + 권한 = 2중 안전장치)

## 메모

- 이 저장소 자체가 Claude Code 환경에서 개발·검증되었습니다 (커넥터 라이브 검증).
- Claude Projects(웹)와 능력은 같고, 차이는 실행 위치(터미널/IDE)와 자동화 가능 여부.
- Phase 2의 자동 실행(cron/GitHub Actions)은 이 코드 트랙에서 구성합니다.

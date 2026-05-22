# Codex CLI 셋업

Codex CLI 사용자가 calendar-worklog를 돌리는 방법입니다. (코드 트랙)

> handoff엔 "mcp.json"으로 적혀 있었지만, 현재 Codex CLI는 MCP 설정을
> **`config.toml`** (`~/.codex/config.toml` 또는 프로젝트 `.codex/config.toml`)에 둡니다.

## 사전 조건

- **Codex CLI 설치 + OpenAI 인증** (ChatGPT 구독 또는 API 키 — 모델 접근은 별도 비용)
- Google Calendar / Slack / monday **MCP 서버** 준비 (각 공식 문서대로)
- monday를 쓰면 회사 어드민이 AI 커넥터를 허용해 둬야 함

## 1단계: `user-config.yaml` 준비

Claude/ChatGPT 트랙과 **동일한 단일 소스**를 재사용합니다.
`core/user-config.example.yaml`을 복사해 본인 정보로 채우거나, 이미 만든 파일 그대로.

## 2단계: MCP 서버 등록

`presets/codex/config.toml.example`의 `[mcp_servers.*]` 블록을
`~/.codex/config.toml`(또는 프로젝트 `.codex/config.toml`)에 병합합니다.

또는 CLI로 등록:
```
codex mcp add google_calendar -- npx -y <google-calendar-mcp-package>
codex mcp add monday --url "<monday-공식-MCP-URL>"
```

> 패키지명·URL·토큰은 **예시 placeholder**입니다. 각 서버 공식 문서의 실제 값으로 채우세요.
> 쓰기 작업은 `default_tools_approval_mode = "prompt"`로 두는 것을 권장합니다.

## 3단계: AGENTS.md 배치

`presets/codex/AGENTS.md`를 작업 디렉토리 루트(또는 전역 `~/.codex/AGENTS.md`)에 둡니다.
같은 디렉토리에 `core/prompt.md` + 본인 `user-config.yaml`을 두면 Codex가 참조합니다.

## 4단계: 동작 확인

```
지참 0835
어제 정리
```
- `지참` → 근태 캘린더에 빠른 등록
- `어제 정리` → 등록 계획 표 출력 → 승인 시 빈 슬롯에 업무 블록 생성
- 쓰기 작업마다 Codex 도구 승인 프롬프트가 뜸 (계획 게이트 + 승인 = 2중 안전장치)

## 메모

- **무료 가능성**: Codex는 모델 접근(구독/API)이 별도 비용이라, ChatGPT 무료 플랜
  검증과는 별개 문제. 코드 트랙은 MCP 서버를 직접 띄우므로 셋업 난도가 높음
  (일반 동료용보다 코드 사용자 전용).
- Phase 2의 코드 작업(monday Time Tracking 동기화, cron/Actions 자동 실행) 때
  이 트랙을 도그푸딩하기 좋음.

## 참고

- [Model Context Protocol — Codex](https://developers.openai.com/codex/mcp)
- [Configuration Reference — Codex](https://developers.openai.com/codex/config-reference)

# calendar-worklog

협업툴(Slack / monday.com / AI 세션 등)에 흩어진 활동 흔적을 모아
캘린더에 시간 단위 업무일지로 박아주는 프롬프트 키트.

> **현재 상태: Phase 1 (WIP)**
> 제주연구원(JRI) 내부 워크플로에 맞춰 구체화하는 단계입니다.
> 다른 회사/조직에서 그대로 쓰기엔 회사 고유 규칙(4개 캘린더 분류, 근태 규칙 등)이
> 박혀 있어요. Phase 3에서 일반화 예정.

---

## 무엇을 하는가

채팅 한 줄로 다음이 됩니다:

- **"지참 0835"** → 근태 캘린더에 `08:30~08:35 지참 08:35` 자동 등록
- **"어제 일정 정리해줘"** → Slack / AI 세션 / monday 활동을 종합해 어제 빈 캘린더 슬롯에 업무 블록을 1시간 단위로 채움. 캘린더 4종(과제/업무/근태/기타)에 자동 배정
- **"이번 주 정리해줘"** *(예정)* → 주간 단위 사후 기록

작동 원리는 사용자별 설정(`user-config.yaml`)과 공통 프롬프트(`core/prompt.md`)를
AI에 함께 주입하는 방식. AI는 Claude / ChatGPT 어느 쪽이든 OK입니다.

## 듀얼 메인 (Claude / ChatGPT)

monday MCP가 양쪽 다 정식 지원되어 기능 격차는 거의 없습니다.

| 트랙 | 셋업 비용 | 회사 내 사용자 분포 |
|---|---|---|
| Claude Projects | 5분 (Connector 토글) | 소수 |
| ChatGPT (Plus/Pro + Developer Mode MCP) | 10분 (1회 MCP URL 등록) | 다수 |
| Codex / Claude Code / Cursor | 10분 (mcp.json 편집) | 코드 사용자 |
| Gemini Gems | 보조 |  |

각 트랙별 셋업은 `presets/` 디렉토리 참조.

## 구조

```
calendar-worklog/
├── README.md                      # 지금 이 문서
├── core/
│   ├── prompt.md                  # AI에 주입할 본체 (사용자/AI 무관)
│   └── user-config.example.yaml   # 사용자 설정 템플릿
├── presets/
│   ├── claude-projects/           # Claude Projects 셋업 가이드
│   ├── chatgpt-gpts/              # (예정)
│   └── codex/                     # (예정)
└── examples/                      # (예정)
```

## 빠르게 시작 (Claude Projects)

1. `core/user-config.example.yaml`을 복사해서 본인 정보로 채우기
2. claude.ai → Projects → New Project
3. Project knowledge에 `core/prompt.md` + 본인 `user-config.yaml` 업로드
4. Connectors에서 Google Calendar / Slack / monday.com 켜기
5. `"지참 0835"` 또는 `"어제 일정 정리해줘"` 입력

자세한 단계는 [presets/claude-projects/README.md](./presets/claude-projects/README.md).

## 로드맵

| Phase | 상태 | 내용 |
|---|---|---|
| 1 | 진행 중 | JRI 전용으로 본인 워크플로 동작시키기 |
| 2 | 예정 | 사내 동료 3~5명이 매일 쓰는 수준으로 안정화 |
| 3 | 예정 | 회사 고유 규칙을 config로 분리, 코어 추상화 |
| 4 | 예정 | 영문 README 추가 + 퍼블릭 공개 |

## 라이선스

(Phase 4에서 결정)

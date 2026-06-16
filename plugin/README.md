# calendar-worklog-ji (Claude Code 플러그인)

제주연구원(JI) 내부용. 본인 캘린더 4종(과제/근태/업무/기타)에
Slack/monday/AI 활동을 종합해 사후 업무일지를 기록한다.

## 무엇이 되나

- `/worklog late 0835` — 지참 빠른 등록
- `/worklog day` — 어제 일정 자동 정리 (계획 표 → 확인 → 등록)
- `/worklog day 5/30` — 특정 일자 정리
- `/worklog week` — 이번 주 과제 보고 (실 → 구성원 → 과제 트리)
- `/worklog now <제목 날짜 시간>` — 단일 일정 즉시 등록
- `/worklog setup` — 셋업 마법사 (최초 1회)

자유 발화도 OK: `지참 0835`, `어제 정리`, `이번 주 보고` 등.

## 설치 (동료용)

### 1. 사전 준비

- **Claude Code** 설치 + Claude Pro/Max 구독
- **claude.ai 커넥터** 또는 로컬 MCP로 다음 셋 연결:
  - Google Calendar (본인 4개 캘린더 + 전사 공식 일정 캘린더에 권한 있어야 함)
  - Slack
  - monday.com

### 2. 플러그인 설치

```
/plugin marketplace add z0nam/calendar-worklog
/plugin install calendar-worklog-ji
```

### 3. 셋업 마법사 1회 실행

```
/worklog setup
```

마법사가 자동으로 다음을 찾아준다:
- 본인 Slack ID (이메일로 조회)
- 본인 캘린더 4종 (이름 매칭)
- 전사 공식 일정 캘린더 (있으면 자동 등록)
- monday 즐겨찾기 보드 (진행업무/진행과제/전체 과제리스트/연구자 소속 마스터)

수동으로 답해야 하는 건 출퇴근 시각 정도. 결과는
`~/.config/calendar-worklog/user-config.yaml`에 저장된다.

### 4. 시작

```
/worklog late 0835
/worklog day
```

## 어디에 저장되나

- 본인 설정: `~/.config/calendar-worklog/user-config.yaml` (비밀, git에 올리지 말 것)
- 플러그인 본체: `~/.claude/plugins/cache/...` (자동 관리)

## 안전장치

- 이벤트 만들기 전 표로 계획 제시 → 사용자 확인 필요
- 민감 키워드는 일반화 제목으로 자동 치환
- 캘린더는 공개 노출 전제 — DM 본문/AI 세션 본문 그대로 옮기지 않음
- work_hours 밖 활동 자동 등록 금지

## 문제가 있으면

저장소: <https://github.com/z0nam/calendar-worklog>

---
marp: true
theme: default
paginate: true
---

# calendar-worklog
## 활동 흔적으로 캘린더에 사후 업무일지 자동 기록

조남운 (JRI PM, IT·security)
부서 세미나 — 2026년 6월

---

## 어떤 문제를 푸는가

업무 시간이 끝나면 흔한 상태:

- Slack에 답변·요청 수십 개
- monday에 처리한 아이템 몇 개
- AI 채팅에 자료 작성·검토 흔적
- **그런데 캘린더는 텅 빔**

→ 사후 보고 / 회고 / Time Tracking이 어렵다

**해법**: 협업툴 활동을 자동 종합해 **캘린더에 시간 단위 업무 블록으로 사후 기록**

---

## 데모 — 채팅 한 줄

```
지참 0835
```
→ 근태 캘린더에 `08:30~08:35 지참 08:35` 자동 등록

```
어제 정리
```
→ 어제 Slack / monday / 캘린더 활동 종합
→ **계획표 보여줌** → 사용자 승인 → 4 캘린더에 1시간 단위 업무 블록 자동 등록

```
5월 30일 14시 집필진회의 등록해줘
```
→ 명시 일정 단건 등록

> 모든 쓰기는 **계획표 → 승인 → 등록** 순서. 마음대로 안 박힘.

---

## 사용하려면 — 5가지 준비

### 1. 유료 AI 구독 (개인 부담, 한 종 선택)

| 트랙 | 적합한 분 | 검증 |
|---|---|---|
| **Claude Projects** (Claude Pro/Max) | 비개발 다수 | ✅ JRI 실데이터 |
| **ChatGPT Plus+** | 비개발 다수 | ✅ |
| Claude Code / Codex | 코드 도구 사용자 | ✅ |

- ❌ **무료 ChatGPT는 안 됨** — Google Calendar 커넥터가 없음 (2026-05-29 동일기계 A/B로 확정)
- ❌ **Gemini 트랙은 아직 미검증** — 가진 다른 유료 트랙으로 진행

> 회사 제공 monday·Slack은 그대로 사용 — **개인 추가비용은 AI 구독뿐**

---

### 2. GitHub 계정

저장소 Private → 접근하려면 GitHub username 필요
→ 조남운에게 username 알려주시면 collaborator 추가

### 3. 본인 정보 (config로 박는 값)

- 본인 Google Calendar의 4 캘린더 ID (과제 / 근태 / 업무 / 기타)
- 본인 Slack `user_id` (Slack 프로필 → Copy member ID)
- 본인 monday 즐겨찾기 보드 ID들
- 출퇴근 시간 (요일별 다르면 weekly로 분리)

→ `core/user-config.yaml`에 입력. **이 파일은 gitignored** (저장소에 안 올라감, 로컬 전용)

### 4. monday AI 커넥터 허용 (어드민 처리)

회사 어드민이 AI 커넥터 접근을 허용해 둬야 monday 활동 조회 가능 — 본인이 어드민이라 일괄 처리

### 5. 5–10분 시간

decision-tree → preset → config → 첫 명령. 한 번 셋업하면 끝.

---

## 보안 모델 — 꼭 알아야 할 것

- **캘린더는 공개 노출 전제** (`calendar.namun.net` 등이 published)
  → 캘린더에 박히는 제목·설명은 외부 노출된다고 보고 작성
- **Blacklist 방식**: 기본은 공개 가능
  → 보안 필요 과업만 제목에 키워드(`[보안]`, `대외비`, `비공개`) 명시
  → 키워드 있으면 캘린더엔 **일반화 제목만** 기재(`[과제] 내부 검토` 등), description 비움
- monday / Drive / Meet **링크는 OAuth로 접근 통제** → description에 남겨도 무방 (열람 권한자만)
- 애매하면 캘린더에 박지 말고 **사용자에게 확인 요청**(`확인 필요` 마킹)

---

## 현재 상태 (2026-06-01)

- **Phase 1 동작** — 4 트랙 end-to-end 검증 완료, JRI 실데이터로 동작 확인
- **워크플로 5 — 주간 과제 보고 (원장 보고용)**: 설계 진행 중
  - PM 기준 수집, 실 → 구성원 → 과제 트리 구조 확정
  - 세부 보고서 형식 / 폴백 / 차주 계획 마킹 규칙 등 다듬는 중
- **Phase 2 (코드 작업)** 예정 — monday URL 자동 보강, 매일 아침 자동 실행 (Codex 트랙에서 진행)
- **Phase 3 (회사 일반화)** / **Phase 4 (외부 공개)**: 장기 과제

---

## 시작하려면

1. **GitHub username 조남운에게 전달** (Slack DM) → collaborator 추가
2. 저장소 접근 후 **`docs/decision-tree.md`** 읽고 본인 트랙 정함
3. **`presets/<트랙>/README.md`** 따라 셋업 (5–10분)
4. **`core/user-config.example.yaml`** 복사 → `user-config.yaml`에 본인 정보
5. **`지참 0835`** 돌려서 동작 확인
6. 막히면 **`namun@ji.re.kr` / Slack DM**

---

## Q&A 예상

**Q. 무료로는 안 되나?**
A. ChatGPT 무료엔 Google Calendar 커넥터 자체가 없어 안 됩니다 (5/29 동일기계 A/B 확정). Claude Pro / ChatGPT Plus 중 하나 필요.

**Q. Gemini로는?**
A. 현재 검증된 트랙 없음. Phase 4 공개 단계에서 검토 예정. 지금은 Claude/ChatGPT 유료로.

**Q. 내 데이터는 안전한가?**
A. 캘린더는 이미 공개 노출 운영(`calendar.namun.net` 등). 보안 과업은 제목 키워드로 표시되면 자동으로 일반화 제목만 캘린더에 박힘. 링크는 OAuth로 접근 통제. 자세히는 보안 모델 슬라이드 / `core/prompt.md` 보안 섹션.

**Q. 회사 monday/Slack 사용에 추가 비용이?**
A. 없음. 회사 유료 구독 그대로. 개인 부담은 AI 구독뿐.

**Q. AI가 잘못 박으면?**
A. 모든 등록은 **사용자 승인 후**에만 실행. 계획표를 먼저 보여주고, 마음에 안 들면 안 누르면 그만. 등록된 뒤에도 캘린더에서 직접 수정/삭제 가능.

**Q. 누구한테 가장 유용한가?**
A. 본인 활동을 사후에 정리해야 하는 PM / 연구원, Time Tracking이 필요한 사람, 회고·보고 자료를 정기적으로 만드는 사람.

---

## 한 줄 요약

채팅 한 줄로 어제 업무가 시간 단위 캘린더로 정리됨.
**진입조건: 유료 AI 구독 1종 + GitHub 계정 + 5–10분 셋업.**
JRI 동료용으로 만들었고, 어드민(조남운)이 monday 커넥터 허용·계정 권한 추가까지 처리.

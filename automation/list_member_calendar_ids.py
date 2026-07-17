#!/usr/bin/env python3
"""1회용(로컬, 멤버 변경 시 재실행) — MEMBER_CALENDAR_IDS 값 산출.

구성원 [과제]/[업무]/[근태]/[기타] 캘린더의 ID 88개를 열거하고,
허브 계정 calendar@ji.re.kr 이 각 캘린더를 읽을 수 있는지(=루틴 토큰이 읽을 수 있는지) 검증한다.
※ 이 스크립트만 DWD 위임키를 쓴다(로컬 admin 작업). 루틴/클라우드에는 올라가지 않는다.

필요:
  GOOGLE_APPLICATION_CREDENTIALS  — 위임키(calendar+calendar.events 인가)
  ROSTER  — 구성원 이메일 명부 JSON 경로(기본 scratch/roster.json). PII라 커밋 금지.

출력:
  stdout 요약 + ids_env.json(=/schedule env 의 MEMBER_CALENDAR_IDS 에 그대로 붙일 JSON 배열).
"""
import json
import os
import sys

from google.oauth2 import service_account
from googleapiclient.discovery import build

SCOPES = ["https://www.googleapis.com/auth/calendar"]  # DWD는 readonly 미인가 → full로 열거
TAGS = ("[과제]", "[업무]", "[근태]", "[기타]")
HUB = "calendar@ji.re.kr"


def svc_as(key, sub):
    creds = service_account.Credentials.from_service_account_file(key, scopes=SCOPES, subject=sub)
    return build("calendar", "v3", credentials=creds, cache_discovery=False)


def main():
    key = os.environ.get("GOOGLE_APPLICATION_CREDENTIALS")
    if not key:
        sys.exit("env GOOGLE_APPLICATION_CREDENTIALS=<위임키 경로> 필요")
    roster_path = os.environ.get("ROSTER", "scratch/roster.json")
    roster = json.load(open(os.path.expanduser(roster_path), encoding="utf-8"))

    members = []
    for div, info in roster["divisions"].items():
        for m in info["members"]:
            members.append((m["name"], m["email"], div))

    hub = svc_as(key, HUB)
    ok_ids, rows, denied = [], [], []
    for name, email, div in members:
        try:
            cals = svc_as(key, email).calendarList().list(maxResults=250).execute().get("items", [])
        except Exception as e:  # noqa: BLE001
            print(f"  ! impersonate {email} 실패: {str(e)[:80]}", file=sys.stderr)
            continue
        for c in cals:
            if not c.get("summary", "").startswith(TAGS):
                continue
            cid = c["id"]
            try:
                hub.events().list(calendarId=cid, maxResults=1).execute()
                ok_ids.append(cid)
                rows.append({"member": name, "division": div, "summary": c["summary"], "id": cid})
            except Exception as e:  # noqa: BLE001
                denied.append((c["summary"], str(e)[:60]))

    json.dump(ok_ids, open("ids_env.json", "w"), ensure_ascii=False)
    print(f"members={len(members)}  hub_readable={len(ok_ids)}  denied={len(denied)}")
    for s, e in denied:
        print(f"  DENIED {s}: {e}")
    print("→ ids_env.json (MEMBER_CALENDAR_IDS 값)")


if __name__ == "__main__":
    main()

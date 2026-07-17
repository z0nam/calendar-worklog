#!/usr/bin/env python3
"""1회용 — calendar@ji.re.kr 의 calendar.readonly refresh token 발급.

선행: GCP(ji-user-calendar-provisioning)에서 OAuth 2.0 Client ID(애플리케이션 유형=데스크톱)
      생성 + 동의화면을 **Internal**로. client_secret JSON 다운로드.

설치(1회):  pip install google-auth-oauthlib

실행:
  CLIENT_SECRET_FILE=~/Downloads/client_secret_xxx.json python get_refresh_token.py
  → 브라우저가 열리면 **반드시 calendar@ji.re.kr 로 로그인**하고 읽기 권한 허용.
  → 콘솔에 CAL_CLIENT_ID / CAL_CLIENT_SECRET / CAL_REFRESH_TOKEN 출력.

이 셋을 /schedule 루틴 env 에 넣으면 read_calendars.py 가 헤드리스로 캘린더를 읽는다.
토큰은 동의화면 Internal + 게시 상태에서 장수명(미사용 6개월/명시적 revoke 시 만료).
"""
import json
import os
import sys

try:
    from google_auth_oauthlib.flow import InstalledAppFlow
except ImportError:
    sys.exit("google-auth-oauthlib 미설치. 실행: pip install google-auth-oauthlib")

SCOPES = ["https://www.googleapis.com/auth/calendar.readonly"]


def main():
    secret_file = os.environ.get("CLIENT_SECRET_FILE")
    if not secret_file:
        sys.exit("env CLIENT_SECRET_FILE=<다운로드한 client_secret.json 경로> 필요")
    secret_file = os.path.expanduser(secret_file)

    flow = InstalledAppFlow.from_client_secrets_file(secret_file, SCOPES)
    # 로컬 서버로 콜백 수신. 브라우저에서 calendar@ji.re.kr 선택/로그인.
    creds = flow.run_local_server(port=0, prompt="consent")

    if not creds.refresh_token:
        sys.exit("refresh_token 미수신. 동의화면에서 prompt=consent로 다시 시도.")

    with open(secret_file, encoding="utf-8") as f:
        info = json.load(f)
    block = info.get("installed") or info.get("web") or {}
    print("\n=== /schedule env 에 넣을 값 ===")
    print(f"CAL_CLIENT_ID={block.get('client_id')}")
    print(f"CAL_CLIENT_SECRET={block.get('client_secret')}")
    print(f"CAL_REFRESH_TOKEN={creds.refresh_token}")


if __name__ == "__main__":
    main()

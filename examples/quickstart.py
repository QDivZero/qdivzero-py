"""Quick start: list the user's accounts with an API key."""

import os
import sys

from qdivzero_py import QDivZero
from qdivzero_py.api.accounts.get_accounts import sync_detailed


def main() -> None:
    api_key = os.environ.get("QDIV0_API_KEY", "")
    if not api_key:
        print("set QDIV0_API_KEY", file=sys.stderr)
        sys.exit(2)

    qd = QDivZero(api_key=api_key)
    response = sync_detailed(client=qd.client)
    if response.status_code != 200:
        print(f"get accounts: status {response.status_code}", file=sys.stderr)
        sys.exit(1)
    parsed = response.parsed
    memberships = getattr(parsed, "memberships", None) or []
    for m in memberships:
        print(f"account={m.account_id} role={m.role}")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""
Simple wrapper that demonstrates how to authenticate to Proton VPN
and fetch the list of available servers. Real implementation
will add auto‑connect, rotation, and encrypted stats storage.
"""

import os
import sys
import json
import requests
from pathlib import Path
from cryptography.fernet import Fernet

API_BASE = "https://api.protonvpn.com/vpn"

def get_token():
    """Read a token from an environment variable (for demo)."""
    token = os.getenv("PROTON_VPN_TOKEN")
    if not token:
        print("Set PROTON_VPN_TOKEN env var with your Proton VPN API token.", file=sys.stderr)
        sys.exit(1)
    return token

def list_servers(token):
    resp = requests.get(f"{API_BASE}/servers", headers={"Authorization": f"Bearer {token}"})
    resp.raise_for_status()
    return resp.json()

def main():
    token = get_token()
    servers = list_servers(token)
    print(json.dumps(servers, indent=2))

if __name__ == "__main__":
    main()

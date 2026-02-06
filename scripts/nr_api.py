import os
import sys
import json
import requests
import argparse

# --- Configuration ---
NR_USER = os.getenv("NR_USER")
NR_PASS = os.getenv("NR_PASS")
NR_URL = os.getenv("NR_URL", "http://127.0.0.1:1880")

class NodeRedAPI:
    def __init__(self):
        self.base_url = NR_URL
        self.token = None

    def login(self):
        url = f"{self.base_url}/auth/login"
        payload = {
            "client_id": "node-red-admin",
            "grant_type": "password",
            "scope": "*",
            "username": NR_USER,
            "password": NR_PASS
        }
        try:
            resp = requests.post(url, json=payload)
            if resp.status_code == 200:
                self.token = resp.json().get("access_token")
                return True
            return False
        except Exception as e:
            print(f"Login error: {e}")
            return False

    def get_headers(self):
        if not self.token:
            self.login()
        return {
            "Authorization": f"Bearer {self.token}",
            "Content-Type": "application/json"
        }

    def list_flows(self):
        url = f"{self.base_url}/flows"
        resp = requests.get(url, headers=self.get_headers())
        return resp.json()

    def deploy(self, flow_data):
        url = f"{self.base_url}/flows"
        # Node-RED expects an object with 'flows' array for a full deploy
        # Or a list of nodes for a partial one. Standardizing on full for now.
        resp = requests.post(url, headers=self.get_headers(), json=flow_data)
        return resp.json()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Node-RED Manager CLI")
    subparsers = parser.add_subparsers(dest="command")

    # List Flows
    subparsers.add_parser("list-flows")

    # Deploy
    deploy_parser = subparsers.add_parser("deploy")
    deploy_parser.add_argument("--file", required=True)

    args = parser.parse_args()
    api = NodeRedAPI()

    if args.command == "list-flows":
        print(json.dumps(api.list_flows(), indent=2))
    elif args.command == "deploy":
        with open(args.file, 'r') as f:
            data = json.load(f)
        print(json.dumps(api.deploy(data), indent=2))
    else:
        parser.print_help()

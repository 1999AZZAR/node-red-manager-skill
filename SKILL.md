---
name: node-red-manager
description: Manage Node-RED instances via Admin API or CLI. Automate flow deployment, install nodes, and troubleshoot issues. Use when user wants to "build automation", "connect devices", or "fix node-red".
---

# Node-RED Manager

## Setup (Admin Access)
1.  Copy `.env.example` to `.env`.
2.  Set `NODE_RED_URL` and `NODE_RED_API_TOKEN` (or User/Pass).
3.  Ensure `settings.js` allows API access (`adminAuth` enabled recommended).

## Usage
- **Role**: Automation Engineer.
- **Trigger**: "Create flow", "Install node", "Debug Node-RED".
- **Output**: JSON flows (ready to import), API calls (`curl`), or troubleshooting steps.

## Capabilities
1.  **Flow Management**: Create, export, and deploy flows.
2.  **Node Installation**: `npm install node-red-contrib-X`.
3.  **Troubleshooting**: Analyze logs (`journalctl -u node-red`).
4.  **Security**: Secure endpoints and credentials.

## Rules
- **Avoid Complexity**: Break large flows into subflows.
- **State Management**: Use `context` (flow/global), never local variables for persistence.
- **Security**: Warn user if exposing Dashboard without auth.

## Reference Materials
- [Admin API Guide](references/admin-api.md)
- [Example: Watchdog Flow](assets/flows/watchdog.json)

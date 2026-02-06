---
name: node-red-manager
description: Manage Node-RED flows and automation scripts via Admin API.
---

# Node-RED Manager Skill

Orchestrate your visual automation engine directly from Mema's brain.

## Core Capabilities

### 1. Flow Orchestration
Programmatically interact with Node-RED's Admin API.
- **List Flows:** Fetch all deployed flows and nodes.
- **Deploy Changes:** Upload new flow configurations.
- **Node Management:** List installed nodes and palette status.

### 2. Authentication Management
Handles Bearer token generation for secure API access.
- Automatically logs in using configured credentials.
- Refreshes tokens as needed.

## CLI Tool

Use the `nr_api.py` script to control the engine.

### Usage
```bash
# List all flows (JSON)
python3 scripts/nr_api.py list-flows

# Get specific flow by ID
python3 scripts/nr_api.py get-flow --id <flow_id>

# Deploy a new flows file
python3 scripts/nr_api.py deploy --file /path/to/flows.json
```

## Best Practices
- **Backup:** Always keep a copy of `flows.json` before deploying major changes.
- **Isolation:** Use different tabs in Node-RED for different project scopes.
- **Security:** Ensure the `.env` file is never pushed to public repositories.

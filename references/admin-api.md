# Node-RED API & Flow Guidelines

## Admin API
- **Endpoint**: `/red/admin` (Default)
- **Auth**: Bearer Token required.
- **Methods**:
  - `GET /flows`: List current flows.
  - `POST /flows`: Deploy/Update flows.
  - `POST /nodes`: Install npm module.

## Flow Design (Best Practices)
- **Error Handling**: Use `catch` nodes for global error management.
- **Context**: Use `flow` or `global` context for state, not function variables.
- **Subflows**: Encapsulate reusable logic.
- **Link Nodes**: Use link nodes instead of long wires (spaghetti flow).

## Security
- **Dashboard**: Always secure `/ui` with basic auth or OAuth.
- **Editor**: Secure `/red` with strong password.
- **Exec Node**: Avoid using `exec` unless strictly necessary (RCE risk).

# API Gateway

Passthrough proxy for direct access to third-party APIs using managed OAuth connections, provided by [Maton](https://maton.ai).

## Quick Start

```bash
# Native Slack API call
python <<'EOF'
import urllib.request, os, json
data = json.dumps({'channel': 'C0123456', 'text': 'Hello from gateway!'}).encode()
req = urllib.request.Request('https://gateway.maton.ai/slack/api/chat.postMessage', data=data, method='POST')
req.add_header('Authorization', f'Bearer {os.environ["MATON_API_KEY"]}')
req.add_header('Content-Type', 'application/json')
print(json.dumps(json.load(urllib.request.urlopen(req)), indent=2))
EOF
```

## Base URL

```
https://gateway.maton.ai/{app}/{native-api-path}
```

## Authentication

All requests require the Maton API key:
```bash
export MATON_API_KEY="YOUR_API_KEY"
```

## Connection Management

### List Connections
```bash
curl -H "Authorization: Bearer $MATON_API_KEY" \
  "https://ctrl.maton.ai/connections?app=slack&status=ACTIVE"
```

### Create Connection
```bash
curl -X POST -H "Authorization: Bearer $MATON_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"app": "slack"}' \
  "https://ctrl.maton.ai/connections"
```

## Supported Services

| Service | App Name |
|---------|----------|
| Slack | `slack` |
| GitHub | `github` |
| Notion | `notion` |
| Airtable | `airtable` |
| Google Calendar | `google-calendar` |
| Google Drive | `google-drive` |
| Gmail | `google-mail` |
| HubSpot | `hubspot` |
| Salesforce | `salesforce` |
| +100 more | ... |

See [Maton documentation](https://maton.ai) for full list.

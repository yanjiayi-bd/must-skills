# Proactive Agent

Transform AI from a task executor into a proactive partner that anticipates needs and takes initiative.

## Overview

Proactive Agent enables OpenClaw to:
- **Monitor** environment changes and user patterns
- **Anticipate** upcoming needs before explicit requests
- **Act** autonomously within defined boundaries
- **Learn** from outcomes to improve future predictions

## Usage

```bash
# Set a goal and let the agent work autonomously
/proactive "Monitor my calendar and prepare meeting materials 30 minutes before each meeting"

# Configure proactive behaviors
/proactive config --add "daily_standup_reminder" --time "09:30" --action "prepare_standup_notes"

# View active proactive tasks
/proactive list

# Pause/resume proactive behaviors
/proactive pause "daily_standup_reminder"
/proactive resume "daily_standup_reminder"
```

## Key Features

### 1. Autonomous Planning
- Break down high-level goals into actionable steps
- Self-correct when encountering obstacles
- Report progress and blockers proactively

### 2. Environment Monitoring
- Watch file changes, calendar updates, messages
- Detect patterns in user behavior
- Trigger actions based on conditions

### 3. Contextual Awareness
- Maintain long-term context across sessions
- Understand implicit needs from context
- Adapt behavior based on time, location, history

## Configuration

```json
{
  "proactive": {
    "enabled": true,
    "permissions": {
      "auto_execute": ["read", "summarize", "notify"],
      "ask_confirmation": ["write", "delete", "send"]
    },
    "behaviors": [
      {
        "name": "meeting_prep",
        "trigger": "calendar.event_starting_soon",
        "action": "prepare_meeting_brief"
      }
    ]
  }
}
```

## Data (ClawHub Rank #10)

- **Deployments**: 7,010+
- **Active Users**: 340+
- **Rating**: 4.6/5.0

## Safety Considerations

⚠️ **Important**: Proactive Agent has elevated permissions:
- Review all configured behaviors regularly
- Set clear boundaries for autonomous actions
- Use confirmation prompts for destructive operations
- Monitor agent activity logs

## Examples

```bash
# Auto-organize downloaded files
/proactive "Organize all files in ~/Downloads by type and date weekly"

# Smart email triage
/proactive "Check emails every hour, summarize important ones, draft responses for my review"

# Code review assistant
/proactive "Monitor repository for new PRs, perform initial review, notify me of critical issues"

# Personal assistant mode
/proactive "Learn my daily routine and proactively suggest optimizations"
```

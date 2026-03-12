# Find Skills

Skill discovery and management tool for OpenClaw. Acts as a package manager for skills - search, install, update from ClawHub and GitHub.

## Installation

```bash
# Install the skills CLI globally
npm install -g skills

# Or use via npx (no install required)
npx skills <command>
```

## Commands

### Search Skills
```bash
# Search for skills by keyword
npx skills find "web search"
npx skills find "github"

# Search with filters
npx skills find "productivity" --sort downloads
```

### Install Skills
```bash
# Install from ClawHub
npx skills add <skill-slug>
npx skills add tavily-search

# Install from GitHub URL
npx skills add https://github.com/author/skill-repo

# Install with confirmation (safer)
npx skills add <skill> --no-y

# Install multiple skills
npx skills add skill1 skill2 skill3
```

### Check for Updates
```bash
# Check which skills have updates
npx skills check

# Update all skills
npx skills update

# Update specific skill
npx skills update <skill-name>
```

### List Installed Skills
```bash
# Show all installed skills
npx skills list

# Show with details
npx skills list --verbose
```

## Security Best Practices

⚠️ **Important Safety Tips:**

1. **Review before install**: Check skill source, author reputation, and GitHub stars
2. **Avoid silent install**: Use `--no-y` flag to review what will be installed
3. **Audit regularly**: Run `npx skills list` and remove unused skills
4. **Prefer verified skills**: Choose skills with high downloads and "Benign" security rating
5. **Isolate environment**: Use Docker or VM for testing unknown skills

## Data (ClawHub Rank #5)

- **Deployments**: 87.6k+
- **GitHub Stars**: 398
- **Active Users**: 837
- **Security**: Passed VirusTotal scan (Benign)

## Integration with OpenClaw

After installing skills via `find-skills`, activate them in OpenClaw:

```bash
# Install via find-skills
npx skills add self-improving-agent

# Then activate in OpenClaw
openclaw skills install ./path/to/self-improving-agent
```

## Tips

- Use natural language: "Find me a skill for PR review"
- Skills are categorized: Web Development, DevOps, Productivity, Media, etc.
- Check `awesome-openclaw-skills` repository for curated lists
- Most popular skills: `self-improving-agent`, `tavily-search`, `gog`, `github`

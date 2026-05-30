# Linear Digressions Wiki

A local MCP server that lets you query the [Linear Digressions](https://lineardigressions.com) knowledge base directly from [Claude Code](https://claude.ai/code). Ask questions about episodes, topics, and concepts — get back cited answers drawn from the podcast's archive.

The wiki is maintained by the podcast hosts and updated after each episode. You run the server locally; your own Anthropic API key powers the queries.

---

## What you need

- Python 3.11 or later
- An [Anthropic API key](https://console.anthropic.com/)
- [Claude Code](https://claude.ai/code) (the CLI or desktop app)

---

## Setup

**1. Clone this repo**

```bash
git clone https://github.com/cmmalone/ld-wiki.git
cd ld-wiki
```

**2. Install dependencies**

```bash
pip install -r requirements.txt
```

Or with a virtual environment (recommended):

```bash
python -m venv .venv
source .venv/bin/activate        # macOS / Linux
.venv\Scripts\activate           # Windows
pip install -r requirements.txt
```

**3. Add your API key**

```bash
cp .env.example .env
```

Open `.env` and replace `sk-ant-...` with your actual Anthropic API key.

**4. Register the server with Claude Code**

Open `~/.claude.json` and add an entry under `mcpServers`:

```json
{
  "mcpServers": {
    "ld-wiki": {
      "command": "python",
      "args": ["/absolute/path/to/ld-wiki/server_public.py"]
    }
  }
}
```

Replace `/absolute/path/to/ld-wiki` with the actual path where you cloned this repo. If you used a virtual environment, use the full path to that Python instead:

```json
"command": "/absolute/path/to/ld-wiki/.venv/bin/python"
```

**5. Verify it's working**

Start a new Claude Code session and run `/mcp`. You should see `ld-wiki` listed as a connected server.

---

## Using it

Once registered, you can ask questions directly in Claude Code:

> *"What has Linear Digressions said about transformer architectures?"*

> *"Which episodes cover reinforcement learning from human feedback?"*

> *"What's the difference between how the show covered frequentist vs. Bayesian statistics?"*

The server reads all wiki pages, passes them to Claude, and returns a cited answer that references specific episode and concept pages.

---

## Staying current

The wiki is updated after each new episode. To get the latest:

```bash
git pull
```

No restart needed — the server reads from disk on every query.

---

## Notes

- Wiki content is © Linear Digressions. This repository is the query interface; the podcast content belongs to the show.
- The server runs entirely on your machine. Your questions and the wiki content are sent to Anthropic's API using your key, subject to [Anthropic's privacy policy](https://www.anthropic.com/privacy).
- For large wikis, query latency scales with the number of pages (all pages are loaded per query). This is a known limitation and may be addressed in a future version.

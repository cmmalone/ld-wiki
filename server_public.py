"""
Linear Digressions wiki — public MCP server.

Exposes a single tool: query_wiki. Reads markdown files from wiki/ (relative
to this file), calls Claude Sonnet, and returns a cited answer.

Setup: see README.md.
"""

from __future__ import annotations

import asyncio
import os
import textwrap
from pathlib import Path
from typing import Any

import anthropic
import mcp.server.stdio
import mcp.types as types
from dotenv import load_dotenv
from mcp.server import Server

load_dotenv(Path(__file__).parent / ".env")

WIKI_DIR = Path(__file__).parent / "wiki"

_api_key = os.environ.get("ANTHROPIC_API_KEY", "")
if not _api_key:
    raise RuntimeError(
        "ANTHROPIC_API_KEY is not set — copy .env.example to .env and add your key."
    )

# Synced from linear-digressions-agent/agent/tools/wiki.py — update both if prompts change
QUERY_SYSTEM = textwrap.dedent("""\
    You are an assistant for "Linear Digressions", a podcast about data science,
    machine learning, and AI. You have access to the podcast's wiki — a collection
    of episode summaries and concept pages.

    Answer the user's question by synthesizing information from the wiki pages
    provided. Always cite which episodes or concept pages you're drawing from.
    Be specific and grounded in what the podcast actually said — don't extrapolate
    beyond the wiki content.
""")

QUERY_USER = textwrap.dedent("""\
    ## Question
    {question}

    ## Wiki pages available

    {wiki_content}

    Answer the question based on the wiki content above, citing episodes and concepts.
""")

app = Server("ld-wiki")


@app.list_tools()
async def list_tools() -> list[types.Tool]:
    return [
        types.Tool(
            name="query_wiki",
            description=(
                "Answer a question by reading the Linear Digressions wiki and synthesizing "
                "across episode summaries and concept pages. Returns an answer with citations."
            ),
            inputSchema={
                "type": "object",
                "properties": {
                    "question": {
                        "type": "string",
                        "description": "The question to answer from the wiki",
                    },
                },
                "required": ["question"],
            },
        )
    ]


@app.call_tool()
async def call_tool(name: str, arguments: dict[str, Any]) -> list[types.TextContent]:
    if name == "query_wiki":
        question = arguments.get("question", "")
        if not question:
            return [types.TextContent(type="text", text="No question provided.")]
        return await _query_wiki(question)
    return [types.TextContent(type="text", text=f"Unknown tool: {name}")]


def _load_wiki_pages() -> list[str]:
    pages = []
    for subdir in ["episodes", "concepts"]:
        folder = WIKI_DIR / subdir
        if folder.exists():
            for md_file in sorted(folder.glob("*.md")):
                if md_file.name == ".gitkeep":
                    continue
                content = md_file.read_text(encoding="utf-8")
                pages.append(f"### {subdir}/{md_file.name}\n\n{content}")
    return pages


async def _query_wiki(question: str) -> list[types.TextContent]:
    pages = _load_wiki_pages()
    if not pages:
        return [types.TextContent(
            type="text",
            text=(
                "The wiki has no pages yet. Make sure you've run `git pull` to get "
                "the latest content, or check that wiki/episodes/ and wiki/concepts/ "
                "contain .md files."
            ),
        )]

    wiki_content = "\n\n---\n\n".join(pages)
    client = anthropic.Anthropic(api_key=_api_key)
    response = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=2048,
        system=QUERY_SYSTEM,
        messages=[{
            "role": "user",
            "content": QUERY_USER.format(question=question, wiki_content=wiki_content),
        }],
    )
    return [types.TextContent(type="text", text=response.content[0].text)]


async def main() -> None:
    async with mcp.server.stdio.stdio_server() as (read_stream, write_stream):
        await app.run(read_stream, write_stream, app.create_initialization_options())


if __name__ == "__main__":
    asyncio.run(main())

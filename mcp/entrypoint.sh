#!/bin/bash
echo "Server url"
echo ${HOST}
echo "Server port"
echo ${PORT}

# Start application
uv venv .venv
uv pip install datacommons-mcp
# uv run datacommons-mcp serve http --host localhost --port 50055
uv run datacommons-mcp serve http --host ${HOST} --port ${PORT}
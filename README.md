# CIRNO Web Search Agent

A web search and Data Commons data collection agent for the CIRNO multi-agent system. This agent is built on the and provides web search capabilities and structured data querying.

## ✨ Features

- 🔍 **Intelligent Web Search**: Uses Exa API for precise, real-time web content retrieval
- 📊 **Data Commons Querying**: Accesses structured public datasets through MCP servers
- 🤖 **Multi-Agent Collaboration**: Integrates with the CIRNO multi-agent system, supporting task distribution and collaborative work
- 🚀 **Docker Containerization**: Complete Docker Compose deployment solution
- 🔄 **Real-time Streaming Responses**: Supports streaming output for better user experience
- 📝 **Configurable Skills**: Supports custom search skills and query examples

## 🏗️ System Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                    CIRNO Multi-Agent System                 │
├─────────────────────────────────────────────────────────────┤
│  ┌─────────────┐     ┌─────────────┐     ┌─────────────┐  │
│  │   Other     │◄────┤   Task      │────►│   Web Search│  │
│  │   Agents    │     │  Coordinator│     │    Agent    │  │
│  └─────────────┘     └─────────────┘     └─────────────┘  │
└─────────────────────────────────────────────────────────────┘
                              │
                     ┌────────▼─────────┐
                     │   a2a Framework  │
                     │   Service Layer  │
                     │  • Task Management│
                     │  • Push Notifications│
                     │  • API Interface │
                     └────────┬─────────┘
                     ┌────────▼─────────┐
                     │   Agent Executor │
                     │  • Skill Routing │
                     │  • Tool Invocation│
                     └────────┬─────────┘
               ┌──────────────┼──────────────┐
        ┌──────▼──────┐ ┌─────▼─────┐ ┌──────▼──────┐
        │   Exa API   │ │ Data      │ │   LLM       │
        │  Web Search │ │ Commons   │ │  Model      │
        │             │ │ MCP Server│ │  Service    │
        └─────────────┘ └───────────┘ └─────────────┘
```

## 🚀 Quick Start

### Prerequisites

- [Docker](https://docs.docker.com/get-docker/) and [Docker Compose](https://docs.docker.com/compose/install/)
- [Git](https://git-scm.com/downloads)
- API keys (Exa, LLM)

### 1. Clone the Project

```bash
git clone https://github.com/StudentAssistantTeam/CIRNO_WebSearchAgent.git
cd CIRNO_WebSearchAgent
```

### 2. Configure Environment Variables

Edit the configuration files:

```bash
# Edit Web Search Agent environment configuration
vim cirno_web_search_agent/cirno_web_search_agent.env

# Edit MCP server environment configuration (if needed)
vim mcp/.env
```

#### Agent Configuration

Example configuration file (`cirno_web_search_agent/cirno_web_search_agent.env`):

```bash
# MCP Configuration
MCP_URL=http://data-commons-mcp:50055

# LLM Configuration (Alibaba Cloud DashScope)
LLM_BASE_URL=https://dashscope-intl.aliyuncs.com/compatible-mode/v1
LLM_API_KEY=your_dashscope_api_key_here
LLM_MODEL_NAME=qwen-plus

# Exa API Configuration
EXA_API_KEY=your_exa_api_key_here

# a2a Server Configuration
A2A_HOST=0.0.0.0
A2A_PORT=4002
USE_DB_PUSH_NOTIFICATIONS=false
USE_DB_TASK_STORE=false
```

#### MCP Configuration

```bash
DC_API_KEY=YOUR_DC_API_KEY_HERE
HOST=localhost
PORT=50055
```

### 3. Start Services

```bash
# Start all services using Docker Compose
docker-compose up -d
```

### 4. Verify Deployment

```bash
# Check service status
docker-compose ps

# View logs
docker-compose logs -f cirno_web_search_agent

# Access health check endpoint
curl http://localhost:4002/health
```

## ⚙️ Configuration

### Environment Variables

| Variable | Description | Default | Required |
|----------|-------------|---------|----------|
| `MCP_URL` | Data Commons MCP server address | `http://data-commons-mcp:50055` | Yes |
| `LLM_BASE_URL` | LLM API base URL | DashScope compatible endpoint | Yes |
| `LLM_API_KEY` | LLM API key | - | Yes |
| `LLM_MODEL_NAME` | LLM model name | `qwen-plus` | Yes |
| `EXA_API_KEY` | Exa API key | - | Yes |
| `A2A_HOST` | a2a server host | `0.0.0.0` | No |
| `A2A_PORT` | a2a server port | `4002` | No |
| `USE_DB_PUSH_NOTIFICATIONS` | Use database push notifications | `false` | No |
| `USE_DB_TASK_STORE` | Use database task store | `false` | No |
| `DB_URL` | Database connection URL (if using database) | - | No |

### API Key Acquisition

1. **Exa API**:
   - Visit [Exa website](https://exa.ai/) to register an account
   - Obtain API key from the console

2. **DashScope LLM**:
   - Visit [Alibaba Cloud DashScope](https://dashscope.aliyun.com/)
   - Create API key, select `qwen-plus` or compatible model

3. **Other LLM Services**:
   - Can be configured with OpenAI-compatible API endpoints
   - Supports any LLM service that conforms to OpenAI API specification

4. **Data Commons API**
    - Visit [Data Commons website](https://datacommons.org/) to register an account

## 🛠️ Development Guide

### Local Development Environment

1. **Python Environment Setup**:

```bash
# Navigate to agent directory
cd cirno_web_search_agent

# Install uv (Python package manager)
pip install uv

# Install dependencies
uv sync
```

2. **Run Local Development Server**:

```bash
uv run cirno_web_search_agent_app
```

## 🐳 Deployment

### Docker Deployment

```bash
# Build and start all services
docker-compose up -d

# Stop services
docker-compose down

# Clean up resources
docker-compose down -v
```

## 🔧 Troubleshooting

### Common Issues

1. **Service Startup Failure**:
   ```bash
   # Check Docker logs
   docker-compose logs cirno_web_search_agent
   
   # Check port occupancy
   netstat -an | grep 4002
   ```

2. **API Key Errors**:
   - Confirm API keys in environment file are correct
   - Check if keys have expired or lack permissions

3. **MCP Connection Failure**:
   - Confirm MCP service is running
   - Check `MCP_URL` configuration is correct
   - Verify network connectivity

### Log Analysis

```bash
# View real-time logs
docker-compose logs -f cirno_web_search_agent

# View logs for specific time period
docker-compose logs --since 10m cirno_web_search_agent

# Search for error logs
docker-compose logs cirno_web_search_agent | grep -i error
```

## 🤝 Contributing

We welcome contributions! 

## 📄 License

This project is released under the [MIT License](LICENSE).

---

**CIRNO Web Search Agent** - Providing powerful search and data collection capabilities for the CIRNO multi-agent system
# SPagent Demos - Azure AI Foundry Agent Examples

Agent demos for customer environment, S&P. This repository contains a progressive series of Python demonstrations showcasing Azure AI Foundry Agent capabilities, from basic connection testing to advanced agent tool integration.

## Table of Contents
- [Prerequisites](#prerequisites)
- [Setup Instructions](#setup-instructions)
- [Demo Scripts Overview](#demo-scripts-overview)
- [Running the Demos](#running-the-demos)
- [File Structure](#file-structure)

## Prerequisites

Before running these demos, ensure you have:

- Python 3.8 or higher
- An Azure AI Foundry project set up
- Access to an Azure AI model deployment
- Azure credentials configured on your machine

## Setup Instructions
For a full set-up guide, see the folder **setup** in this repo that has step by step instructions.

### 1. Clone the Repository
```bash
git clone https://github.com/gabycb/SPagent_demos.git
cd SPagent_demos
```

### 2. Create Virtual Environment (Recommended)
```bash
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

1. Copy the example environment file:
   ```bash
   cp .env.example .env
   ```

2. Edit the `.env` file with your Azure credentials:
   ````
   PROJECT_ENDPOINT=https://your-project-endpoint.cognitiveservices.azure.com/
   MODEL_DEPLOYMENT_NAME=your-model-deployment-name
   ```

### 5. Authentication

The demos use `DefaultAzureCredential` for authentication. Configure your Azure credentials using one of these methods:
- Azure CLI: `az login`
- Environment variables: Set `AZURE_TENANT_ID`, `AZURE_CLIENT_ID`, `AZURE_CLIENT_SECRET`
- Managed Identity (if running in Azure)

## Demo Scripts Overview

This repository contains four progressive demo scripts that demonstrate increasing levels of Azure AI Foundry Agent functionality:

### 📋 01. `01project_connection_test.py`
**Purpose**: Basic Project Connection Test

Validates that you can successfully connect to your Azure AI Foundry project and authenticate with Azure credentials.

**What it does**:
- Establishes a connection to the Azure AI Foundry project using the provided endpoint
- Authenticates using `DefaultAzureCredential`
- Confirms successful connection to the project

**Key concepts**:
- Azure authentication and credential handling
- AIProjectClient initialization
- Resource management with context managers

**When to run**: Start here first to verify your setup is correct

---

### 🔗 02. `02openai_response_test.py`
**Purpose**: OpenAI Client Response Testing

Tests the OpenAI client connection to Foundry and demonstrates retrieving responses from your deployed model.

**What it does**:
- Connects to your Azure AI Foundry project
- Uses the OpenAI client to send prompts to your model deployment
- Retrieves and displays model responses
- Demonstrates conversation context by using `previous_response_id` for follow-up questions

**Example workflow**:
1. Ask the model: "What is the size of France in square miles?"
2. Follow up with: "And what is the capital city?" (maintaining conversation context)

**Key concepts**:
- OpenAI client integration with Azure AI Foundry
- Request/response cycle with model deployments
- Conversation context management

**Reference**: [Microsoft's OpenAI Client Guide](https://learn.microsoft.com/en-us/python/api/overview/azure/ai-projects-readme?view=azure-python-preview#performing-responses-operations-using-openai-client)

---

### 🤖 03. `03agent_test.py`
**Purpose**: Agent Creation and Basic Interaction

Demonstrates creating an AI agent and interacting with it through conversations.

**What it does**:
- Creates an agent named "MyAgent" with a specific system instruction
- Establishes a conversation with the agent
- Sends user messages to the agent
- Retrieves and displays agent responses

**Key concepts**:
- Agent creation and versioning
- PromptAgentDefinition configuration
- Conversation management
- Agent system instructions

**Use case**: Foundation for building more complex agent interactions

---

### 🛠️ 04. `04agent_tool_test.py`
**Purpose**: Agent with Built-in Tools

Demonstrates creating an agent that can use built-in tools (like Code Interpreter) to answer complex questions.

**What it does**:
- Creates an agent with CodeInterpreterTool capability
- Sends a complex task requiring code execution (generate a multiplication chart)
- Forces the agent to use tools with `tool_choice="required"`
- Displays the code executed by the tool and the final response

**Example task**: "Could you please generate a multiplication chart for the numbers 1 through 5?"

**Key concepts**:
- Tool declaration and integration
- CodeInterpreterTool for programmatic problem-solving
- Tool-driven agent responses
- Extracting and displaying tool execution results

**Reference**: [Azure SDK Built-in Tools Guide](https://github.com/Azure/azure-sdk-for-python/blob/main/sdk/ai/azure-ai-projects/README.md#built-in-tools)

---

## Running the Demos

Run the demo scripts in order. Each script builds on the previous one:

```bash
# Step 1: Test basic connection
python 01project_connection_test.py

# Step 2: Test OpenAI model responses
python 02openai_response_test.py

# Step 3: Test agent creation and interaction
python 03agent_test.py

# Step 4: Test agent with tools
python 04agent_tool_test.py
```

### Expected Output Examples

Each script will print confirmation messages and responses. You should see output like:
- Connection confirmations
- Model responses to prompts
- Agent IDs and conversation IDs
- Code executed by tools
- Final text output from agents

## File Structure

```
SPagent_demos/
├── README.md                          # This file
├── requirements.txt                   # Python dependencies
├── .env.example                       # Example environment variables
├── .gitignore                         # Git ignore patterns
├── 01project_connection_test.py       # Demo 1: Connection test
├── 02openai_response_test.py          # Demo 2: OpenAI responses
├── 03agent_test.py                    # Demo 3: Agent basics
├── 04agent_tool_test.py               # Demo 4: Agent with tools
└── setup/                             # Setup utilities (if present)
```

## Dependencies

Key packages used in these demos:
- **azure-identity** (≥1.17.1): Azure authentication
- **azure-ai-projects** (2.0.0b4): Azure AI Foundry project client
- **azure-ai-agents** (1.2.0b5): Agent framework
- **python-dotenv** (≥1.0.1): Environment variable management
- **openai**: OpenAI client for model interactions

See `requirements.txt` for complete dependency list.

## Troubleshooting

### Connection Issues
- Verify `PROJECT_ENDPOINT` and `MODEL_DEPLOYMENT_NAME` in `.env`
- Check Azure authentication: run `az login`
- Ensure your Azure account has access to the AI Foundry project

### Module Not Found Errors
- Activate your virtual environment
- Run `pip install -r requirements.txt`
- Verify Python version is 3.8+

### Model Deployment Errors
- Confirm the model deployment name matches your Azure resource
- Check that the deployment is active and not paused

## Next Steps

After successfully running all demos:
- Explore modifying prompts and system instructions
- Implement custom tools beyond CodeInterpreterTool
- Build more complex multi-turn conversations
- Integrate agents into your applications

## Resources

- [Azure AI Foundry Documentation](https://learn.microsoft.com/en-us/azure/ai-foundry/)
- [Azure AI Projects Python SDK](https://learn.microsoft.com/en-us/python/api/overview/azure/ai-projects-readme)
- [OpenAI API Documentation](https://platform.openai.com/docs)

## License

This project is provided for demonstration and educational purposes in the S&P customer environment.

---

**Last Updated**: March 2026

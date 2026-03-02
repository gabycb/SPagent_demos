# 1. Assuming you have completed the steps in project_connection_test.py to connect to Foundry
## follow this guide for testing responses using agent property on AIProjectClient
## https://github.com/Azure/azure-sdk-for-python/blob/main/sdk/ai/azure-ai-projects/README.md#built-in-tools
# 2. This code tests the .agent client with built-in tool connection to Foundry and retrieves a response from the model deployment specified in the .env file. 
# Make sure to set the PROJECT_ENDPOINT and MODEL_DEPLOYMENT_NAME environment variables in your .env file before running this test.
import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential
from azure.ai.projects.models import PromptAgentDefinition, CodeInterpreterTool


# construct synchronous client and credential instances using context managers to ensure proper cleanup of resources
with (
    DefaultAzureCredential() as credential,
    AIProjectClient(endpoint=os.getenv("PROJECT_ENDPOINT"), credential=DefaultAzureCredential()) as project_client
):
# use the .agent client to create an agent, send messages to it, and retrieve responses
    # start tool declaration
    tool = CodeInterpreterTool()
    # end tool declaration

    #create agent with tool included in the definition
    with project_client.get_openai_client() as openai_client:
        agent = project_client.agents.create_version(
            agent_name="MyAgent",
            definition=PromptAgentDefinition(
                model=os.environ["MODEL_DEPLOYMENT_NAME"],
                instructions="You are a helpful assistant that answers general questions",
                tools=[tool], # include tool in agent definition
            ),
            description="Agent with code interpreter tool included in the definition",
        )
        print(f"Agent created (id: {agent.id}, name: {agent.name}, version: {agent.version})")

        conversation = openai_client.conversations.create()
        print(f"Created conversation with initial user message (id: {conversation.id})")

        response = openai_client.responses.create(
            conversation=conversation.id,
            input="Could you please generate a multiplication chart for the numbers 1 through 5? You can use the code interpreter tool to generate the chart.",
            extra_body={"agent_reference": {"name": agent.name, "type": "agent_reference"}},
            tool_choice="required", # specify that the agent must use a tool to answer this question
        )
        print(f"Response id: {response.id}")

        # Print code executed by the tool and its output
        code = next((output.code for output in response.output if output.type=="code_interpreter_call"),"")
        print(f"Code executed by the tool: {code}")

        # Print final assistant text output
        print(f"Final assistant text output: {response.output_text}")

        print("\nCleaning up..")
        #project_client.agents.delete_version(agent_name=agent.name, agent_version=agent.version)
        #print("Agent deleted")
# 1. Assuming you have completed the steps in project_connection_test.py to connect to Foundry
## follow this guide for testing responses using agent property on AIProjectClient
## https://github.com/Azure/azure-sdk-for-python/blob/main/sdk/ai/azure-ai-projects/README.md#performing-agent-operations

# 2. This code tests the .agent client connection to Foundry and retrieves a response from the model deployment specified in the .env file. 
# Make sure to set the PROJECT_ENDPOINT and MODEL_DEPLOYMENT_NAME environment variables in your .env file before running this test.
import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential
from azure.ai.projects.models import PromptAgentDefinition 


# construct synchronous client and credential instances using context managers to ensure proper cleanup of resources
with (
    DefaultAzureCredential() as credential,
    AIProjectClient(endpoint=os.getenv("PROJECT_ENDPOINT"), credential=DefaultAzureCredential()) as project_client
):
# use the .agent client to create an agent, send messages to it, and retrieve responses
    with project_client.get_openai_client() as openai_client:
        agent = project_client.agents.create_version(
            agent_name="MyAgent",
            definition=PromptAgentDefinition(
                model=os.environ["MODEL_DEPLOYMENT_NAME"],
                instructions="You are a helpful assistant that answers general questions",
            ),
        )
        print(f"Agent created (id: {agent.id}, name: {agent.name}, version: {agent.version})")

        conversation = openai_client.conversations.create(
            items=[{"type": "message", "role": "user", "content": "What is the size of France in square miles?"}],
        )
        print(f"Created conversation with initial user message (id: {conversation.id})")

        response = openai_client.responses.create(
            conversation=conversation.id,
            extra_body={"agent_reference": {"name": agent.name, "type": "agent_reference"}},
        )
        print(f"Response output: {response.output_text}")

        openai_client.conversations.items.create(
            conversation_id=conversation.id,
            items=[{"type": "message", "role": "user", "content": "And what is the capital city?"}],
        )
        print(f"Added a second user message to the conversation")

        response = openai_client.responses.create(
            conversation=conversation.id,
            extra_body={"agent_reference": {"name": agent.name, "type": "agent_reference"}},
        )
        print(f"Response output: {response.output_text}")

        openai_client.conversations.delete(conversation_id=conversation.id)
        print("Conversation deleted")

    project_client.agents.delete_version(agent_name=agent.name, agent_version=agent.version)
    print("Agent deleted")
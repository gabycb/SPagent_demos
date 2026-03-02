# 1. Assuming you have completed the steps in project_connection_test.py to connect to Foundry
## follow this guide for testing responses using openAI client
## https://learn.microsoft.com/en-us/python/api/overview/azure/ai-projects-readme?view=azure-python-preview#performing-responses-operations-using-openai-client

# 2. This code tests the OpenAI client connection to Foundry and retrieves a response from the model deployment specified in the .env file. 
# Make sure to set the PROJECT_ENDPOINT and MODEL_DEPLOYMENT_NAME environment variables in your .env file before running this test.
import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential

# construct synchronous client and credential instances using context managers to ensure proper cleanup of resources
with (
    DefaultAzureCredential() as credential,
    AIProjectClient(endpoint=os.getenv("PROJECT_ENDPOINT"), credential=DefaultAzureCredential()) as project_client
):
    # use the client to call the OpenAI API and get a response from the specified model deployment
    with project_client.get_openai_client() as openai_client:
        response = openai_client.responses.create(
            model=os.getenv("MODEL_DEPLOYMENT_NAME"),
            input= "What is the size of France in square miles?",
        )
        print(f"Response from OpenAI model deployment: {response.output_text}")

        response = openai_client.responses.create(
            model=os.getenv("MODEL_DEPLOYMENT_NAME"),
            input="And what is the capital city?",
            previous_response_id=response.id , # Pass the ID of the previous response to maintain context in the conversation
        )
        print(f"Response to follow-up question from OpenAI model deployment: {response.output_text}")
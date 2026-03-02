# Steps to connect to Foundry
# 1. Follow the steps in the set up guide, including installing the required packages from requirements.txt

# 2. For local login, complete via terminal: az login
## Confirm you have Azure CLI installed: az --version, if not, install from https://learn.microsoft.com/en-us/cli/azure/install-azure-cli-windows?view=azure-cli-latest&pivots=msi
## If cannot install, use Azure extension: Azure Resources or use Device Code Azure Account extension to sign in to Azure and set the subscription

# 3. Confirm you have set environment variables for Foundry connection
## You can set these in a .env file in the same directory as this script, or set them in your environment variables
## Required environment variables:
### PROJECT_ENDPOINT: The endpoint URL for your Foundry project, which can be found in the Foundry portal under your project settings
### MODEL_DEPLOYMENT_NAME: The name of the model deployment you want to connect to, which can be found in the Foundry portal under your project settings -> Model Deployments
## Optional environment variables, if not already authenticated via Azure extension per set up guide:
### AZURE_CLIENT_ID: The client ID of your Azure AD application
### AZURE_TENANT_ID: The tenant ID of your Azure AD
### AZURE_SUBSCRIPTION_ID: The subscription ID where your Foundry instance is deployed
### FOUNDRY_RESOURCE_GROUP: The resource group where your Foundry instance is deployed
### FOUNDRY_INSTANCE_NAME: The name of your Foundry instance

# 4. Test the connection to Foundry by running this script, which will attempt to connect to the specified model deployment and print the result
import os
from dotenv import load_dotenv
from azure.identity import DefaultAzureCredential
from azure.ai.projects import AIProjectClient

load_dotenv()  # Load environment variables from .env file

endpoint = os.getenv("PROJECT_ENDPOINT")
if not endpoint:
    raise ValueError("PROJECT_ENDPOINT environment variable is not set. Please set it in your .env file or environment variables.")

client = AIProjectClient(endpoint=endpoint, credential=DefaultAzureCredential())

with client:
    try:
        # Attempt to get project details to confirm connection
        agents_client = client.agents
        print("Successfully connected to Foundry project!")
        print(f"Agents Client: {agents_client}")
    except Exception as e:
        print("Failed to connect to Foundry project.")
        print(f"Error: {e}")


# 5. Run this code in your terminal: python project_connection_test.py      

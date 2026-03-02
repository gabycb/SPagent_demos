# Guide: Accessing Foundry Portal, Getting Endpoint, Loading GitHub Repo in VS Code, and Testing Files

## 1. Access the Foundry Portal
1. Open your web browser.
2. Navigate to the Foundry Portal URL https://ai.azure.com/.
3. Log in with your corporate credentials.
4. Once logged in, use the search bar or navigation panel to locate your project.

## 2. Retrieve an Endpoint in Foundry
1. From your project, go to the **Overview** tab on the left-hand menu, and you should see a screen that says project and **Endpoints and keys** section.
2. Select the Microsoft Foundry option under Libraries, and copy the Microsoft Foundry project endpoint. This endpoint allows us to connect to Azure Open and Azure AI services easily, but you can also call to those endpoints directly if you prefer. 
3. We are going to use our Microsoft credentials for authentication so you do not need the API key for these samples. If you have other projects and would prefer to connect using API, this is where you can find the API key for authentication.

## 3. Set up Visual Studio Code with Azure Extension
1. Open **Visual Studio Code**.
2. Select **Extensions** or press **Ctrl+Shift+X** (Windows/Linux) to access the extenstions marketplace.
3. For these demos, you need to add **Python** and **Azure** from the extensions marketplace. Search for Python then Azure Resources, and click Install for each. There are various other toolkits for Azure services, but we will only require Azure for these demos.
4. Once the extensions are is installed, you will see them on the left-hand side where you found the Extensions selector (below file explorer).
5. Select the Azure extension, and select the login option. This will prompt you to sign in with your credentials. Use the same ones that you used to sign in to Foundry. This is an easy way to authenticate any use of azure services in Visual Studio Code, and how we will call authenticaiton for agents in these demos.
6. There are other options for authentication, but we will use this toolkit for this demo. At the bottom tab you will see **Accounts and Tenants**, ensure you see your account and S&P Global listed. In the resources tab, you will see a list of subscriptions that are part of the tenant. You will only be able to view the details of the subscription you have access to, but we do not need to select it or do anything else in this extension.
7. The other options for authentication are logging in via the terminal and authenticating using Azure CLI (az login).

## 4. Load a GitHub Repository in Visual Studio Code
1. Open **Visual Studio Code**.
2. Press **Ctrl+Shift+P** (Windows/Linux) or **Cmd+Shift+P** (Mac) to open the command palette.
3. Type `Git: Clone` and select **Git: Clone**.
4. Paste the GitHub repository URL for this repo: https://github.com/gabycb/SPagent_demos.git. 
5. Select a folder on your machine where the repo will be cloned.
6. When prompted, choose **Open Repository** to open it directly in VS Code.
7. If authentication is required for GitHub, sign in when prompted.

## 5. Install Dependencies (Optional)
Depending on the project type:
- For Python: `pip install -r requirements.txt`
- For Node.js: `npm install`
- For Java: ensure Maven/Gradle installs the dependencies

## 6. Connect VS Code to Foundry APIs
1. Selec the .env example file and view the required connections to AI Foundry.
2. Copy or Create a new a `.env` file for storing tokens:
   ```env
   PROJECT_ENDPOINT=<your-endpoint>
   MODEL_DEPLOYMENT_NAME=<name-of-model>
   ```
3. Using the project endpoint from Foundry we got in Step 2, paste that link directly into the .env file. It should look similar to this: https://<subscription>.services.ai.azure.com/api/projects/<project-name>
4. Also copy the model deployment name you have in Foundry, which can be found under Models and endpoints or in the Azure portal. It will be the exact name of the model, gpt-4o, unless you changed it to a custom name in deployment.

## 7. Test Files in VS Code
1. Locate the file you want to test in the **Explorer** panel. Start with 01project_connection_test.py
2. Open the file.
3. For all files eding in py, it's a script so you can run it with:
   - Python: right-click → **Run Python File in Terminal**
   - Node.js: run `node <filename>.js`
   - Shell script: `./script.sh`
4. To run unit tests:
   - Python: `pytest` or use the Test Explorer
   - JavaScript: `npm test`
   - Java: `mvn test` or **Run Tests** in the Testing panel
5. Check the terminal output for results.



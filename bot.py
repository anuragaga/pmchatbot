import os

# Dynamically create the secrets.toml file

secrets_dir = "/root/.streamlit"
secrets_path = os.path.join(secrets_dir, "secrets.toml")

os.makedirs(secrets_dir, exist_ok=True)

secrets_dir = "/tmp/.streamlit"
secrets_path = os.path.join(secrets_dir, "secrets.toml")

os.makedirs(secrets_dir, exist_ok=True)


secrets_content = f"""
[general]

AZURE_CLIENT_ID = "{os.getenv('AZURE_CLIENT_ID')}"
AZURE_CLIENT_SECRET = "{os.getenv('AZURE_CLIENT_SECRET')}"
AZURE_CISCO_OPENAI_APP_KEY = "{os.getenv('AZURE_CISCO_OPENAI_APP_KEY')}"
CISCO_BRAIN_USER_ID = "{os.getenv('CISCO_BRAIN_USER_ID')}"
URL = "{os.getenv('URL')}"
AZURE_ENDPOINT = "{os.getenv('AZURE_ENDPOINT')}"
OPENAI_API_KEY = "{os.getenv('OPENAI_API_KEY')}"
NEO4J_URI = "{os.getenv('NEO4J_URI')}"
NEO4J_USERNAME = "{os.getenv('NEO4J_USERNAME')}"
NEO4J_PASSWORD = "{os.getenv('NEO4J_PASSWORD')}"

"""
# Write the content to the secrets.toml file
with open("/root/.streamlit/secrets.toml", "w") as secrets_file:
    secrets_file.write(secrets_content)



import streamlit as st
import streamlit
from utils import write_message
# from PMagent import generate_response
from PMAgentAzure import generate_response


# Page Config
st.set_page_config("ProjectManager", page_icon=":material/monitoring:")

# Set up Session State
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Hi, I'm a PM Chatbot!  How can I help you?"},
    ]

# Submit handler
def handle_submit(message):
    # Handle the response
    with st.spinner('Thinking...'):
        # # TODO: Replace this with a call to your LLM
        response = generate_response(message)
        write_message('assistant', response)


# Display messages in Session State
for message in st.session_state.messages:
    write_message(message['role'], message['content'], save=False)

# Handle any user input
if prompt := st.chat_input("What is your query?"):
    # Display user message in chat message container
    write_message('user', prompt)

    # Generate a response
    handle_submit(prompt)

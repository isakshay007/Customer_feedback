import os
import streamlit as st
from agents import create_agent, create_env, create_task
import time
from PIL import Image

# Fetch API key from Streamlit secrets and set it as an environment variable
os.environ["OPENAI_API_KEY"] = st.secrets["apikey1"]

# Create environment and agent
def initialize_agent():
    env_id = create_env()
    if env_id is None:
        st.error("Failed to create environment. Please check your API configuration.")
        return None
    agent_id = create_agent(
        env_id=env_id,
        system_prompt="Analyze customer reviews and feedback to provide a summary of common issues and suggestions for improvement.",
        agent_name="Feedback Analyzer",
        agent_persona="Analyze Customer Feedback"
    )
    return agent_id

agent_id = initialize_agent()

# Streamlit application
st.set_page_config(page_title="Customer Feedback Analyzer", layout="wide")

st.title("Customer Feedback Analyzer 🧑‍💻")

st.markdown(
    """
    <style>
    .stTextArea>div>textarea {
        border: 2px solid #4CAF50;
        border-radius: 5px;
        padding: 10px;
    }
    .stButton>button {
        background-color: #4CAF50;
        color: white;
        padding: 15px 32px;
        text-align: center;
        text-decoration: none;
        display: inline-block;
        font-size: 16px;
        margin: 4px 2px;
        cursor: pointer;
        border-radius: 5px;
    }
    .stButton>button:hover {
        background-color: #45a049;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Add some description
st.markdown(
    """
    **Welcome to the Customer Feedback Analyzer! Just share your customer feedback, and we’ll quickly summarize the key issues and offer suggestions for improvement.**
    """
)

feedback = st.text_area("Enter the Customer's Reviews and Feedbacks:", height=300)

# Add a loading spinner
if st.button("Analyze Feedback"):
    if feedback:
        with st.spinner("Analyzing feedback..."):
            time.sleep(2)  # Simulate a delay for the analysis
            task_response = create_task(
                user_id="default_user",
                agent_id=agent_id,
                session_id="example_session",
                message=feedback
            )
        
        st.subheader("Analysis Results")
        st.markdown(task_response)
    else:
        st.error("Please enter some customer feedback before analyzing.")

# Sidebar with links
st.sidebar.title("Quick Links")
st.sidebar.markdown(
    """
    <div style="font-family: Arial, sans-serif; margin-bottom: 15px;">
        <a href="https://www.lyzr.ai/" target="_blank" style="text-decoration: none; font-size: 18px; color: #4CAF50;">🔗 Visit Lyzr</a>
    </div>
    <div style="font-family: 'Courier New', Courier, monospace; margin-bottom: 15px;">
        <a href="https://www.lyzr.ai/book-demo/" target="_blank" style="text-decoration: none; font-size: 18px; color: #FF5733;">📅 Book a Demo</a>
    </div>
    <div style="font-family: Verdana, Geneva, sans-serif; margin-bottom: 15px;">
        <a href="https://discord.gg/nm7zSyEFA2" target="_blank" style="text-decoration: none; font-size: 18px; color: #7289DA;">💬 Join Discord</a>
    </div>
    <div style="font-family: 'Times New Roman', Times, serif; margin-bottom: 15px;">
        <a href="https://join.slack.com/t/genaiforenterprise/shared_invite/zt-2a7fr38f7-_QDOY1W1WSlSiYNAEncLGw" target="_blank" style="text-decoration: none; font-size: 18px; color: #4A154B;">🤝 Join Slack</a>
    </div>
    """,
    unsafe_allow_html=True
)

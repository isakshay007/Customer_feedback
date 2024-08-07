import os

import requests
import json
from dotenv import load_dotenv

load_dotenv()
api = os.getenv("OPENAI_API_KEY")


def create_env():
    url = "https://demo.dev.app.lyzr.ai/environment/"

    payload = json.dumps({
        "features": [
            {
                "type": "SHORT_TERM_MEMORY",
                "config": {},
                "priority": 0
            }
        ],
        "tools": [],
        "llm_api_key": api
    })

    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    result=response.json()
    print(result)
    return result['env_id']
     

def create_agent(env_id, system_prompt, agent_name, agent_persona):
    url = "https://demo.dev.app.lyzr.ai/agent/"

    payload = json.dumps({
        "env_id": env_id,
        "system_prompt": system_prompt,
        "name": agent_name,
        "agent_persona": agent_persona,
        "agent_instructions": "",
        "agent_description": ""
    })
    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    
    result=response.json()
    print(result)
    return result['agent_id']


def create_task(user_id, agent_id, session_id, message):
    url = "https://demo.dev.app.lyzr.ai/chat/"

    payload = json.dumps({
        "user_id": user_id,
        "agent_id": agent_id,
        "session_id": session_id,
        "message": message
    })
    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    
    result=response.json()
    print(result)
    return result['response']


if __name__ == "__main__":
    id=create_env()
    print(id)
    
import requests
import streamlit as st
# Update API Endpoint and Key
API_ENDPOINT = st.secrets["api"]["api_endpoint"]
API_KEY = st.secrets["api"]["api_key"]
def get_gpt4_answer(question, options):
    headers = {
        "Content-Type": "application/json",
        "api-key": API_KEY,
    }

    prompt = f"Here is a multiple-choice question:\n\n{question}\n"
    for i, option in enumerate(options, start=1):
        prompt += f"Option {chr(64 + i)}: {option}\n"
    prompt += "\nPlease select the best answer (A, B, C, or D):"

    payload = {
        "messages": [{"role": "user", "content": prompt}],
        "max_tokens": 10,
        "temperature": 0,
    }

    response = requests.post(API_ENDPOINT, headers=headers, json=payload)
    response.raise_for_status()
    
    response_data = response.json()
    choices = response_data.get("choices", [])
    if choices:
        return choices[0]["message"]["content"].strip()
    return "No Answer"

def get_gpt4_answer(question, options):
    """
    Queries Azure OpenAI GPT-4 for the best answer to a multiple-choice question.

    Args:
        question (str): The MCQ question.
        options (list): A list of options (e.g., ['Option A', 'Option B', 'Option C', 'Option D']).

    Returns:
        str: The answer chosen by GPT-4 (e.g., 'A', 'B', 'C', or 'D').
    """
    headers = {
        "Content-Type": "application/json",
        "api-key": API_KEY,
    }

    # Construct the prompt
    prompt = f"Here is a multiple-choice question:\n\n{question}\n"
    for i, option in enumerate(options, start=1):
        prompt += f"Option {chr(64 + i)}: {option}\n"
    prompt += "\nPlease select the best answer (A, B, C, or D):"

    payload = {
        "messages": [{"role": "user", "content": prompt}],
        "max_tokens": 10,
        "temperature": 0,
    }

    try:
        response = requests.post(API_ENDPOINT, headers=headers, json=payload)
        response.raise_for_status()
        
        response_data = response.json()
        print("Full API Response:", response_data)  # Debugging

        choices = response_data.get("choices", [])
        if not choices:
            raise ValueError("No choices in response.")

        message = choices[0].get("message", {})
        if "content" in message:
            return message["content"].strip()
        else:
            # Handle content filtering
            finish_reason = choices[0].get("finish_reason", "unknown")
            if finish_reason == "content_filter":
                return "Response was filtered due to content restrictions."
            else:
                return f"Response missing content key. Finish reason: {finish_reason}"

    except requests.exceptions.RequestException as e:
        print(f"Request Error: {e}")
        raise
    except Exception as e:
        print(f"Unexpected Error: {e}")
        raise

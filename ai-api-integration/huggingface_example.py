# Huggingface Example

# Run 'pip install requests' in terminal

import os
import requests

API_URL = "https://router.huggingface.co/v1/chat/completions"

headers = {
    "Authorization": f"Bearer {os.getenv('HUGGINGFACE_API_KEY')}",
    "Content-Type": "application/json"
}

def query_huggingface(prompt):
    try:
        response = requests.post(
            API_URL,
            headers=headers,
            json={
                "model": "mistralai/Mistral-7B-Instruct-v0.2",
                "messages": [
                    {"role": "user", "content": prompt}
                ]
            }
        )

        if response.status_code != 200:
            return f"Error: {response.text}"

        result = response.json()
        return result["choices"][0]["message"]["content"]

    except Exception as e:
        return f"Error: {e}"


if __name__ == "__main__":
    prompt = input("Enter your prompt: ")

    print("\nQuerying HuggingFace...\n")

    result = query_huggingface(prompt)

    print("Response:\n")
    print(result)
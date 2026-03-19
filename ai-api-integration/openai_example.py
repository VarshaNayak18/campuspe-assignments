# OpenAI Example

# Run 'pip install openai' in terminal

import os
from openai import OpenAI

# Configure API Key
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Query Function
def query_openai(prompt):
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error: {e}"
    
# Main Execution
prompt = input("Enter your prompt: ")
result = query_openai(prompt)

print("Response:")
print(result)
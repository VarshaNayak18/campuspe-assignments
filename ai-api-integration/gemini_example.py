# Gemini Example

# Run 'pip install google-generativeai' in terminal

import os
import google.generativeai as genai

# Configure API key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def query_gemini(prompt):
    try:
        model = genai.GenerativeModel("gemini-1.5-flash")

        response = model.generate_content(prompt)

        return response.text

    except Exception as e:
        return f"Error: {e}"


if __name__ == "__main__":
    prompt = input("Enter your prompt: ")

    print("\nQuerying Gemini...\n")

    result = query_gemini(prompt)

    print("Response:\n")
    print(result)
# Cohere Example

# Run 'pip install cohere' in terminal

import os
import cohere

# Configure client
co = cohere.Client(os.getenv("COHERE_API_KEY"))

def query_cohere(prompt):
    try:
        response = co.generate(
            model="command-r",
            prompt=prompt,
            max_tokens=300,
            temperature=0.7
        )

        return response.generations[0].text.strip()

    except Exception as e:
        return f"Error: {e}"


if __name__ == "__main__":
    prompt = input("Enter your prompt: ")

    print("\nQuerying Cohere...\n")

    result = query_cohere(prompt)

    print("Response:\n")
    print(result)
from dotenv import load_dotenv
load_dotenv()

import os
import base64
from groq import Groq

# Step 1: Load GROQ API key
GROQ_API_KEY = os.environ.get("GROQ_API_KEY")
if not GROQ_API_KEY:
    raise ValueError("GROQ_API_KEY is not set. Set it in your .env or environment variables.")

# Step 2: Image encoding
def encode_image(image_path):
    image_file=open(image_path,"rb")
    return base64.b64encode(image_file.read()).decode('utf-8')

# Step 3: Setup model and query


query = "tell me solution"
model = "meta-llama/llama-4-scout-17b-16e-instruct"

def analyze_image_with_query(query, model, encoded_image):
    client = Groq(api_key=GROQ_API_KEY)
    messages = [
        {
            "role": "user",
            "content": [
                {"type": "text", "text": query},
                {
                    "type": "image_url",
                    "image_url": {
                        "url": f"data:image/jpeg;base64,{encoded_image}",
                    },
                },
            ],
        }
    ]
    chat_completion = client.chat.completions.create(
        messages=messages,
        model=model
    )

    return chat_completion.choices[0].message.content

# Step 4: Run main code
if __name__ == "__main__":
    image_path = "acne.jpg"  # Make sure this file exists
    encoded_img = encode_image(image_path)
    result = analyze_image_with_query(query, model, encoded_img)
    print(result)

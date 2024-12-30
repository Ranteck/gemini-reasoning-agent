# main.py

import os
import logging
import google.generativeai as genai
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Get and validate environment variables
api_key = os.getenv("GEMINI_API_KEY")
model_name = os.getenv("MODEL")

if not api_key:
    logging.error("GEMINI_API_KEY environment variable is not set")
    raise ValueError("GEMINI_API_KEY is required")

if not model_name:
    logging.error("MODEL environment variable is not set")
    raise ValueError("MODEL is required")

logging.info(f"Using model: {model_name}")
logging.info("API key loaded successfully")

genai.configure(api_key=api_key)
model = genai.GenerativeModel(model_name)

# Get user input
topic = input("Enter a topic: ")
loops = int(input("Enter the number of loops: "))

# First Agent - low temperature for focused, consistent output
setup_prompt = f"""Here's what the user said {topic} ####
Your task is to formulate a set of detailed instructions for this topic.
Keep the instructions generic and non-specific.
Make sure to clearly & thoroughly describe HOW to best answer the user's
question, encouraging the person you are writing these instructions for to
approach the topic from many different angles."""
first_response = model.generate_content(
    setup_prompt,
    stream=True,
    generation_config=genai.types.GenerationConfig(
        temperature=0.3
    )
)

print("\nFormulating Question:")
question = ""
for chunk in first_response:
    question += chunk.text
    print(chunk.text)
print("\n" + "-" * 80)

# Second Agent - high temperature for creative reasoning
current_thoughts = question
all_thoughts = []
for i in range(loops):
    print(f"\nReasoning Loop {i+1}/{loops}:")

    reasoning_prompt = f"""HERE'S WHAT YOU NEED TO DO: #### {current_thoughts}

    Answer as if you were a 170 IQ person."""
    response = model.generate_content(
        reasoning_prompt,
        stream=True,
    )

current_thoughts = ""    
for chunk in response:
    current_thoughts += chunk.text
    print(chunk.text)
all_thoughts.append(current_thoughts)

print("\n" + "-" * 80)

# Third agent - very low temperature for consistent summarization
print("\nFinal Synthesis:")
synthesis_prompt = f"""Topic: {topic} 
Initial Framework: {question}
Reasoning Chain: {' | '.join(all_thoughts)}

IMPORTANT: Your task is to provide a clear, coherent synthesis of these insights in tow concise paragraphs.

Use simple easy-to-understand language. Write in short sentences."""

final_response = model.generate_content(
    synthesis_prompt,
    stream=True,
    generation_config=genai.types.GenerationConfig(
        temperature=0.1
    )
)
for chunk in final_response:
    print(chunk.text)
print("-" * 80)
# ai_helper.py

import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-2.0-flash")

def get_ai_response(symptoms):
    prompt = (
        "You are a helpful AI medical assistant. Based only on these symptoms, reply in 1–2 sentences with a brief suggestion of mild conditions and OTC remedies. "
        "If symptoms are serious, add a short warning.\n\n"
        f"Symptoms: {symptoms}"
    )

    response = model.generate_content(prompt)
    return response.text.strip()

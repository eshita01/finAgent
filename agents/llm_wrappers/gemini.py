# agents/llm_wrappers/gemini.py

import google.generativeai as genai
from config.env_loader import load_env

class GeminiLLM:
    def __init__(self, model_name: str = "gemini-pro"):
        self.config = load_env()
        api_key = self.config.get("GOOGLE_API_KEY")
        if not api_key:
            raise ValueError("GOOGLE_API_KEY not found in environment variables.")
        
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel(model_name)

    def generate(self, prompt: str, **kwargs) -> str:
        try:
            response = self.model.generate_content(prompt, **kwargs)
            return response.text.strip() if response.text else ""
        except Exception as e:
            print(f"[GeminiLLM] Error generating response: {e}")
            return "LLM_ERROR"

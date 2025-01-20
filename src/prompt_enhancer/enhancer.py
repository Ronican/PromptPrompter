import os
import google.generativeai as genai
from openai import OpenAI
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)

class PromptEnhancer:
    def __init__(self, openai_api_key=None, gemini_api_key=None):
        self.openai_api_key = openai_api_key or os.getenv('OPENAI_API_KEY')
        self.gemini_api_key = gemini_api_key or os.getenv('GEMINI_API_KEY')
        if not self.openai_api_key or not self.gemini_api_key:
            raise ValueError("API keys for OpenAI and Gemini must be provided.")

        genai.configure(api_key=self.gemini_api_key)
        self.client = OpenAI(api_key=self.openai_api_key)

    def enhance_prompt(self, prompt: str, model: str = "openai", openai_model: str = "gpt-4o") -> str:
        # Improve the given prompt
        improvement_prompt = f"Improve the following prompt for better clarity and detail: {prompt}. Ensure the prompt is clear, concise, and easy to understand."
        if model == "openai":
            return self._call_openai(improvement_prompt, openai_model)
        elif model == "gemini":
            return self._call_gemini(improvement_prompt)
        else:
            raise ValueError("Unsupported model. Choose 'openai' or 'gemini'.")

    def get_final_answer(self, prompt: str, model: str = "openai", openai_model: str = "gpt-4o") -> str:
        enhanced_prompt = self.enhance_prompt(prompt, model, openai_model)
        if model == "openai":
            return self._call_openai(enhanced_prompt, openai_model)
        elif model == "gemini":
            return self._call_gemini(enhanced_prompt)
        else:
            raise ValueError("Unsupported model. Choose 'openai' or 'gemini'.")

    def _call_openai(self, prompt: str, model: str = "gpt-4o") -> str:
        completion = self.client.chat.completions.create(
            model=model,
            store=True,
            messages=[
                {"role": "user", "content": prompt}
            ]
        )
        return completion.choices[0].message.content

    def _call_gemini(self, prompt: str) -> str:
        model = genai.GenerativeModel("gemini-1.5-flash")
        response = model.generate_content(prompt)
        return response.text
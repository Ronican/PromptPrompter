from prompt_enhancer import PromptEnhancer

# Initialize the PromptEnhancer with your API keys
enhancer = PromptEnhancer(openai_api_key="your_openai_api_key", gemini_api_key="your_gemini_api_key")

# Get the final answer for a given prompt using OpenAI
final_response = enhancer.get_final_answer(prompt="Explain quantum entanglement in simple terms", model="openai")
print(final_response)
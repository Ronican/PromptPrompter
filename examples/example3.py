from prompt_enhancer import PromptEnhancer

# Initialize the PromptEnhancer with your API keys
enhancer = PromptEnhancer(openai_api_key="your_openai_api_key", gemini_api_key="your_gemini_api_key")

# Get the final answer for a given prompt using OpenAI with a specific model
# Available OpenAI models: gpt-4o, gpt-4o-mini, o1, o1-mini
final_response = enhancer.get_final_answer(prompt="Write a short story about a robot", model="openai", openai_model="gpt-4o-mini")
print(final_response)
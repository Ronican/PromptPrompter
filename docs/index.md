# PromptPrompter Documentation

Welcome to the documentation for PromptPrompter, a Python package for prompt enhancement and multi-model interaction with OpenAI and Gemini.

## Getting Started

To get started with PromptPrompter, follow the installation instructions in the [README.md](../README.md) file.

## Usage

Here's an example of how to use PromptPrompter:

```python
from prompt_enhancer import PromptEnhancer

# Initialize the PromptEnhancer with your API keys
enhancer = PromptEnhancer(openai_api_key="your_openai_api_key", gemini_api_key="your_gemini_api_key")

# Get the final answer for a given prompt
final_response = enhancer.get_final_answer(prompt="Explain quantum entanglement in simple terms", model="openai")
print(final_response)
```

## API Key Management

You can set environment variables (`OPENAI_API_KEY`, `GEMINI_API_KEY`) or pass them as arguments when initializing the class or function.

## Contributing

Contributions are welcome! Please read the [CONTRIBUTING.md](../CONTRIBUTING.md) file for details on how to propose changes or submit pull requests.

## License

This project is licensed under the MIT License - see the [LICENSE](../LICENSE) file for details.
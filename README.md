# PromptPrompter

A Python package for prompt enhancement and multi-model interaction with OpenAI and Gemini.

## Installation

You can install PromptPrompter via pip:

```bash
pip install PromptPrompter
```

Or from source by cloning the repository and running:

```bash
pip install .
```

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

## Available OpenAI Models

The following OpenAI models can be used with the `PromptEnhancer` class:

- `gpt-4o`
- `gpt-4o-mini`
- `o1`
- `o1-mini`

## Contributing

Contributions are welcome! Please read the [CONTRIBUTING.md](CONTRIBUTING.md) file for details on how to propose changes or submit pull requests.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Detailed Instructions

### Setting Up the Environment

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/Ronican/PromptPrompter.git
   cd PromptPrompter
   ```

2. **Create a Virtual Environment**:
   ```bash
   python3 -m venv venv
   ```

3. **Activate the Virtual Environment**:
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```
   - On Windows:
     ```bash
     .\venv\Scripts\activate
     ```

4. **Install Dependencies**:
   ```bash
   pip install -e .
   ```

### Importing API Keys

You can set your API keys as environment variables or pass them directly when initializing the `PromptEnhancer` class.

#### Using Environment Variables

Set the environment variables in your shell:

- On macOS/Linux:
  ```bash
  export OPENAI_API_KEY="your_openai_api_key"
  export GEMINI_API_KEY="your_gemini_api_key"
  ```

- On Windows:
  ```cmd
  set OPENAI_API_KEY=your_openai_api_key
  set GEMINI_API_KEY=your_gemini_api_key
  ```

#### Passing API Keys Directly

You can pass the API keys directly when initializing the `PromptEnhancer` class:

```python
from prompt_enhancer import PromptEnhancer

enhancer = PromptEnhancer(
    openai_api_key="your_openai_api_key",
    gemini_api_key="your_gemini_api_key"
)
```

### Examples

Check out the [examples](examples) folder for detailed usage examples.
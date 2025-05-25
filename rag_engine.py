import subprocess

MODEL_PATH = "./model/mistral-7b-instruct-v0.1.Q4_K_M.gguf"
LLAMA_CLI = "./llama.cpp/build/bin/llama-cli"

def get_response(prompt: str) -> str:
    """
    Run the chatbot model with the given prompt and return the output.
    """
    try:
        result = subprocess.run(
            [LLAMA_CLI, "-m", MODEL_PATH, "-p", prompt],
            capture_output=True, text=True, timeout=120
        )
        if result.returncode != 0:
            return f"Model Error: {result.stderr.strip()}"
        lines = [l.strip() for l in result.stdout.splitlines() if l.strip()]
        return lines[-1] if lines else "Sorry, no response from the AI."
    except subprocess.TimeoutExpired:
        return "Model timed out. Please try again."
    except Exception as e:
        return f"Error: {str(e)}"
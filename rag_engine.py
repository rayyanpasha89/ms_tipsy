import subprocess

MODEL_PATH = "./model/mistral-7b-instruct-v0.1.Q4_K_M.gguf"
LLAMA_CLI = "./llama.cpp/build/bin/llama-cli"

def get_response(prompt: str) -> str:
    try:
        output = subprocess.run(
            [LLAMA_CLI, "-m", MODEL_PATH, "-p", prompt],
            capture_output=True, text=True, timeout=60
        )
        response = output.stdout.split("\n")[-5]  # crude parsing; refine later
        return response.strip()
    except Exception as e:
        return f"Error: {str(e)}"

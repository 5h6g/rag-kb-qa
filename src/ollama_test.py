import requests
import json

BASE = "http://localhost:11434"
MODEL = "qwen3:4b"

def test_native_api():
    """Ollama 原生接口"""
    r = requests.post(
        f"{BASE}/api/generate",
        json={"model": MODEL, "prompt": "你好，请简单介绍RAG"}
    )
    print("[native] status:", r.status_code)
    print("[native] raw:", r.text[:200])  

def test_openai_compat():
    """OpenAI 兼容接口 —— 以后 LangChain 用这个"""
    r = requests.post(
        f"{BASE}/v1/chat/completions",
        json={
            "model": MODEL,
            "messages": [{"role": "user", "content": "你好，请简单介绍RAG"}]
        }
    )
    print("\n[openai兼容]", r.json()["choices"][0]["message"]["content"])

if __name__ == "__main__":
    test_native_api()
    test_openai_compat()

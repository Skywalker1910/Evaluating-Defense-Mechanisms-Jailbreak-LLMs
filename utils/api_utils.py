import openai
import time
import os

def call_openai_api(model, prompt, max_tokens=300, temperature=0.7):
    openai.api_key = os.getenv("OPENAI_API_KEY")
    start_time = time.time()
    try:
        response = openai.ChatCompletion.create(
            model=model,
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt},
            ],
            max_tokens=max_tokens,
            temperature=temperature,
        )
        latency = time.time() - start_time
        reply = response.choices[0].message["content"]
        token_usage = response.usage.total_tokens
        return reply, latency, token_usage, None
    except Exception as e:
        latency = time.time() - start_time
        return str(e), latency, 0, e
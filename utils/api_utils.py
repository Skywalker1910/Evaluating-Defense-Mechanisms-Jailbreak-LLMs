import openai
import time
import os

def call_openai_api(model, prompt, max_tokens=300, temperature=0.7):
    openai.api_key = os.getenv("OPENAI_API_KEY")
    start_time = time.time()
    try:
        if model in ["gpt-4o", "o3", "o3-mini"]:
            response = openai.chat.completions.create(
                model=model,
                messages=[{"role": "user", "content": prompt}],
                max_completion_tokens=300
            )
        else:
            response = openai.ChatCompletion.create(
                model=model,
                messages=[{"role": "user", "content": prompt}],
                temperature=temperature,
                max_tokens=max_tokens
            )

        latency = time.time() - start_time
        reply = response.choices[0].message.content 
        token_usage = response.usage.total_tokens
        return reply, latency, token_usage, None
    except Exception as e:
        latency = time.time() - start_time
        return str(e), latency, 0, e

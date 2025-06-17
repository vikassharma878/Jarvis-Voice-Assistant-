# from openai import OpenAI

# client = OpenAI(
# #   base_url="https://openrouter.ai/api/v1",
#   api_key="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",
# )

# completion = client.chat.completions.create(
# #   extra_headers={
# #     "HTTP-Referer": "<YOUR_SITE_URL>", # Optional. Site URL for rankings on openrouter.ai.
# #     "X-Title": "<YOUR_SITE_NAME>", # Optional. Site title for rankings on openrouter.ai.
# #   },
#   model="deepseek/deepseek-chat-v3-0324:free",
#   messages=[
#     {"role": "system", "content": "You are a virtual assistant named jarvis skilled in general tasks like Alexa and Google Cloud"},
#     {"role": "user", "content": "what is coding"}
#   ]
# )

# print(completion.choices[0].message.content)



# ai_client.py
from openai import OpenAI

client = OpenAI(
    api_key="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",
    base_url="https://openrouter.ai/api/v1"
)

def ai_respond(prompt):
    response = client.chat.completions.create(
        model="deepseek/deepseek-chat-v3-0324:free",
        messages=[
            {"role": "system", "content": "You are Jarvis, a helpful assistant. Keep answers short."},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content.strip()


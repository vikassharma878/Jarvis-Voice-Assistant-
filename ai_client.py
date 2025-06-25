# from openai import OpenAI

# client = OpenAI(
# #   base_url="https://openrouter.ai/api/v1",
#   api_key="USE-YOUR-APIKEY",
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
    api_key="USE-YOUR-APIKEY",
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


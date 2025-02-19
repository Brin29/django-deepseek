from django.shortcuts import render, redirect
from django.http import JsonResponse
from openai import OpenAI
from .models import Chat

client = OpenAI(api_key="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", base_url="https://openrouter.ai/api/v1")

def ask_openai(message):
    response = client.chat.completions.create(
        model="deepseek/deepseek-r1:free",
        messages=[
        {
            "role": "user",
            "content": message
        }
        ]
    )

    answer = response.choices[0].message.content.strip()
    print(answer)
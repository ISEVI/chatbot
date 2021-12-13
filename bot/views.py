import json

from django.shortcuts import render
from .forms import UserForm
import requests


def start_chatbot(request):
    template = 'bot/bot.html'
    #context = {
    #    'content': text
    #}

    return render(request, template)


def start_devopchatbot(request):
    template = 'bot/devop.html'
    submitbutton = request.POST.get("submit")

    question = ""
    content = ""

    form = UserForm(request.POST or None)
    if form.is_valid():
        question = form.cleaned_data.get("question")
        print(question)
        with open('static/note.txt', 'r', encoding='utf-8') as note:
            note = note.read()
            print(note)
        post_data = {
                      "context_raw": [
                        note,
                      ],
                      "question_raw": [
                        question,
                      ]
                    }
        response = requests.post("http://127.0.0.1:5005/model", data=json.dumps(post_data))
        content = response.json()
        content = content[0][0]

    context = {
        'content': content,
        'question': question
    }

    return render(request, template, context)


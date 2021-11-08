from django.shortcuts import render

def start_chatbot(request):
    template = 'bot/bot.html'
    #context = {
    #    'content': text
    #}

    return render(request, template)


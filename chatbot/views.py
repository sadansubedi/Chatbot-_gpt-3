from django.shortcuts import render
from django.http import JsonResponse
import openai


openai_api_key ='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' 

openai.api_key =openai_api_key


def ask_openai(message):
    reponse = openai.Completion.create(
        model ='text-davinci-003',
        prompt = message,
        max_tokens =150,
        n=1,
        stop = None,
        temperature = 0.7,
    )
    print(reponse)
    answer = reponse.choices[0].text.strip()
    return answer


'''
# gpt-4 is not available this time ok 

def ask_openai(message):
    response = openai.ChatCompletion.create(
        model = "gpt-4",
        messages=[
            {"role": "system", "content": "You are an helpful assistant."},
            {"role": "user", "content": message},
        ]
    )
    
    answer = response.choices[0].message.content.strip()
    return answer

'''

def Chatbot(request):
    if request.method == 'POST':
        messages = request.POST.get('messages')
        response = ask_openai(messages)   
        return JsonResponse({'messages':messages,'response':response})
    return render(request,'chatbot/chatbot.html')

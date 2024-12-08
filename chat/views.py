from django.http import JsonResponse
from django.shortcuts import render, redirect
from .models import Conversation, Messages
from .ai_message_db import ai_message_db
from django.contrib.auth.decorators import login_required
# Create your views here.


@login_required(login_url="signin")
def chat(request):
    if request.method == "POST":
        input_message = request.POST.get("user-input")
        if not input_message:
            return JsonResponse({"error": "No input provided."}, status=400)

        conversation = Conversation.objects.create(
            user=request.user, name=input_message[0:14])
        message_data = {"message": input_message,
                        "ai_message": ai_message_db.get(input_message, "I'm sorry, I didn't understand that."),
                        "conversation": conversation
                        }
        Messages.objects.create(**message_data)
        return redirect('chat_by_id', conversationId=conversation.id)

    conversations = Conversation.objects.filter(
        user=request.user).order_by('-created_at')
    return render(request, 'chat.html', {'conversations': conversations})


@login_required(login_url="signin")
def chat_by_coversationId(request, conversationId):
    if not request.user.is_authenticated:
        return redirect('/accounts/signin/')
    if request.method == "POST":
        input_message = request.POST.get("user-input")
        if not input_message:
            return JsonResponse({"error": "No input provided."}, status=400)
        conversation = Conversation.objects.get(id=conversationId)
        message_data = {"message": input_message,
                        "ai_message": ai_message_db.get(input_message, "I'm sorry, I didn't understand that."),
                        "conversation": conversation
                        }
        message = Messages.objects.create(**message_data)
        response_data = {
            "id": message.id,
            "message": message.message,
            "ai_message": message.ai_message,
            "conversation_id": message.conversation.id,
            "user": {
                "id": message.conversation.user.id,
                "username": message.conversation.user.username,
                "gmail": message.conversation.user.email,
            }
        }
        return JsonResponse(response_data, safe=False)

    messages = Messages.objects.filter(conversation=conversationId)
    conversations = Conversation.objects.filter(
        user=request.user).order_by('-created_at')
    pathlist = request.path.split("/")
    endpoint = int(pathlist[2])
    print(f'endpoint is {endpoint}')
    return render(request, 'chatById.html', {'conversations': conversations, "messages": messages, 'endpoint': endpoint})

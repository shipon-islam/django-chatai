from django.http import JsonResponse
from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from .models import Conversation, Messages
from .forms import RegistrationForm
from django.contrib import messages
from .ai_message_db import ai_message_db

# Create your views here.


def home(request):
    if not request.user.is_authenticated:
        return redirect('login/')
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
        return redirect(f'chat/{conversation.id}/')

    conversations = Conversation.objects.filter(
        user=request.user).order_by('-created_at')
    return render(request, 'home.html', {'conversations': conversations})


def chat_by_coversationId(request, conversationId):
    if not request.user.is_authenticated:
        return redirect('login/')
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
    endpoint = int(request.path.split("/")[2])
    return render(request, 'chat.html', {'conversations': conversations, "messages": messages, 'endpoint': endpoint})


def register_user(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()  # Save the user to the database
            login(request, user)  # Log the user in after registration
            return redirect("/")  # Redirect to the homepage or dashboard
    else:
        form = RegistrationForm()

    return render(request, 'register.html', {"form": form})


def login_user(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        print(request.POST)
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("/")
        else:
            messages.error(request, 'Invalid username or password')
    return render(request, 'login.html')


def logout_user(request):
    logout(request)
    return redirect("/login")

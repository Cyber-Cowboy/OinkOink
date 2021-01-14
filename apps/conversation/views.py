from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Conversation, ConversationMessage
from apps.notification.utilities import create_notification

@login_required
def conversations(request):
	return render(request, 'conversation/conversations.html', {'conversations':request.user.conversations.all()})

@login_required
def conversation(request, user_id):
	conversations = Conversation.objects.filter(users__in=[request.user.id])
	conversations = conversations.filter(users__in=[user_id])
	if conversations.count() == 1:
		users_conversation = conversations[0]
	else:
		recipient = User.objects.get(pk=user_id)
		users_conversation = Conversation.objects.create()
		users_conversation.users.add(request.user)
		users_conversation.users.add(recipient)
		users_conversation.save()
	context = {'conversation':users_conversation}
	return render(request, 'conversation/conversation.html', context)
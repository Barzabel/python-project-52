from django.shortcuts import render
from django.views import View
from django.contrib import messages
from django.utils.translation import gettext_lazy as _


class IndexView(View):
    def get(self, request, *args, **kwargs):
        messages_ = messages.get_messages(request)

        return render(
            request,
            'index.html',
            context={
                'messages': messages_
            }
        )

# create users
# login
# get all users

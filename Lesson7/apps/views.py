from time import time

from django.contrib import messages
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
from django.http import JsonResponse
from django.shortcuts import render
from django.template.loader import render_to_string
from django.urls import reverse_lazy
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.views import View
from django.views.generic import TemplateView, FormView

from .forms import UserRegisterForm
from django.contrib.auth import authenticate, get_user_model, login
from django.shortcuts import redirect, render


from apps.tasks import send_to_email
from .models import User
from .tokens import account_activation_token


class HomeTemplateView(TemplateView):
    template_name = ('apps/home.html')


class SendEmailView(View):
    def get(self, requests):
        email = requests.GET['email']
        msg = requests.GET['msg']
        start = time()
        send_to_email.delay(email, msg)
        end = time()
        return JsonResponse({"status" : "Yuborildi" , "time" : int(end-start) , "email" : email})



def verify_email_confirm(request, uidb64, token):
    uid = force_str(urlsafe_base64_decode(uidb64))
    user = User.objects.get(pk=uid)

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        messages.success(request, 'Your email has been verified.')
        return redirect('login')
    else:
        messages.warning(request, 'The link is invalid.')
    return render(request, 'login')
class RegisterFormView(FormView):
    form_class = UserRegisterForm
    success_url = reverse_lazy('register')
    template_name = 'apps/auth/register.html'


    def form_valid(self, form):
        user = form.save(commit=False)
        password = form.cleaned_data.get('password')
        user.is_active = False
        user.set_password(password)
        user.save()
        send_to_email.delay(user.email, )
        return super().form_valid(form)


def verify_email(request):
    if request.method == "POST":
        if request.user.is_active != True:
            current_site = get_current_site(request)
            user = request.user
            email = request.user.email
            subject = "Verify Email"
            message = render_to_string('apps/auth/verify_email_message.html', {
                'request': request,
                'user': user,
                'domain': current_site.domain,
                'uid':urlsafe_base64_encode(force_bytes(user.pk)),
                'token':account_activation_token.make_token(user),
            })
            send_to_email(subject , email, message)
            return redirect('verify-email-done')
        else:
            return redirect('signup')
    return render(request, 'apps/auth/login.html')
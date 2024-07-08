from django.contrib.auth.decorators import login_required
from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth.views import LogoutView, LoginView
from django.urls import reverse_lazy, reverse
from .forms import RegistrationForm
from django.views.generic import CreateView, RedirectView, DeleteView, DetailView
from .models import BlogUser
from django.contrib.auth import logout
from django.http import HttpResponseRedirect, JsonResponse
from django.urls import reverse
from django.views import View
from rest_framework.authtoken.models import Token


# Create your views here.
class UserLoginView(LoginView):
    template_name = 'usersapp/login.html'

# class UserLogoutView(LogoutView):
#     def dispatch(self, request, *args, **kwargs):
#         # Обработка GET-запросов
#         if request.method == 'GET':
#             return self.get(request, *args, **kwargs)
#         # Обработка POST-запросов
#         return super().dispatch(request, *args, **kwargs)

class UserLogoutView(LogoutView):
    next_page = reverse_lazy('index')

class CustomLogoutView(RedirectView):
    url = reverse_lazy('usersapp:login')  # Перенаправляем на страницу входа после выхода
    permanent = False

    def get(self, request, *args, **kwargs):
        logout(request)
        return super().get(request, *args, **kwargs)


# class UserLogoutView(LogoutView):
#     def get(self, request, *args, **kwargs):
#         response = super().get(request, *args, **kwargs)
#         return response


class UserCreateView(CreateView):
    model = BlogUser
    template_name = 'usersapp/register.html'
    form_class = RegistrationForm
    success_url = reverse_lazy('users:login')

class UserDetailView(DeleteView):
    template_name = 'usersapp/profile.html'
    model = BlogUser

# def update_token(request):
#     user = request.user
#     # если уже есть
#     if user.auth_token:
#         # обновить ?
#         user.auth_token.delete()
#         Token.objects.create(user=user)
#     else:
#         # создать
#         Token.objects.create(user=user)
#     return HttpResponseRedirect(reverse('user:profile', kwargs={'pk': user.pk}))

@login_required
def update_token(request):
    user = request.user
    try:
        token = user.auth_token  # Попытка получить токен пользователя
        token.delete()  # Если токен существует, удаляем его
    except Token.DoesNotExist:
        pass  # Если токен не существует, ничего не делаем

    # Создаем новый токен для текущего пользователя
    Token.objects.create(user=user)

    # После обновления токена перенаправляем пользователя на страницу профиля
    return HttpResponseRedirect(reverse('usersapp:profile', kwargs={'pk': user.pk}))

@login_required
def update_token_ajax(request):
    user = request.user
    try:
        token = user.auth_token  # Попытка получить токен пользователя
        token.delete()  # Если токен существует, удаляем его
    except Token.DoesNotExist:
        pass  # Если токен не существует, ничего не делаем

    # Создаем новый токен для текущего пользователя
    new_token = Token.objects.create(user=user)

    # После обновления токена возвращаем новый токен в формате JSON
    return JsonResponse({'key': new_token.key})
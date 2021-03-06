from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse


def sign_up(request):
    data = dict()
    if request.method == 'GET':
        data['title'] = 'Регистрация'
        return render(request, 'account/sign_up.html', context=data)
    elif request.method == 'POST':
        # 1 izvlechenie dannih iz massiva iz slovarya POST:
        login_x = request.POST.get('login')
        pass1_x = request.POST.get('pass1')
        pass2_x = request.POST.get('pass2')
        email_x = request.POST.get('email')
        # 2 tehnicheskaya proverka
        data['login'] = login_x
        data['pass1'] = pass1_x
        data['pass2'] = pass2_x
        data['email'] = email_x

        # 3- validazia na storone servera:

        if pass1_x != pass2_x:
            data['color'] = 'red'
            data['report'] = 'Введеные пароли не совпадают'
        elif login_x == '...':
            # Ostalnie proverki
            pass
        else:
            # registrazia
            user = User.objects.create_user(login_x, email_x, pass1_x)
            user.save()
            if user is None:
                data['color'] = 'red'
                data['report'] = 'В регистрации отказано'
            else:
                data['color'] = 'cadetblue'
                data['report'] = 'Регистрация завершена'





        # fin - otparvka otcheta
        data['title'] = 'Отчет о регистрации'

        return render(request, 'account/report.html', context=data)


def sign_in(request):
    data = dict()
    if request.method == 'GET':
        data['title'] = 'Авторизация'
        return render(request, 'account/sign_in.html', context=data)
    elif request.method == 'POST':
        # 1 Poluchenie dannih iz formi avtorizazii:
        login_x = request.POST.get('login')
        pass1_x = request.POST.get('pass1')

        # 2 Proverka podlinnosti znachenii login/parol:
        user = authenticate(request, username=login_x, password=pass1_x)
        if user is None:
            data['color'] = 'red'
            data['report'] = 'Пользователь не найден'
            data['title'] = 'Отчет об авторизации'
            return render(request, 'account/report.html', context=data)
        else:
            login(request, user)
            return redirect('/home')


def sign_out(request):
    logout(request)
    return redirect('/home')


def profile(request):
    data = dict()
    data['title'] = 'Профиль'
    return render(request, 'account/profile.html', context=data)






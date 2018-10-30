from django.shortcuts import render, redirect, reverse
from django.contrib.auth import login, logout

from .models import MyUserModel
# Create your views here.


def user_login(request):

    if request.method == 'GET':

        return render(request, 'login.html')

    elif request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')

        try:

            user = MyUserModel.objects.get(username=username)

            # 验证密码是否正确
            if user.check_password(password):

                # 登陆成功
                login(request, user)

                return redirect(reverse('subject_list'))

            else:
                return render(request, 'login.html', {'errmsg': '帐户或密码错误！'})

        except Exception as e:

            return render(request, 'login.html', {'errmsg': '账户不存在！'})


def user_logout(request):

    logout(request)

    return redirect(reverse('login'))
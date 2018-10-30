import datetime
import time

from django.shortcuts import render, HttpResponse, redirect
# make_password() 对明文密码进行加密的函数
from django.contrib.auth.hashers import make_password
# Q 查询多条件 或 关系
from django.db.models import Q
# login() 登陆函数， 会将登陆状态存储到session表中
from django.contrib.auth import login, logout
# login_required 装饰器 访问某个装饰的路由函数时，必须是登陆状态，否则跳转到指定的登陆路由
from django.contrib.auth.views import login_required

from .models import UserProfile, EmailRecard
from .email_send import mail_send, random_code
from .forms import RegisterForm, ForgetForm, ModifyForm, LoginForm
# Create your views here.
'''
注册业务逻辑：

    客户端通过post请求发送数据到服务端
    服务端取出数据
    验证数据合法性(是否是邮箱地址、两次密码是否一致，密码是否包含特殊字符、密码长度是否符合要求)
    验证账户是否被注册
    
    创建用户模型对象
    设置用户对象属性，例如：email、username、password(加密)、is_active等等.....
    保存数据到数据库，发送注册成功后的激活邮件
'''


def user_register(request):
    """
    注册用户
    :param request:
    :return:
    """
    if request.method == 'GET':

        # 创建form表单对象目的，为了在页面中显示验证码
        form = RegisterForm()
        return render(request, 'register.html', {'form': form})

    elif request.method == 'POST':

        # 根据request.POST中的参数，创建form表单对象
        form = RegisterForm(request.POST)
        # is_valid() 判断传递的参数是否符合验证规则
        result = form.is_valid()
        if result:
            # 取出email、password
            email = form.cleaned_data['email']
            if UserProfile.objects.filter(email=email):
                return render(request, 'register.html', {'form': form, 'email_error': '该邮箱已注册！'})
            # 取出已验证数据
            pwd1 = form.cleaned_data['pwd1']
            pwd2 = form.cleaned_data['pwd2']
            if pwd1 != pwd2:

                return render(request, 'register.html', {'form': form, 'pwd_error':'两次密码不一致！'})

            user = UserProfile()
            user.email = email
            user.username = random_code(6)
            user.is_active = 0
            user.password = make_password(pwd1)
            # 邮件发送成功表示注册成功
            if mail_send(email):
                user.save()
                return render(request, 'active.html', {'msg': f'注册成功，激活邮件已发送至您的{email}邮箱中，请注意查收！'})
            else:

                return render(request, 'register.html', {'form': form, 'pwd_error': '注册失败，请稍后重试！'})
        else:

            return render(request, 'register.html', {'form': form})

        # 判断邮箱是否被注册
        # if UserProfile.objects.filter(email=email):
        #     content['email_error'] = '该邮箱以被注册！'
        #     # 邮箱被注册
        #     return render(request, 'register.html', content)
        #
        # # 判断两次密码是否一致
        # if pwd1 != pwd2:
        #     # 两次密码不一致
        #     content['pwd_error'] = '两次密码不一致！'
        #     return render(request, 'register.html', content)
        #
        # # 注册账户
        # user = UserProfile()
        # user.email = email
        # # 对密码进行加密的函数
        # user.password = make_password(pwd1)
        # print(user.password)
        # # 设置用户名
        # user.username = email
        # # 该账户是否是激活状态
        # user.is_active = 0
        #
        # user.save()
        # content = {}
        # # 向注册邮箱发送激活邮件
        # if mail_send(to_email=email):
        #
        #     content['msg'] = f'注册成功，激活邮件已发送至您的{email}邮箱，请登陆查看！'
        # else:
        #     content['msg'] = f'注册成功，激活邮件发送失败，点击重新发送！'

        return render(request, 'active.html')


def user_active(request, code):
    """
    发送激活邮件，设置邮件code、email、发送时间、过期时间、邮件状态、邮件类型

    点击激活链接，访问当前路由，取出传递的code参数

    根据code参数，取出邮件记录

    判断邮件使用状态、判断邮件是否过期

    获取邮箱地址，根据邮箱获取用户

    更改用户激活状态

    保存数据

    更改邮件使用状态

    保存数据

    :param request:
    :param code:
    :return:
    """
    if request.method == 'GET':

        # 1.根据code找到这条邮件记录
        email_recard = EmailRecard.objects.filter(code=code)
        if email_recard:
            # 判断邮件是否已使用
            email_recard = email_recard[0]
            if email_recard.email_status:

                return HttpResponse('该激活链接已失效！')
            # 判断邮件是否过期，比较当前时间和过期时间
            # 将两个时间都转换为时间戳
            today = datetime.datetime.now()
            exprie_time = email_recard.expire_time
            # mktime() 将时间元组转换为时间戳
            today_time = time.mktime(today.timetuple())
            exprie_time = time.mktime(exprie_time.timetuple())
            # 判断是否过期
            if today_time > exprie_time:
                email_recard.delete()
                return HttpResponse('该链接已过期，点击重新发送激活邮件！')

            # 2.获取code对应的email
            email = email_recard.email
            # 3.根据email找到用户
            user = UserProfile.objects.get(email=email)
            # 4.激活账户
            user.is_active = 1
            # 5.保存修改
            user.save()
            # 修改为已使用
            email_recard.email_status = 1
            email_recard.save()
            return HttpResponse('<a href="http://127.0.0.1:8000/user/login"><strong>账户激活成功，点击前往登陆</strong></a>')

        else:
            # code不存在
            return HttpResponse(status=404)


def user_forget(request):
    """
    1.点击忘记密码，进入找回密码页面，加载验证码
    2.输入要修改的注册邮箱地址，输入验证码，验证表单数据是否合法
    3.根据提交的email，验证账户是否存在，若存在继续执行，不存在返回错误信息
    4.给该邮箱地址，发送找回密码邮件
    :param request:
    :return:
    """
    if request.method == 'GET':

        forms = ForgetForm()

        return render(request, 'forget.html', {'forms': forms})
    elif request.method == 'POST':

        forms = ForgetForm(request.POST)

        if forms.is_valid():
            # 取出找回密码的邮箱地址
            email = forms.cleaned_data['email']
            # 判断该账户是否存在
            if UserProfile.objects.filter(email=email):

                # 用户存在，向用户邮箱发送找回密码邮件

                if mail_send(email, type='forget'):

                    return render(request, 'active.html', {'msg': f'修改密码的邮件已发送至您的{email}邮箱，请注意接收！'})
                else:
                    return render(request, 'forget.html', {
                        'forms': forms,
                        'errmsg': '发送失败，请稍后重试'
                    })

            else:

                return render(request, 'forget.html', {
                    'forms': forms,
                    'errmsg': '该用户不存在！'
                })
        else:

            return render(request, 'forget.html', {'forms': forms})


def user_modify(request, code):
    """
    GET请求：
    1.点击找回密码邮件中的链接
    2.根据链接中的code参数，找email_recard,若没有返回404
    3.判断邮件状态，是否过期
    4.返回修改页面，将code和email传递到模板中，隐藏输入框

    POST请求：
    1.根据post参数，验证表单数据是否合法，不合法返回错误信息
    2.验证code和提交email是否是同一条数据，匹配失败，返回错误信息
    3.判断两次密码是否一致，不一致返回错误信息
    4.根据email找到user用户，修改user.password ，保存数据
    5.修改邮件使用状态，保存邮件数据
    6.返回修改成功信息

    :param request:
    :param code:
    :return:
    """
    if request.method == 'GET':

        # 查找邮件
        email_recard = EmailRecard.objects.filter(code=code)

        if email_recard:
            # 验证邮件状态、邮件是否过期
            email_recard = email_recard[0]
            if email_recard.email_status:

                return render(request, 'active.html', {'msg': '该链接已失效！'})
            # 获取当前时间时间戳
            today_t = time.mktime(datetime.datetime.now().timetuple())
            # 获取过期时间时间戳
            exprie_t = time.mktime(email_recard.expire_time.timetuple())

            if today_t > exprie_t:

                return render(request, 'active.html', {'msg': '该链接已过期，点击重新发送！'})

            # 取出邮件对应的邮箱
            email = email_recard.email

            return render(request, 'modify.html', {'forms': {'email': {'value': email}, 'code': {'value': code}}})
        else:
            return HttpResponse(status=404)

    elif request.method == 'POST':
        # 根据code找用户邮箱
        # email和code值一定要对应，保证要修改的用户是邮件指定的用户
        forms = ModifyForm(request.POST)

        if forms.is_valid():
            pwd1 = forms.cleaned_data['pwd1']
            pwd2 = forms.cleaned_data['pwd2']
            if pwd1 == pwd2:

                try:
                    email = request.POST['email']
                    email_recard = EmailRecard.objects.get(code=code, email=email)
                    if email_recard:
                        user = UserProfile.objects.get(email=email)
                        user.password = make_password(pwd1)
                        user.save()
                        # 更改邮件使用状态
                        email_recard.email_status = 1
                        email_recard.save()

                except Exception as e:

                    return render(request, 'modify.html', {'forms': forms, 'errmsg': '数据不合法，你懂的？'})
                else:

                    return render(request, 'active.html', {'msg': '<a href="http://127.0.0.1:8000/user/login"><strong>修改成功,点击前往登录</a></strong>'})


            else:
                return render(request, 'modify.html', {'forms': forms, 'errmsg': '两次密码不一致！'})
        else:
            return render(request, 'modify.html', {'forms': forms})


def user_login(request):

    if request.method == 'GET':
        forms = LoginForm()

        return render(request, 'login.html', {'forms': forms})

    elif request.method == 'POST':

        # 验证form表单数据
        forms = LoginForm(request.POST)

        if forms.is_valid():
            username = forms.cleaned_data['username']
            password = forms.cleaned_data['password']
            try:
                # 获取用户，通过username或者email查找用户是否存在
                user = UserProfile.objects.get(Q(username=username)|Q(email=username))

                # 判断密码是否正确
                # check_password() 检测用户密码是否正确
                if user.check_password(password):
                    # 登陆成功
                    login(request, user)
                    # render() 不会改变路由地址
                    # return render(request, 'index.html')
                    # 重定向，改变当前url路由地址
                    return redirect('/')
                else:
                    return render(request, 'login.html', {'forms': forms, 'errmsg': '帐号或密码错误！'})

            except Exception as e:

                return render(request, 'login.html', {'forms': forms, 'errmsg': '用户不存在！'})
        else:

            return render(request, 'login.html', {'forms': forms})


def user_logout(request):
    # 退出登陆
    logout(request)

    return redirect('/')


# 装饰器
@login_required
def user_center(request):
    """
    必须要求用户登录后才能访问
    :param request:
    :return:
    """
    return HttpResponse('个人中心需要登陆后才能访问到，你已经登陆了')


    # 判断请求中携带的user是否已经登陆
    # if request.user.is_authenticated():
    #
    #     return HttpResponse('个人中心需要登陆后才能访问到，你已经登陆了')
    #
    # else:
    #     # 没有登陆，重定向到登陆界面
    #     return redirect('/user/login')






# -*- coding: utf-8 -*-
__author__ = 'wj'
__date__ = '2018/10/18 14:34'
import random
import datetime
from django.core.mail import send_mail

from UserProject import settings
from .models import EmailRecard


def random_code(length=16):
    """随机产生验证码函数"""
    string = 'QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm1234567890'
    # 随机生成验证码
    code = ''.join([string[random.randint(0, len(string)-1)] for x in range(length)])

    return code


def mail_send(to_email, type='register'):
    """
    :param to_email: 接收邮件的email地址
    :param type: 邮件类型
                register 注册类型邮件
    :return:True 发送成功   False 发送失败
    """

    email_recard = EmailRecard()
    # 验证码
    email_recard.code = random_code()
    email_recard.email = to_email
    email_recard.email_type = type
    # 过期时间  获取7天之后的时间
    email_recard.expire_time = datetime.datetime.now() + datetime.timedelta(days=7)

    if type == 'register':
        message = f'注册成功，点击<a href="http://127.0.0.1:8000/user/active/{email_recard.code}"><strong>http://127.0.0.1:8000/user/active/{email_recard.code}</strong></a>激活账户！'
        subject = '智游论坛注册邮件'

    else:
        # 找回密码邮件
        message = f'找回密码邮件，点击链接<a href="http://127.0.0.1:8000/user/modify/{email_recard.code}"><strong>http://127.0.0.1:8000/user/modify/{email_recard.code}</strong></a>修改您的密码!'
        subject = '智游论坛找回密码'

    try:
        result = send_mail(subject, message, settings.EMAIL_HOST_USER, [to_email], html_message=message)
        if result == 1:
            # 保存数据到数据库
            email_recard.save()
            return True
        else:

            return False
    except Exception as e:
        print(e)
        return False

#
# if __name__ == '__main__':
#
#     # 获取7天之后的时间
#     print(datetime.datetime.now())
#     print(datetime.timedelta(days=7))
#     print(datetime.datetime.now()+ datetime.timedelta(days=7))






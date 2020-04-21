"""
第三方配置
"""

HY_SMS_URL = 'https://106.ihuyi.com/webservice/sms.php?method=Submit'
HY_SMS_PARAMS = {
    'account': 'C91565239',
    'password': 'facb86fcc3c10c3b98366411a7663b42',
    'content': '您的验证码是：%s。请不要把验证码泄露给其他人。',
    'mobile': None,
    'format': 'json',
}


# =========================云之讯=============================
# HY_SMS_URL = 'https://open.ucpaas.com/ol/sms/{function}'
# HY_SMS_PARAMS = {
#     'appid': 'cfdbb259caa84cc8ab1377814f92f5a0',
#     'sid': '08ec28e7eb133affc35bd9e145e60248',
#     'token': '336b4f61a4e3dac5599480895e303cf1',
#     'templateid': '539606',
#     'param': '【云之讯】您的验证码是：%s.请不要把验证码泄露给其他人【自用测试】',
#     'mobile': None,
#     'format': 'json',
# }
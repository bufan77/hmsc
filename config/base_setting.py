SERVER_PORT = 9000
SQLALCHEMY_DATABASE_URI = 'mysql://root:root@127.0.0.1/hmsc_db?charset=utf8'
SQLALCHEMY_TRACK_MODIFICATIONS = False

#Cookie
AUTH_COOKIE_NAME = "hmsc_1901C"

#设置拦截器忽略规则
IGNORE_URLS = [
    "^/user/login"
]
IGNORECHECK_LOGIN_URLS = [
    "^/static",
    "^favicon.ico"
]
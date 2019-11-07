HOST_PORT = 8999
DEBUG = True

AUTH_COOKIE_NAME = "mooc_food"




SQLALCHEMY_DATABASE_URI = "mysql://root:123456@47.93.232.114/test"
SQLALCHEMY_TRACK_MODIFICATIONS = False


PAGE_SIZE = 50
PAGE_DISPLAY = 10

STATUS_MAPPING = {
    "1":"正常",
    "0":"已删除"
}



PAY_STATUS_MAPPING = {
    "1":"已支付",
    "-8":"待支付",
    "0":"已关闭"
}


UPLOAD = {
    'ext':[ 'jpg','gif','bmp','jpeg','png' ],
    'prefix_path':'/web/static/upload/',
    'prefix_url':'/static/upload/'
}


APP = {
    'domain':'http://192.168.0.119:8999'
}
from utils import result
from utils.jwts import parse_payload


def check_login(func):
    """定义装饰器"""

    # 登录鉴权检测
    def wrapper(request, *args, **kwargs):
        # print("装
        # 登录检测
        # 自定义忽略URL数组
        ignoreURL = ['/category/list', '/user/register', '/user/login', '/user/logout', '/product/pages',
                     '/product/:productId']
        if request.path not in ignoreURL:
            # 从请求头中获取token值
            access_token = request.headers['Authorization']
            # 字符串替换
            access_token = access_token.replace('Bearer ', "")
            # JWT解密
            result = parse_payload(access_token)
            # 结果标识
            code = result['code']
            if code != 0:
                return R.failed(code=401, msg=result['msg'])
            request.jwt_user = result['data']
        # 一切正常，返回该返回的
        return func(request, *args, **kwargs)

    # 返回对象
    return wrapper

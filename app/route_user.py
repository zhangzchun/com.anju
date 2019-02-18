

# 用户路由
from flask import Blueprint,request
# 导入user_service模块
from app.service.user_service import *
from app.utils.my_token import checkLogin

import json

# 用参数name和import_name初始化
# user是模块的名称
user = Blueprint('user',__name__)

# restful api

# 注册页面
@user.route('/regist/',methods=['POST'])
def regist():
    # 判断前端数据
    if request.is_json and request.get_json():
        u = request.get_json()

        # result为添加用户的结果
        result = addUser(u)
        return result
    else:
        return json.dumps({"status_code": "40005", "status_text": "数据格式不合法"})


# 登录页面
@user.route('/login/',methods=['POST'])
def login():
    if request.is_json and request.get_json():
        u = request.get_json()

        # result为查找用户的结果
        result = getUser(u)
        return result
    else:
        return json.dumps({"status_code": "40005", "status_text": "数据格式不合法"})


# 检查token是否过期
@user.route('/checkToken/',methods=['GET'])
@checkLogin(request)
def checkToken():
    return json.dumps({"status_code":"10003","status_text":"登录成功"})

# 修改用户信息页面




# 修改密码页面




# 用户预约信息页面




# 用户收藏信息页面




# 用户日记信息页面




# 用户房屋信息页面


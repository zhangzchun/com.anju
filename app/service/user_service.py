
#用户接口
import app.dao.user_dao as userDao
# 导入json
import json
# 导入加密模块
from werkzeug.security import generate_password_hash,check_password_hash

from flask import make_response
# 导入token
from app.utils.my_token import createToken


# 注册用户接口
def addUser(user):
    if user.get('telephone') and user.get('nickname') and user.get('password'):

        # 密码加密
        pf = generate_password_hash(user['password'], method='pbkdf2:sha1:1001', salt_length=8)
        user['password'] = pf
        # rr是注册用户的结果
        rr = userDao.addUser(user)
        if rr:
            if rr==-1:
                return json.dumps({"status_code":"10002","status_text":"用户已经存在"})
            else:
                # 构建token
                token = createToken(rr['id'])

                response = make_response()
                response.data = json.dumps({"status_code":"10001","status_text":"注册成功", "token": token})
                response.status_code = 200
                return response
                # return json.dumps({"status_code":"10001","status_text":"注册成功"})
        else:
            return json.dumps({"status_code":"40004","status_text":"系统错误"})

    else:
        return json.dumps({"status_code": "40005", "status_text": "数据格式不合法"})




# 登录用户接口
def getUser(user):
    res_user = userDao.getUserByTel(user['telephone'])
    if res_user:
        if res_user == -1:
            return json.dumps({"status_code": "10004", "status_text": "该用户不存在"})
        else:
            # 验证密码是否相同
            if (check_password_hash(res_user['password'], user['password'])):
                # 构建token
                token = createToken(res_user['id'])

                response = make_response()
                response.data = json.dumps({"status_code": "10003", "status_text": "登录成功", "token": token})
                response.status_code = 200
                return response
            else:
                return json.dumps({"status_code": "10005", "status_text": "密码错误"})
    else:
        return json.dumps({"status_code": "40004", "status_text": "系统错误"})



# 修改密码接口
def updatePassword():

    pass
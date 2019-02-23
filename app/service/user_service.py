
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
                response.data = json.dumps({"status_code":"10001","status_text":"注册成功",
                                            "token": token,"user_id":rr['id'],"nickname":rr['nickname']})
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
                response.data = json.dumps({"status_code": "10003", "status_text": "登录成功",
                                            "token": token,"user_id":res_user['id'],"nickname":res_user['nickname']})
                response.status_code = 200
                return response
            else:
                return json.dumps({"status_code": "10005", "status_text": "密码错误"})
    else:
        return json.dumps({"status_code": "40004", "status_text": "系统错误"})



# 修改密码接口
def updatePassword():

    pass



# 房屋信息接口
def getHouseList(user):
    res=userDao.getHouseList(user["user_id"])

    if res:
        if res == -1:
            return json.dumps({"status_code":"10008","status_text":"未找到数据"})
        else:
            return json.dumps({"status_code": "10009", "status_text": "找到数据", "content": res})
    else:
        return json.dumps({"status_code": "40004", "status_text": "系统错误"})



# 增加预约接口
def addAppointment(appoint):
    res=userDao.addAppointment(appoint)

    if res:
        if res == -1:
            return json.dumps({"status_code":"10021","status_text":"预约失败"})
        else:
            return json.dumps({"status_code":"10020","status_text":"预约成功", "content": res})
    else:
        return json.dumps({"status_code": "40004", "status_text": "系统错误"})


# 获取预约接口
def getAppointment(user_id):
    res=userDao.getAppointment(user_id)
    if res:
        if res == -1:
            return json.dumps({"status_code":"10008","status_text":"未找到数据"})
        else:
            return json.dumps({"status_code":"10009","status_text":"找到数据", "content": res})
    else:
        return json.dumps({"status_code": "40004", "status_text": "系统错误"})


# 取消预约接口
def subAppointment(id):
    res=userDao.subAppointment(id)
    if res:
        if res == -1:
            return json.dumps({"status_code":"10021","status_text":"取消预约失败"})
        else:
            return json.dumps({"status_code":"10020","status_text":"取消预约成功", "content": res})
    else:
        return json.dumps({"status_code": "40004", "status_text": "系统错误"})



# 修改房屋状态接口
def updateHouse():
    res=userDao.updateHouse()
    pass
    # 提醒
    # userDao.updateHouse()



# 用户收藏接口
def getCollectDetail(collect):
    res=userDao.getCollectDetail(collect)

    if res:
        if res == -1:
            return json.dumps({"status_code":"10008","status_text":"未找到数据"})
        else:
            return json.dumps({"status_code": "10009", "status_text": "找到数据", "content": res})
    else:
        return json.dumps({"status_code": "40004", "status_text": "系统错误"})





# 增加收藏接口
def addCollect(collect):

    res=userDao.addCollect(collect)
    print(res)

    if res:
        if res == -1:
            return json.dumps({"status_code":"10031","status_text":"收藏失败",})
        else:
            return json.dumps({"status_code":"10030","status_text":"收藏成功", "content": res})
    else:
        return json.dumps({"status_code": "40004", "status_text": "系统错误"})

    # 提醒
    # userDao.addCollect()


# 取消收藏接口
def subCollect(collect):

    res=userDao.subCollect(collect)
    if res:
        if res == -1:
            return json.dumps({"status_code":"10041","status_text":"取消收藏失败",})
        else:
            return json.dumps({"status_code":"10040","status_text":"取消收藏成功", "content": res})
    else:
        return json.dumps({"status_code": "40004", "status_text": "系统错误"})
    # 提醒
    # userDao.subCollect()


# 获取收藏接口
def getCollectList(collect_type,user_id):
    if collect_type=="case":
        res = userDao.getCaseCollect(user_id)
    elif collect_type=="company":
        res = userDao.getCompanyCollect(user_id)
    elif collect_type=="strategy":
        res = userDao.getStrategyCollect(user_id)
    elif collect_type=="diary":
        res = userDao.getDiaryCollect(user_id)
        if res and res != -1:
            for i in range(len(res)):
                diary_img = res[i]["diary_img"].split(",")
                res[i]["diary_img"] = diary_img
    if res:
        if res == -1:
            return json.dumps({"status_code": "10008", "status_text": "未找到数据"})
        else:
            for r in res:
                collect_date = str(r["collect_date"]).replace("-", "/")
                r["collect_date"] = collect_date
            return json.dumps({"status_code": "10009", "status_text": "找到数据", "content": res})
    else:
        return json.dumps({"status_code": "40004", "status_text": "系统错误"})

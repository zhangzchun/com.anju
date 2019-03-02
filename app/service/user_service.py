
#用户接口
import app.dao.user_dao as userDao
# 导入json
import json
import random
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
            return json.dumps({"status_code": "40004", "status_text": "系统错误"})
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
        return json.dumps({"status_code": "10004", "status_text": "该用户不存在"})


# 获取用户信息接口
def getUserInfo(user):
    res = userDao.getUserInfo(user["user_id"])
    if res:
        if res == -1:
            return json.dumps({"status_code": "10008", "status_text": "未找到数据"})
        else:
            return json.dumps({"status_code": "10009", "status_text": "找到数据", "content": res})
    else:
        return json.dumps({"status_code": "40004", "status_text": "系统错误"})


# 修改用户信息
def changeUserInfo(info):
    if info:
        res=userDao.changeUserInfo(info)
        if res:
            return json.dumps({"status_code":"10012","status_text":"添加信息成功"})
        else:
            return json.dumps({"status_code":"10013","status_text": "添加信息失败"})
    else:
        return json.dumps({"status_code": "40005", "status_text": "数据格式不合法"})


# 获取验证码
def getIdentifyingCode():
    id=random.choice(range(1,26))
    res=userDao.getIdentifyingCode(id)
    if res:
        return json.dumps({"status_code": "10009", "status_text": "找到数据","content":res})
    else:
        return json.dumps({"status_code": "10008", "status_text": "未找到数据"})



# 验证前端验证码
def checkCode(info):
    if info:
        res=userDao.getIdentifyingCode(info['code_id'])
        if res['code_content']==info['content']:
            return json.dumps({"status_code": "10009", "status_text": "找到数据"})
        else:
            return json.dumps({"status_code": "10008", "status_text": "未找到数据"})
    else:
        return json.dumps({"status_code": "40005", "status_text": "数据格式不合法"})



# 修改密码接口
def updatePassword(info):
    if info:
        res=userDao.getPasswordById(info['user_id'])
        print(res['password'])
        # 验证密码是否相同
        if (check_password_hash(res['password'], info['old_password'])):
            # 密码加密
            pf = generate_password_hash(info['new_password'], method='pbkdf2:sha1:1001', salt_length=8)
            info['new_password'] = pf
            res=userDao.updatePassword(info)
            if res:
                return json.dumps({"status_code":"10012","status_text":"添加信息成功"})
            else:
                return json.dumps({"status_code":"10013","status_text": "添加信息失败"})
        else:
            return json.dumps({"status_code": "10005", "status_text": "密码错误"})
    else:
        return json.dumps({"status_code": "40005", "status_text": "数据格式不合法"})



# 房屋信息接口
def getHouseList(user):
    if user["house_id"]:
        res=userDao.getHouseInfo(user["house_id"])
        if res:
            if res == -1:
                return json.dumps({"status_code":"10008","status_text":"未找到数据"})
            else:
                return json.dumps({"status_code": "10009", "status_text": "找到数据", "content": res})
        else:
            return json.dumps({"status_code": "40004", "status_text": "系统错误"})
    else:
        res=userDao.getHouseList(user["user_id"])
        if res:
            if res == -1:
                return json.dumps({"status_code":"10008","status_text":"未找到数据"})
            else:
                return json.dumps({"status_code": "10009", "status_text": "找到数据", "content": res})
        else:
            return json.dumps({"status_code": "40004", "status_text": "系统错误"})



# 新增房屋信息
def addHouseInfo(info):
    if info:
        if info['house_type']=='小户型':
            info['house_type']=8
        elif info['house_type']=='一居':
            info['house_type']=1
        elif info['house_type']=='二居':
            info['house_type']=2
        elif info['house_type']=='三居':
            info['house_type']=3
        elif info['house_type']=='四居':
            info['house_type']=4
        elif info['house_type']=='复式':
            info['house_type']=5
        elif info['house_type']=='别墅':
            info['house_type']=6
        elif info['house_type']=='公寓':
            info['house_type']=7

        res=userDao.addHouseInfo(info)
        if res:
            return json.dumps({"status_code":"10012","status_text":"添加信息成功"})
        else:
            return json.dumps({"status_code":"10013","status_text": "添加信息失败"})
    else:
        return json.dumps({"status_code": "40005", "status_text": "数据格式不合法"})



# 修改房屋信息
def updateHouseInfo(info):
    if info:
        if info['house_type']=='小户型':
            info['house_type']=8
        elif info['house_type']=='一居':
            info['house_type']=1
        elif info['house_type']=='二居':
            info['house_type']=2
        elif info['house_type']=='三居':
            info['house_type']=3
        elif info['house_type']=='四居':
            info['house_type']=4
        elif info['house_type']=='复式':
            info['house_type']=5
        elif info['house_type']=='别墅':
            info['house_type']=6
        elif info['house_type']=='公寓':
            info['house_type']=7

        res=userDao.updateHouseInfo(info)
        if res:
            return json.dumps({"status_code":"10012","status_text":"添加信息成功"})
        else:
            return json.dumps({"status_code":"10013","status_text": "添加信息失败"})
    else:
        return json.dumps({"status_code": "40005", "status_text": "数据格式不合法"})









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


# 获取用户日记接口
def getUserDiary(user_id):
    res=userDao.getUserDiary(user_id)
    if res:
        if res == -1:
            return json.dumps({"status_code":"10008","status_text":"未找到数据"})
        else:
            print(res)
            for i in range(len(res)):
                public_date = str(res[i]["public_date"]).replace("-", "/")
                res[i]["public_date"] = public_date
            print(res)
            return json.dumps({"status_code": "10009", "status_text": "找到数据", "content": res})
    else:
        return json.dumps({"status_code": "40004", "status_text": "系统错误"})



def addDiary(diary):
    res = userDao.addDiary(diary)

    if res:
        if res == -1:
            return json.dumps({"status_code": "10013", "status_text": "添加信息失败"})
        else:
            return json.dumps({"status_code": "10012", "status_text": "添加信息成功", "content": res})
    else:
        return json.dumps({"status_code": "40004", "status_text": "系统错误"})



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

# 获取用户信息页面
@user.route('/getUserInfo/',methods=['GET','POST'])
def UserInfo():
    if request.is_json and request.get_json():
        u = request.get_json()
        res = getUserInfo(u)
        return res
    else:
        return json.dumps({"status_code": "40005", "status_text": "数据格式不合法"})






# 修改用户信息页面
@user.route('/changeUserInfo/',methods=['GET','POST'])
def changeInfo():
    if request.is_json and request.get_json():
        info = request.get_json()
        res = changeUserInfo(info)
        return res
    else:
        return json.dumps({"status_code": "40005", "status_text": "数据格式不合法"})


# 获取验证码
@user.route('/getIdentifyingCode/',methods=['GET','POST'])
def getCode():
    if request.method=='GET':
        res = getIdentifyingCode()
        return res
    elif request.method=='POST':
        if request.is_json and request.get_json():
            info = request.get_json()
            res = checkCode(info)
            return res
        else:
            return json.dumps({"status_code": "40005", "status_text": "数据格式不合法"})




# 修改密码页面
@user.route('/changePassword/',methods=['GET','POST'])
def changeUserPassword():
    if request.is_json and request.get_json():
        info = request.get_json()
        print(info)
        res = updatePassword(info)
        print(res)
        return res
    else:
        return json.dumps({"status_code": "40005", "status_text": "数据格式不合法"})







# 用户房屋信息页面
@user.route('/houseList/',methods=['GET','POST'])
@checkLogin(request)
def houseList():
    if request.is_json and request.get_json():
        u = request.get_json()
        res = getHouseList(u)
        return res
    else:
        return json.dumps({"status_code": "40005", "status_text": "数据格式不合法"})



# 用户房屋信息页面
@user.route('/houseInfo/',methods=['GET','POST'])
def houseInfo():
    if request.is_json and request.get_json():
        info = request.get_json()
        print(info)
        res = addHouseInfo(info)
        print(res)
        return res
    else:
        return json.dumps({"status_code": "40005", "status_text": "数据格式不合法"})




#编辑房屋信息
@user.route('/updateHouseInfo/',methods=['GET','POST'])
def updateInfo():
    if request.is_json and request.get_json():
        info = request.get_json()
        res = updateHouseInfo(info)
        return res
    else:
        return json.dumps({"status_code": "40005", "status_text": "数据格式不合法"})





# 用户增加预约
@user.route('/makeAppointment/',methods=['GET','POST'])
# @checkLogin(request)
def makeAppointment():
    # 判断前端数据
    if request.is_json and request.get_json():
        appoint= request.get_json()

        res= addAppointment(appoint)

        return res
    else:
        return json.dumps({"status_code": "40005", "status_text": "数据格式不合法"})



# 用户获得预约
@user.route('/getAppointments/',methods=['GET','POST'])
# @checkLogin(request)
def getAppointments():
    user_id=request.args.get("user_id")
    result=getAppointment(user_id)
    return result



# 用户取消预约
@user.route('/cutAppointment/',methods=['GET','POST'])
# @checkLogin(request)
def cutAppointment():
    # 判断前端数据
    id=request.args.get("id")
    if id:
        res= subAppointment(id)
        return res
    else:
        return json.dumps({"status_code": "40005", "status_text": "数据格式不合法"})





# 修改房屋状态
def updateHouse():

    pass


# 获取用户收藏
@user.route('/collectDetail/',methods=['GET','POST'])
@checkLogin(request)
def collectDetail():
    if request.is_json and request.get_json():
        collect = request.get_json()

        # res为查找收藏的结果
        res = getCollectDetail(collect)
        return res
    else:
        return json.dumps({"status_code": "40005", "status_text": "数据格式不合法"})





# 用户收藏
@user.route('/makeCollect/',methods=['GET','POST'])
@checkLogin(request)
def makeCollect():
    if request.is_json and request.get_json():
        collect = request.get_json()
        # print()
        # res为增加收藏的结果
        res = addCollect(collect)

        return res
    else:
        return json.dumps({"status_code": "40005", "status_text": "数据格式不合法"})



# 用户取消收藏
@user.route('/cutCollect/',methods=['GET','POST'])
@checkLogin(request)
def cutCollect():
    if request.is_json and request.get_json():
        collect = request.get_json()

        # res为取消收藏的结果
        res = subCollect(collect)

        return res
    else:
        return json.dumps({"status_code": "40005", "status_text": "数据格式不合法"})


# 用户收藏信息页面
@user.route("/collectList/", methods=['GET'])
def collectList():
    collect_type=request.args.get("collect_type")
    user_id=request.args.get("user_id")
    if collect_type and user_id:
        result=getCollectList(collect_type,user_id)
        return result
    else:
        return json.dumps({"status_code": "40005", "status_text": "数据格式不合法"})


# 获取用户日记
@user.route('/userDiary/',methods=['GET','POST'])
def userDiary():
    user_id = request.args.get("user_id")
    if user_id:
        result = getUserDiary(user_id)
        print(result)
        return result
    else:
        return json.dumps({"status_code": "40005", "status_text": "数据格式不合法"})



# 添加用户日记
@user.route('/makeDiary/',methods=['GET','POST'])
def makeDiary():
    if request.is_json and request.get_json():
        diary = request.get_json()

        # res为添加日记的结果
        res = addDiary(diary)

        return res
    else:
        return json.dumps({"status_code": "40005", "status_text": "数据格式不合法"})

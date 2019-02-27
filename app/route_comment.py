

# 搜索路由
from flask import Blueprint,request
# 导入search_service模块
from app.service.comment_service import *
from app.utils.my_token import checkLogin
# 导入json
import json


# 用参数name和import_name初始化
comment = Blueprint('comment',__name__)

# restful api

# 获取评论数据
@comment.route('/getComment/', methods=['GET', 'POST'])
def getComment():
    if request.method=="GET":
        id=request.url.split("?")[1].split("=")
        result=getComments(id)
        return result


# 插入评论数据
@comment.route('/postComment/', methods=['GET', 'POST'])
@checkLogin(request)
def postComment():
    if request.method=="POST":
        if request.is_json and request.get_json():
            data=request.get_json()
            result=postComments(data)
            return result
        else:
            return json.dumps({"status_code": "40005", "status_text": "数据格式不合法"})


# 获取回复数据
@comment.route('/getReply/', methods=['GET', 'POST'])
def getReply():
    if request.method == "GET":
        id = request.args.get("comment_id")
        result = getReplys(id)
        return result



# 回复数据
@comment.route('/postReply/', methods=['GET', 'POST'])
@checkLogin(request)
def postReply():
    # 插入回复数据
    if request.method == "POST":
        if request.is_json and request.get_json():
            data=request.get_json()
            result=postReplys(data)
            return result
        else:
            return json.dumps({"status_code": "40005", "status_text": "数据格式不合法"})




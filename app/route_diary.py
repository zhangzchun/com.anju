

# 日记路由
from flask import Blueprint,request
# 导入diary_service模块
from app.service.diary_service import *
# 导入json
import json


# 用参数name和import_name初始化
# diary是模块的名称
diary = Blueprint('diary',__name__)

# restful api

# 日记列表页面
@diary.route('/diaryList/', methods=['GET','POST'])
def diaryList():

    res= getDiaryList()
    return res


# 日记详情页面
@diary.route('/diaryDetail/', methods=['GET','POST'])
def diaryDetail():
    diary_id = request.args.get("diary_id")
    if diary_id:
        result = getDiaryDetail(diary_id)
        return result
    else:
        return json.dumps({"status_code": "40005", "status_text": "数据格式不合法"})

# 发布日记页面
@diary.route('/diaryPub/', methods=['GET','POST'])
def diaryPub():
    pass

# 首页用户头像
@diary.route("/diaryUserIcon/")
def diaryUserIcon():
    result=getDiaryUserIcon()
    return result

# 首页日记展示
@diary.route("/diaryItem/")
def diaryItem():
    diary_id=request.args.get("diary_id")
    result=getDiaryItem(diary_id)
    return result

# 首页攻略日记标题
@diary.route("/diaryTitle/")
def diaryTitle():
    result = getDiaryTitle()
    return result



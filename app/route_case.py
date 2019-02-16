

# 案例路由
from flask import Blueprint,request
# 导入case_service模块
from app.service.case_service import *

import json

# 用参数name和import_name初始化
# diary是模块的名称
case = Blueprint('case',__name__)

# restful api

# 案例列表页面
@case.route('/caseList/',methods=['GET','POST'])
def caseList():
    res = getCaseList()
    return res


# 案例筛选页面
@case.route('/caseScreen/',methods=['GET','POST'])
def caseScreen():

    if request.is_json and request.get_json():
        condition = request.get_json()
        res = getCaseScreen(condition)
        return res
    else:
        return json.dumps({"status_code": "40005", "status_text": "数据格式不合法"})


    # res=  getCaseScreen()
    # return res


# 案例详情页面
@case.route('/caseScreen/',methods=['GET','POST'])
def caseDetail():
    case_id = request.args.get("case_id")
    if case_id:
        res = getCaseDetail(case_id)
        return res
    else:
        return json.dumps({"status_code": "40005", "status_text": "数据格式不合法"})

    # res = getCaseDetail()
    # return res

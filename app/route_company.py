

# 公司路由
from flask import Blueprint,request
# 导入company_service模块
from app.service.company_service import *

import json

# 用参数name和import_name初始化
# diary是模块的名称
company = Blueprint('company',__name__)
# restful api

# 公司列表页面
@company.route('/companyList/', methods=['GET'])
def companyList():
    res = getCompanyList()
    return res

# 首页公司列表
@company.route('/indexCompanyList/', methods=['GET'])
def indexCompanyList():
    res = getIndexCompanyList()
    return res

# 公司筛选页面
@company.route('/companyScreen/', methods=['GET','POST'])
def companyScreen():

    if request.is_json and request.get_json():
        condition = request.get_json()
        res = getCompanyScreen(condition)
        return res
    else:
        return json.dumps({"status_code": "40005", "status_text": "数据格式不合法"})




# 公司排序页面
@company.route('/companySort/', methods=['GET','POST'])
def companySort():

    if request.is_json and request.get_json():
        c = request.get_json()
        res = getCompanySort(c)
        return res
    else:
        return json.dumps({"status_code": "40005", "status_text": "数据格式不合法"})


# 公司详情页面
@company.route('/companyDetail/', methods=['GET'])
def companyDetail():
    company_id = request.args.get("company_id")
    if company_id:
        result = getCompanyDetail(company_id)
        return result
    else:
        return json.dumps({"status_code": "40005", "status_text": "数据格式不合法"})




# 搜索路由
from flask import Blueprint,request
# 导入search_service模块
from app.service.search_service import *
# 导入json
import json


# 用参数name和import_name初始化
# search
search = Blueprint('search',__name__)

# restful api

# 搜索公司页面
@search.route('/', methods=['GET', 'POST'])
def searchs():

    pass



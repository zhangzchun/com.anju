


# 设计师路由
from flask import Blueprint,request
# 导入designer_service模块
from app.service.designer_service import *

import json

# 用参数name和import_name初始化
# diary是模块的名称
designer = Blueprint('designer',__name__)

# restful api


# 设计师列表页面
@designer.route('/designerList/', methods=['GET','POST'])
def designerList():

    res = getDesignerList()
    return res



# 设计师详情页面
@designer.route('/designerDetail/', methods=['GET','POST'])
def designerDetail():

    res = getDesignerDetail()
    return res

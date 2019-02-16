

# 攻略路由
from flask import Blueprint,request
# 导入strategy_service模块
from app.service.strategy_service import *

import json

# 用参数name和import_name初始化
# strategy是模块的名称
strategy = Blueprint('strategy',__name__)

# restful api

# 攻略列表页面
@strategy.route('/strategyList/', methods=['GET','POST'])
def strategyList():
    result = getStrategyList()
    return result


# 攻略详情页面
@strategy.route('/strategyDetail/', methods=['GET'])
def strategyDetail():
    strategy_id = request.args.get("strategy_id")

    # 判断数据
    if strategy_id:
        result = getStrategyDetail(strategy_id)
        return result
    else:
        return json.dumps({"status_code": "40005", "status_text": "数据格式不合法"})


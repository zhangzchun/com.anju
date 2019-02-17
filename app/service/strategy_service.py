


# 攻略接口
import app.dao.strategy_dao as strategyDao
import json

# 攻略列表接口
def getStrategyList():
    res = strategyDao.getStrategyList()
    if res:
        if res == -1:
            return json.dumps({"status_code": "10008", "status_text": "未找到数据"})
        else:
            return json.dumps({"status_code": "10009", "status_text": "找到数据", "content": res})
    else:
        return json.dumps({"status_code": "40004", "status_text": "系统错误"})

    # 提醒作用
    # strategyDao.getStrategyList()


# 攻略详情接口
def getStrategyDetail(id):
    res = strategyDao.getStrategyDetail(id)
    if res:
        if res == -1:
            return json.dumps({"status_code": "10008", "status_text": "未找到数据"})
        else:
            public_date = str(res["public_date"]).replace("-", "/")
            res["public_date"] = public_date
            return json.dumps({"status_code": "10009", "status_text": "找到数据", "content": res})
    else:
        return json.dumps({"status_code": "40004", "status_text": "系统错误"})
    # 提醒
    # strategyDao.getStrategyDetail()


# 首页攻略标题
def getStrategyTitle():
    res = strategyDao.getStrategyTitle()
    if res:
        if res == -1:
            return json.dumps({"status_code": "10008", "status_text": "未找到数据"})
        else:
            return json.dumps({"status_code": "10009", "status_text": "找到数据", "content": res})
    else:
        return json.dumps({"status_code": "40004", "status_text": "系统错误"})


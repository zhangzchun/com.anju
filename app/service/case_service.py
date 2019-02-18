

# 案例接口
import app.dao.case_dao as caseDao
import json


# 案例列表接口
def getCaseList(id):
    res = caseDao.getCaseList(id)
    if res:
        if res == -1:
            return json.dumps({"status_code": "10008", "status_text": "数据不存在"})
        else:
            return json.dumps({"status_code": "10009", "status_text":"找到数据","content": res})
    else:
        return json.dumps({"status_code": "40004", "status_text": "系统错误"})

    # 提醒
    # caseDao.getCaseList()


# 案例筛选接口
def getCaseScreen(condition):

    if condition:
        if condition["area"]=="":
            condition.setdefault('area_min', '')
            condition.setdefault('area_max', '')
        elif condition["area"]=="60m²以下":
            condition.setdefault('area_min', '0')
            condition.setdefault('area_max', '60')
        elif condition["area"]=="60-80m²":
            condition.setdefault('area_min', '60')
            condition.setdefault('area_max', '80')
        elif condition["area"]=="80-100m²":
            condition.setdefault('area_min', '80')
            condition.setdefault('area_max', '100')
        elif condition["area"]=="100-120m²":
            condition.setdefault('area_min', '100')
            condition.setdefault('area_max', '120')
        elif condition["area"]=="120-150m²":
            condition.setdefault('area_min', '120')
            condition.setdefault('area_max', '150')
        elif condition["area"]=="150m²以上":
            condition.setdefault('area_min', '150')
            condition.setdefault('area_max', '999')
        res = caseDao.getCaseScreen(condition)
        if res:
            if res == -1:
                return json.dumps({"status_code": "10008", "status_text": "数据不存在"})
            else:
                return json.dumps({"status_code": "10009", "status_text":"找到数据","content": res})
        else:
            json.dumps({"status_code": "40004", "status_text": "系统错误"})
    else:
        return json.dumps({"status_code": "10006", "status_text": "无数据"})

    # 提醒
    # caseDao.getCaseScreen()

# 案例详情接口
def getCaseDetail(id):
    res = caseDao.getCaseDetail(id)
    if res:
        if res == -1:
            return json.dumps({"status_code": "10008", "status_text": "数据不存在"})
        else:
            return json.dumps({"status_code": "10009", "status_text":"找到数据","content": res})
            # return res
    else:
        return json.dumps({"status_code": "40004", "status_text": "系统错误"})

    # 提醒
    # caseDao.getCaseDetail()



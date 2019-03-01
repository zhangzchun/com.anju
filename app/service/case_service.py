

# 案例接口
import app.dao.case_dao as caseDao
import json


# 获取案例数进行分页
def getCaseNum(condition):
    con=judgeCondition(condition)
    if con.get('sql_num')=='getCaseNum':
        res = caseDao.getCaseNum(con)
        if res:
            if res == -1:
                return json.dumps({"status_code": "10008", "status_text": "数据不存在"})
            else:
                return json.dumps({"status_code": "10009", "status_text": "找到数据", "content": res})
        else:
            return json.dumps({"status_code": "40004", "status_text": "系统错误"})
    else:
        res = caseDao.getScreenNum(con)
        if res:
            if res == -1:
                return json.dumps({"status_code": "10008", "status_text": "数据不存在"})
            else:
                return json.dumps({"status_code": "10009", "status_text": "找到数据", "content": res})
        else:
            return json.dumps({"status_code": "40004", "status_text": "系统错误"})


def judgeCondition(condition):
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


        if (condition["ht_name"] == "" and condition["style_name"] == "" and condition["area_min"] != "" and condition[
            "area_max"] != "") \
                or (
                condition["ht_name"] == "" and condition["area_min"] == "" and condition["area_max"] == "" and condition[
            "style_name"] != "") \
                or (
                condition["style_name"] == "" and condition["area_min"] == "" and condition["area_max"] == "" and condition[
            "ht_name"] != ""):
            condition.setdefault('sql_screen','screen01')
            condition.setdefault('sql_num','screen01_num')
        elif condition["ht_name"] != "" and condition["style_name"] != "" and condition["area_min"] != "" and condition["area_max"] != "":
            condition.setdefault('sql_screen', 'screen03')
            condition.setdefault('sql_num', 'screen03_num')

        elif condition["ht_name"] == "" and condition["style_name"] == "" and condition["area_min"] == "" and condition["area_max"] == "":
            condition.setdefault('sql_screen', 'getCaseList')
            condition.setdefault('sql_num', 'getCaseNum')
        else:
            condition.setdefault('sql_screen', 'screen02')
            condition.setdefault('sql_num', 'screen02_num')

        return condition


# 案例列表接口
def getCaseList(condition):
    condition['pageNum']=(int(condition['pageNum'])-1)*20
    con=judgeCondition(condition)
    res = caseDao.getCaseList(con)
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
        condition['pageNum'] = (int(condition['pageNum']) - 1) * 20
        con=judgeCondition(condition)
        res = caseDao.getCaseScreen(con)
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


if __name__ == '__main__':
    # res=getCaseNum(condition={'company_id': 1, 'pageNum': 1, 'perPageNum': 20, 'ht_name': '一居', 'style_name': '', 'area': ''})
    res=getCaseScreen(condition={'company_id': 1, 'pageNum': 1, 'perPageNum': 20, 'ht_name': '小户型', 'style_name': '', 'area': ''})
    # res=getCaseList(condition={'company_id':1,'pageNum':1,'perPageNum':20,
    #     "ht_name":'',"style_name":'',"area":''})
    # res=judgeCondition(condition={'company_id': 1, 'pageNum': 1, 'perPageNum': 20, 'ht_name': '一居', 'style_name': '', 'area': ''})
    print(res)
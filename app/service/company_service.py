

# 公司接口
import app.dao.company_dao as companyDao

import json


#  公司列表接口
def getCompanyList():
    res = companyDao.getCompanyList()
    if res:
        if res == -1:
            return json.dumps({"status_code": "10008", "status_text": "数据不存在"})
        else:
            return json.dumps({"status_code": "10009", "content": res})
    else:
        return json.dumps({"status_code": "40004", "status_text": "系统错误"})

    # 提醒
    # companyDao.getCompanyList()


# 首页公司列表接口
def getIndexCompanyList():
    res = companyDao.getIndexCompanyList()
    if res:
        if res == -1:
            return json.dumps({"status_code": "10008", "status_text": "数据不存在"})
        else:
            for r in res:
                r["company_icon"]=r["company_icon"][1:]
                r["c_img"]=r["c_img"][1:]
            return json.dumps({"status_code": "10009", "content": res})
    else:
        return json.dumps({"status_code": "40004", "status_text": "系统错误"})


# 公司筛选接口
def getCompanyScreen(condition):

    res = companyDao.getCompanyScreen(condition)
    if res:
        if res == -1:
            return json.dumps({"status_code": "10008", "status_text": "数据不存在"})
        else:
            return json.dumps({"status_code": "10009", "content": res})
    else:
        json.dumps({"status_code": "40004", "status_text": "系统错误"})


    # 提醒
    # companyDao.getCompanyScreen(condition)

# 公司排序接口
def getCompanySort(c):

    if c['detail']=="综合":
        de='sort01'
    elif c['detail']=='案例':
        de='sort02'
    elif c['detail']=='工地':
        de='sort03'
    elif c['detail']=='信用':
        de='sort04'

    res = companyDao.getCompanySort(de)
    if res:
        if res == -1:
            return json.dumps({"status_code": "10008", "status_text": "数据不存在"})
        else:
            return json.dumps({"status_code": "10009", "content": res})
    else:
        return json.dumps({"status_code": "40004", "status_text": "系统错误"})
    # 提醒
    # companyDao.getCompanySort()


# 公司详情接口
def getCompanyDetail(id):

    res=companyDao.getCompanyDetail(id)

    if res:
        if res == -1:
            return json.dumps({"status_code":"10008","status_text":"未找到数据"})
        else:
            return json.dumps({"status_code":"10009","status_text":"找到数据","content":res})
    else:
        return json.dumps({"status_code":"40004","status_text":"系统错误"})

    # 提醒
    # companyDao.getCompanyDetail()

if __name__ == '__main__':
    print(getIndexCompanyList())

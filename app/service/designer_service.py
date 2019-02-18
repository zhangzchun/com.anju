

# 设计师接口
import app.dao.designer_dao as designerDao
import json


# 设计师列表接口
def getDesignerList(company_id):

    res = designerDao.getDesignerList(company_id)
    if res:
        if res == -1:
            return json.dumps({"status_code": "10008", "status_text": "数据不存在"})
        else:
            return json.dumps({"status_code": "10009", "content": res})
    else:
        return json.dumps({"status_code": "40004", "status_text": "系统错误"})

    # 提醒
    # caseDao.getCaseList()




# 设计师详情接口
def getDesignerDetail(designer_id):
    res = designerDao.getCaseList(designer_id)
    if res:
        if res == -1:
            return json.dumps({"status_code": "10008", "status_text": "数据不存在"})
        else:
            return json.dumps({"status_code": "10009", "content": res})
    else:
        return json.dumps({"status_code": "40004", "status_text": "系统错误"})

    # 提醒
    # caseDao.getCaseList()




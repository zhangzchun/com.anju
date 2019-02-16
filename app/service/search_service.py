

# 搜索接口
import app.dao.search_dao as searchDao
import json

# 搜索接口
def getSearchContent(search_condition,search_content):
    if search_condition and search_condition=="装修公司":
        res = getCompanyList(search_content)
        if res:
            if res == -1:
                return json.dumps({"status_code": "10008", "status_text": "未找到数据"})
            else:
                return json.dumps({"status_code": "10009", "status_text": "找到数据", "content": res})
        else:
            return json.dumps({"status_code": "40004", "status_text": "系统错误"})

    elif search_condition and search_condition=="装修攻略":
        res=getStrategyList(search_content)
        if res:
            if res == -1:
                return json.dumps({"status_code": "10008", "status_text": "未找到数据"})
            else:
                return json.dumps({"status_code": "10009", "status_text": "找到数据", "content": res})
        else:
            return json.dumps({"status_code": "40004", "status_text": "系统错误"})

    elif search_condition and search_condition=="装修日记":
        res = getDiaryList(search_content)
        if res:
            if res == -1:
                return json.dumps({"status_code": "10008", "status_text": "未找到数据"})
            else:
                for i in range(len(res)):
                    diary_img = res[i]["diary_img"].split(",")
                    public_date = str(res[i]["public_date"]).replace("-", "/")[0:16]
                    res[i]["diary_img"] = diary_img
                    res[i]["public_date"] = public_date
                return json.dumps({"status_code": "10009", "status_text": "找到数据", "content": res})
        else:
            return json.dumps({"status_code": "40004", "status_text": "系统错误"})

    # 提醒
    searchDao.getStrategyDetail()



# 日记接口
import app.dao.diary_dao as diaryDao
import json


# 日记列表接口
def getDiaryList():
    res = diaryDao.getDiaryList()
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
    # diaryDao.getDiaryList()


# 日记详情接口
def getDiaryDetail(id):
    res = diaryDao.getDiaryDetail(id)
    print(res)
    # return res
    if res[0]:
        if res[0] == -1:
            return json.dumps({"status_code": "10008", "status_text": "未找到数据"})
        else:
            public_date = str(res[0]["public_date"]).replace("-", "/")
            res[0]["public_date"] = public_date
            result = []
            for i in range(len(res[1])):
                public_date = str(res[1][i]["diary_date"]).replace("-", "/")
                res[1][i]["diary_date"] = public_date
                result02 = {}
                for key, value in res[1][i].items():
                    result02[key] = value
                diary_img = result02["diary_img"].split(",")
                result02["diary_img"] = diary_img
                result.append(result02)
            res[0]["stages"] = result
            # return res[0]
            return json.dumps({"status_code": "10009", "status_text": "找到数据", "content": res[0]})

    else:
        return json.dumps({"status_code": "40004", "status_text": "系统错误"})

    # 提醒
    # diaryDao.getDiaryDetail()


# 获取用户头像
def getDiaryUserIcon():
    res = diary_dao.getDiaryUserIcon()
    if res:
        if res == -1:
            return json.dumps({"status_code": "10008", "status_text": "未找到数据"})
        else:
            for r in res:
                r["icon"]=r["icon"][1:]
            return json.dumps({"status_code": "10009", "status_text": "找到数据", "content": res})
    else:
        return json.dumps({"status_code": "40004", "status_text": "系统错误"})

# 首页日记展示
def getDiaryItem(id):
    res = diary_dao.getDiaryItem(id)
    if res:
        if res == -1:
            return json.dumps({"status_code":"10008","status_text":"未找到数据"})
        else:
            diary_img = res["diary_img"].split(",")
            if len(diary_img)>2:
                diary_img=diary_img[0:2]
            for d in range(len(diary_img)):
                diary_img[d]=diary_img[d][1:]
            res["diary_img"] = diary_img
            res["icon"]=res["icon"][1:]
            return json.dumps({"status_code": "10009", "status_text": "找到数据", "content":res})
    else:
        return json.dumps({"status_code":"40004","status_text":"系统错误"})

# 首页攻略日记标题
def getDiaryTitle():
    res = diary_dao.getDiaryTitle()
    if res:
        if res == -1:
            return json.dumps({"status_code": "10008", "status_text": "未找到数据"})
        else:
            return json.dumps({"status_code": "10009", "status_text": "找到数据", "content": res})
    else:
        return json.dumps({"status_code": "40004", "status_text": "系统错误"})


if __name__ == '__main__':
    print(getDiaryDetail(1))

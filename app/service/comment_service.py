import json
import app.dao.comment_dao as commentDao
import datetime

# 获取评论数据
def getComments(id):
    if id[0]=="strategy_id":
        res = commentDao.getStrategyComments(id[1])
    elif id[0]=="diary_id":
        res = commentDao.getDiaryComments(id[1])

    if res:
        if res == -1:
            return json.dumps({"status_code": "10008", "status_text": "未找到数据"})
        else:
            for i in range(len(res)):
                comment_time = str(res[i]["comment_time"]).replace("-", "/")
                res[i]["comment_time"] = comment_time
            return json.dumps({"status_code": "10009", "status_text": "找到数据", "content": res})
    else:
        return json.dumps({"status_code": "40004", "status_text": "系统错误"})

# 获取回复数据
def getReplys(id):
    res = commentDao.getReplys(id)
    if res:
        if res == -1:
            return json.dumps({"status_code": "10008", "status_text": "未找到数据"})
        else:
            for i in range(len(res)):
                reply_time = str(res[i]["reply_time"]).replace("-", "/")
                res[i]["reply_time"] = reply_time
            return json.dumps({"status_code": "10009", "status_text": "找到数据", "content": res})
    else:
        return json.dumps({"status_code": "40004", "status_text": "系统错误"})

# 插入评论数据
def postComments(data):
    res = commentDao.postComments(data)
    if res:
        if res == -1:
            return json.dumps({"status_code": "10011", "status_text": "评论失败"})
        else:
            return json.dumps({"status_code": "10010", "status_text": "评论成功", "content": res})
    else:
        return json.dumps({"status_code": "40004", "status_text": "系统错误"})

# 插入回复数据
def postReplys(data):
    res = commentDao.postReplys(data)
    print(res)
    if res[0] and res[1]:
        if res[0]==-1 or res[1] == -1:
            return json.dumps({"status_code": "10011", "status_text": "评论失败"})
        else:
            return json.dumps({"status_code": "10010", "status_text": "评论成功", "content": res})
    else:
        return json.dumps({"status_code": "40004", "status_text": "系统错误"})


if __name__ == '__main__':
    data={'from_uid': '2', 'comment_id': '27', 'reply_id': "null", 'reply_type_id': 1, 'reply_content': '呵呵呵', 'to_uid': '1', 'to_unickname': '瀚海百丈冰', 'reply_time': '2019/02/20'}

    # data={'from_uid': '2',"comment_content":"hahaha","comment_time":'2019/02/20 18:17:43',"comment_type_id":"1","comment_obj_id":"1"}
    print(postReplys(data))

from . import POOL
import pymysql
# 导入SQL语句
from app.dao.sql.comment_sql import comment_sql


# 获取攻略评论数据
def getStrategyComments(id):
    try:
        client = POOL.connection()
        diary_collect=None
        cursor = client.cursor(cursor=pymysql.cursors.DictCursor)
        sql = comment_sql["getStrategyComments"].format(strategy_id=id)
        cursor.execute(sql)
        diary_collect=cursor.fetchall() or -1
        client.commit()
    except Exception as ex:
        client.rollback()
    finally:
        client.close()
        return diary_collect

# 获取日记评论数据
def getDiaryComments(id):
    try:
        client = POOL.connection()
        diary_collect=None
        cursor = client.cursor(cursor=pymysql.cursors.DictCursor)
        sql = comment_sql["getDiaryComments"].format(diary_id=id)
        cursor.execute(sql)
        diary_collect=cursor.fetchall() or -1
        client.commit()
    except Exception as ex:
        client.rollback()
    finally:
        client.close()
        return diary_collect

# 获取回复数据
def getReplys(id):
    try:
        client = POOL.connection()
        diary_collect=None
        cursor = client.cursor(cursor=pymysql.cursors.DictCursor)
        sql = comment_sql["getReplys"].format(comment_id=id)
        cursor.execute(sql)
        diary_collect=cursor.fetchall() or -1
        client.commit()
    except Exception as ex:
        client.rollback()
    finally:
        client.close()
        return diary_collect

# 插入评论数据
def postComments(data):
    try:
        client = POOL.connection()
        comment_d=None
        cursor = client.cursor(cursor=pymysql.cursors.DictCursor)
        sql = comment_sql["postComments"].format(from_uid=data["from_uid"],comment_content=data["comment_content"],
            commnet_time=data["comment_time"],comment_type_id=data["comment_type_id"],comment_obj_id=data["comment_obj_id"])
        comment_d=cursor.execute(sql) or -1
        client.commit()
    except Exception as ex:
        client.rollback()
    finally:
        client.close()
        return comment_d

# 插入回复数据
def postReplys(data):
    try:
        client = POOL.connection()
        reply_d=None
        reply_d01=None
        cursor = client.cursor(cursor=pymysql.cursors.DictCursor)
        sql = comment_sql["postReplys"].format(from_uid=data["from_uid"],comment_id=data["comment_id"],
              reply_id=data["reply_id"],reply_type_id=data["reply_type_id"],reply_content=data["reply_content"],
              to_uid=data["to_uid"],to_unickname=data["to_unickname"],reply_time=data["reply_time"])

        print(sql)
        reply_d=cursor.execute(sql) or -1
        sql01 = comment_sql["postReplys01"].format(comment_id=data["comment_id"])
        reply_d01 = cursor.execute(sql01) or -1
        client.commit()
    except Exception as ex:
        print(ex)
        client.rollback()
    finally:
        client.close()
        return reply_d,reply_d01
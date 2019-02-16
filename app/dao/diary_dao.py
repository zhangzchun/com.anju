


# 日记模块
from . import POOL
import pymysql
# 导入SQL语句
from app.dao.sql.diary_sql import diary_sql


# 日记列表数据
def getDiaryList():
    try:
        client = POOL.connection()
        diary_list=None
        cursor = client.cursor(cursor=pymysql.cursors.DictCursor)
        sql = diary_sql["getDiaryList"]
        cursor.execute(sql)
        diary_list=cursor.fetchall() or -1
        # print("")
        client.commit()
    except Exception as ex:
        client.rollback()
    finally:
        client.close()
        return diary_list


# 日记详情数据
def getDiaryDetail():
    try:
        client = POOL.connection()
        diary_info01=None
        diary_info02=None
        cursor = client.cursor(cursor=pymysql.cursors.DictCursor)
        sql01 = diary_sql["getDiaryInfo01"].format(id=id)
        cursor.execute(sql01)
        diary_info01=cursor.fetchone() or -1

        sql02 = diary_sql["getDiaryInfo02"].format(id=id)
        cursor.execute(sql02)
        diary_info02 = cursor.fetchall() or -1

        client.commit()
    except Exception as ex:
        client.rollback()
    finally:
        client.close()
        return diary_info01 , diary_info02


# 添加日记数据
def pub():
    pass


# 首页用户头像
def getDiaryUserIcon():
    try:
        client = POOL.connection()
        user_icon = None
        cursor = client.cursor(cursor=pymysql.cursors.DictCursor)
        sql = diary_sql.get("getDiaryUserIcon")
        cursor.execute(sql)
        user_icon = cursor.fetchall() or -1
        client.commit()
    except Exception as ex:
        client.rollback()
    finally:
        client.close()
        return user_icon
    
# 首页日记展示
def getDiaryItem(id):
    try:
        client = POOL.connection()
        diary_item=None
        cursor = client.cursor(cursor=pymysql.cursors.DictCursor)
        sql = diary_sql.get("getDiaryItem").format(diary_id=id)
        cursor.execute(sql)
        diary_item=cursor.fetchone() or -1
        client.commit()
    except Exception as ex:
        client.rollback()
    finally:
        client.close()
        return diary_item
    
# 首页攻略日记标题
def getDiaryTitle():
    try:
        client = POOL.connection()
        diary_title=None
        cursor = client.cursor(cursor=pymysql.cursors.DictCursor)
        sql = diary_sql.get("getDiaryTitle")
        cursor.execute(sql)
        diary_title=cursor.fetchall() or -1
        client.commit()
    except Exception as ex:
        client.rollback()
    finally:
        client.close()
        return diary_title

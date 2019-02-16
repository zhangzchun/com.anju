


# 搜索模块
from . import POOL
import pymysql
# 导入SQL语句
from app.dao.sql.search_sql import search_sql


# 搜索公司数据
def getCompanyList(search_content):
    try:
        client = POOL.connection()
        company_list = None
        cursor = client.cursor(cursor=pymysql.cursors.DictCursor)
        # 4. 准备sql语句
        sql = search_sql.get('getCompanyList').format(search_content=search_content)
        cursor.execute(sql)
        company_list = cursor.fetchall() or -1
        client.commit()
    except Exception as ex:
        client.rollback()
    finally:
        client.close()
        return company_list



# 搜索日记数据
def getDiaryList(search_content):
    try:
        client = POOL.connection()
        diary_list=None
        cursor = client.cursor(cursor=pymysql.cursors.DictCursor)
        sql = search_sql["getDiaryList"].format(search_content=search_content)
        cursor.execute(sql)
        diary_list=cursor.fetchall() or -1
        client.commit()
    except Exception as ex:
        client.rollback()
    finally:
        client.close()
        return diary_list



# 搜索攻略数据
def getStrategyList(search_content):
    try:
        client = POOL.connection()
        strategy_list=None
        cursor = client.cursor(cursor=pymysql.cursors.DictCursor)
        sql = search_sql["getStrategyList"].format(search_content=search_content)
        cursor.execute(sql)
        strategy_list=cursor.fetchall() or -1
        client.commit()
    except Exception as ex:
        client.rollback()
    finally:
        client.close()
        return strategy_list



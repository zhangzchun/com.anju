


# 攻略模块
from . import POOL
import pymysql
# 导入SQL语句
from app.dao.sql.strategy_sql import strategy_sql


# 攻略列表数据
def getStrategyList():
    try:
        client = POOL.connection()
        strategy_list=None
        cursor = client.cursor(cursor=pymysql.cursors.DictCursor)
        sql = strategy_sql["getStrategyList"]
        cursor.execute(sql)
        strategy_list=cursor.fetchall() or -1
        client.commit()
    except Exception as ex:
        client.rollback()
    finally:
        client.close()
        return strategy_list



# 攻略详情数据
def getStrategyDetail(id):
    try:
        client = POOL.connection()
        strategy_detail=None
        cursor = client.cursor(cursor=pymysql.cursors.DictCursor)
        sql = strategy_sql["getStrategyDetail"].format(id=id)
        cursor.execute(sql)
        strategy_detail=cursor.fetchone() or -1
        client.commit()
    except Exception as ex:
        client.rollback()
    finally:
        client.close()
        return strategy_detail


# 首页攻略标题
def getStrategyTitle():
    try:
        client = POOL.connection()
        strategy_title=None
        cursor = client.cursor(cursor=pymysql.cursors.DictCursor)
        sql = strategy_sql.get("getStrategyTitle")
        cursor.execute(sql)
        strategy_title=cursor.fetchall() or -1
        client.commit()
    except Exception as ex:
        client.rollback()
    finally:
        client.close()
        return strategy_title


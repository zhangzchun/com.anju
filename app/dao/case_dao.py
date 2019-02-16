


# 案例模块
from . import POOL
import pymysql
# 导入SQL语句
from app.dao.sql.case_sql import case_sql


# 案例列表数据
def getCaseList():
    try:
        client = POOL.connection()
        case = None
        cursor = client.cursor(cursor=pymysql.cursors.DictCursor)
        # 4. 准备sql语句
        sql = case_sql.get('getCaseList')

        # sql = sql_user.get('addUser').format(telephone=user['telephone'], password=user['password'])
        # 5. 通过游标进行操作,execute()执行sql语句,这时结果为：1.如果插入成功返回受影响的行数 2. 如果插入失败返回None
        cursor.execute(sql)
        case = cursor.fetchall() or -1
        client.commit()
    except Exception as ex:
        client.rollback()
    finally:
        client.close()
        return case


# 案例筛选数据
def getCaseScreen(condition):
    try:
        client = POOL.connection()
        case = None
        cursor = client.cursor(cursor=pymysql.cursors.DictCursor)
        # 4. 准备sql语句
        if (condition["ht_name"] == "" and condition["style_name"] == "" and condition["area_min"] != "" and condition["area_max"] != "") \
                or (condition["ht_name"] == "" and condition["area_min"] == "" and condition["area_max"] == "" and condition["style_name"] != "") \
                or (condition["style_name"] == "" and condition["area_min"] == "" and condition["area_max"] == "" and condition["ht_name"] != ""):
            sql = case_sql.get('screen01').format(ht_name=condition["ht_name"],
                                                            style_name=condition["style_name"],
                                                            area_min=condition["area_min"],
                                                            area_max=condition["area_max"])
        elif condition["ht_name"] == ""and (condition["style_name"] != "" and condition["area_min"] != "" and condition["area_max"] != "") \
                or condition["style_name"] == "" and (condition["ht_name"] != "" and condition["area_min"] != "" and condition["area_max"] != "")\
                or condition["area_min"] == "" and condition["area_max"] == "" and (condition["style_name"] != "" and condition["ht_name"] != ""):
            sql = case_sql.get('screen02').format(ht_name=condition["ht_name"],
                                                            style_name=condition["style_name"],
                                                            area_min=condition["area_min"],
                                                            area_max=condition["area_max"])
        else:
            sql = case_sql.get('screen03').format(ht_name=condition["ht_name"],
                                                           style_name=condition["style_name"],
                                                              area_min=condition["area_min"],
                                                              area_max=condition["area_max"])
        cursor.execute(sql)
        case = cursor.fetchall() or -1
        client.commit()
    except Exception as ex:
        client.rollback()
    finally:
        client.close()
        return case

# 案例详情数据
def getCaseDetail():
    try:
        client = POOL.connection()
        case = None
        cursor = client.cursor(cursor=pymysql.cursors.DictCursor)
        sql = case_sql.get('detail').format(case_id=id)
        cursor.execute(sql)
        case = cursor.fetchall() or -1
        client.commit()
    except Exception as ex:
        client.rollback()
    finally:
        client.close()
        return case




# 案例模块
from . import POOL
import pymysql
# 导入SQL语句
from app.dao.sql.case_sql import case_sql


# 获取案例数
def getCaseNum(con):
    try:
        client = POOL.connection()
        case_num = None
        cursor = client.cursor(cursor=pymysql.cursors.DictCursor)
        sql = case_sql.get(con['sql_num']).format(company_id=con['company_id'])
        cursor.execute(sql)
        case_num = cursor.fetchone() or -1
        client.commit()
    except Exception as ex:
        client.rollback()
    finally:
        client.close()
        return case_num


def getScreenNum(con):
    try:
        client = POOL.connection()
        case_num = None
        cursor = client.cursor(cursor=pymysql.cursors.DictCursor)
        sql = case_sql.get(con['sql_num']).format(ht_name=con["ht_name"],style_name=con["style_name"],
                                            area_min=con["area_min"],area_max=con["area_max"],company_id=con['company_id'])
        cursor.execute(sql)
        case_num = cursor.fetchone() or -1
        client.commit()
    except Exception as ex:
        client.rollback()
    finally:
        client.close()
        return case_num




# 案例列表数据
def getCaseList(con):
    try:
        client = POOL.connection()
        case = None
        cursor = client.cursor(cursor=pymysql.cursors.DictCursor)
        # 4. 准备sql语句
        sql = case_sql.get('getCaseList').format(company_id=con['company_id'],pageNum=con['pageNum'],
                                                 perPageNum=con['perPageNum'])

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
def getCaseScreen(con):
    try:
        client = POOL.connection()
        case = None
        cursor = client.cursor(cursor=pymysql.cursors.DictCursor)

        sql = case_sql.get(con['sql_screen']).format(ht_name=con["ht_name"],style_name=con["style_name"],
                                            area_min=con["area_min"],area_max=con["area_max"],company_id=con['company_id'],
                                            pageNum=con['pageNum'],perPageNum=con['perPageNum'])
        cursor.execute(sql)
        case = cursor.fetchall() or -1
        client.commit()
    except Exception as ex:
        client.rollback()
    finally:
        client.close()
        return case

# 案例详情数据
def getCaseDetail(id):
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

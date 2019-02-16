


# 公司模块
from . import POOL
import pymysql
# 导入SQL语句
from app.dao.sql.company_sql import company_sql



# 公司列表数据
def getCompanyList():
    try:
        client = POOL.connection()
        company = None
        cursor = client.cursor(cursor=pymysql.cursors.DictCursor)
        # 4. 准备sql语句
        sql = company_sql.get('getCompanyList')

        # sql = sql_user.get('addUser').format(telephone=user['telephone'], password=user['password'])
        # 5. 通过游标进行操作,execute()执行sql语句,这时结果为：1.如果插入成功返回受影响的行数 2. 如果插入失败返回None
        cursor.execute(sql)
        company = cursor.fetchall() or -1
        client.commit()
    except Exception as ex:
        client.rollback()
    finally:
        client.close()
        return company




# 公司筛选数据
def getCompanyScreen(condition):
    try:
        client = POOL.connection()
        company = None
        cursor = client.cursor(cursor=pymysql.cursors.DictCursor)
        # 4. 准备sql语句
        if (condition["price_name"] == "" and condition["style_name"] == "" and condition["district"] != "") \
                or (condition["price_name"] == "" and condition["district"] == "" and condition["style_name"] != "") \
                or (condition["style_name"] == "" and condition["district"] == "" and condition["price_name"] != ""):
            sql = company_sql.get('screen01').format(price_name=condition["price_name"],
                                                                  style_name=condition["style_name"],
                                                                  district=condition["district"])
        elif condition["price_name"] == ""and (condition["style_name"] != "" and condition["district"] != "") \
                or condition["style_name"] == "" and (condition["price_name"] != "" and condition["district"] != "")\
                or condition["district"] == "" and (condition["style_name"] != "" and condition["price_name"] != ""):
            sql = company_sql.get('screen02').format(price_name=condition["price_name"],
                                                                  style_name=condition["style_name"],
                                                                  district=condition["district"])
        else:
            sql = company_sql.get('screen03').format(price_name=condition["price_name"],
                                                                  style_name=condition["style_name"],
                                                                  district=condition["district"])
        cursor.execute(sql)
        company = cursor.fetchall() or -1
        client.commit()
    except Exception as ex:
        client.rollback()
    finally:
        client.close()
        return company


# 公司排序数据
def getCompanySort(s):
    try:
        client = POOL.connection()
        company = None
        cursor = client.cursor(cursor=pymysql.cursors.DictCursor)
        sql = company_sql.get(s)
        cursor.execute(sql)
        company = cursor.fetchall() or -1
        client.commit()
    except Exception as ex:
        client.rollback()
    finally:
        client.close()
        return company



# 公司详情数据
def getCompanyDetail(id):

    try:
        client = POOL.connection()
        company_detail = None
        cursor = client.cursor(cursor=pymysql.cursors.DictCursor)
        sql=company_sql.get("getCompanyDetail").format(id=id)
        cursor.execute(sql)
        company_detail=cursor.fetchone() or -1
        client.commit()
    except Exception as ex:
        client.rollback()
    finally:
        client.close()
        return company_detail
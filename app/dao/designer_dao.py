


# 设计师模块
from . import POOL
import pymysql
# 导入SQL语句
from app.dao.sql.designer_sql import designer_sql


# 设计师列表数据
def getDesignerList(company_id):
    try:
        client = POOL.connection()
        designer_detail = None
        cursor = client.cursor(cursor=pymysql.cursors.DictCursor)
        # 4. 准备sql语句
        sql = designer_sql.get('getDesignerList').format(id=company_id)

        # sql = sql_user.get('addUser').format(telephone=user['telephone'], password=user['password'])
        # 5. 通过游标进行操作,execute()执行sql语句,这时结果为：1.如果插入成功返回受影响的行数 2. 如果插入失败返回None
        cursor.execute(sql)
        designer_detail = cursor.fetchall() or -1
        client.commit()
    except Exception as ex:
        client.rollback()
    finally:
        client.close()
        # print(designer_detail)
        return designer_detail



# 设计师详情数据
def getDesignerDetail(designer_id):
    try:
        client = POOL.connection()
        case = None
        cursor = client.cursor(cursor=pymysql.cursors.DictCursor)
        # 4. 准备sql语句
        sql = designer_sql.get('getDesignerDetail').format(id=designer_id)

        # sql = sql_user.get('addUser').format(telephone=user['telephone'], password=user['password'])
        # 5. 通过游标进行操作,execute()执行sql语句,这时结果为：1.如果插入成功返回受影响的行数 2. 如果插入失败返回None
        cursor.execute(sql)
        designer_detail = cursor.fetchall() or -1
        client.commit()
    except Exception as ex:
        client.rollback()
    finally:
        client.close()
        return designer_detail
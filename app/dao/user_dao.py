


# 用户模块
from . import POOL
import pymysql
# 导入SQL语句
from app.dao.sql.user_sql import user_sql


# 注册用户数据
def addUser(user):
    '''
    :param user:
    :return: 添加用户结果
    '''

    if not getUserByTel(user['telephone']):
        try:
            client = POOL.connection()
            user_id = None
            cursor = client.cursor(cursor=pymysql.cursors.DictCursor)
            # 4. 准备sql语句

            sql = user_sql.get('addUser').format(telephone=user['telephone'], nickname=user['nickname'],
                                                 password=user['password'])
            # 5. 通过游标进行操作,execute()执行sql语句,这时结果为：1.如果插入成功返回受影响的行数 2. 如果插入失败返回None

            user_id = cursor.execute(sql)
            client.commit()
        except Exception as ex:
            client.rollback()
        finally:
            if user_id == 1:
                user_id = getUserByTel(user['telephone'])
            client.close()
            # print(user_id)
            return user_id
    else:
        return -1


# 查找用户数据
def getUserByTel(tel):
    try:
        client = POOL.connection()
        res_user = -1
        cursor = client.cursor(cursor=pymysql.cursors.DictCursor)
        # 4. 准备sql语句
        sql = user_sql.get('getUserByTel').format(telephone=tel)

        # 5. 通过游标进行操作,execute()执行sql语句,这时结果为：1.如果插入成功返回受影响的行数 2. 如果插入失败返回None
        cursor.execute(sql)
        res_user = cursor.fetchone()
        client.commit()
    except Exception as ex:
        client.rollback()
    finally:
        client.close()
        return res_user



# 修改用户数据
def updateUser(user):
    pass

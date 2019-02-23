


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




# 获取用户房屋信息数据
def getHouseList(id):
    try:
        client = POOL.connection()
        res_house = -1
        cursor = client.cursor(cursor=pymysql.cursors.DictCursor)
        # 4. 准备sql语句
        sql = user_sql.get('getHouseList').format(id=id)

        # 5. 通过游标进行操作,execute()执行sql语句,这时结果为：1.如果插入成功返回受影响的行数 2. 如果插入失败返回None
        cursor.execute(sql)
        res_house = cursor.fetchall()
        client.commit()
    except Exception as ex:
        client.rollback()
    finally:
        client.close()
        return res_house



# 添加用户预约数据
def addAppointment(appoint):
    try:
        client = POOL.connection()
        res_appoint = -1
        cursor = client.cursor(cursor=pymysql.cursors.DictCursor)
        # 4. 准备sql语句
        sql = user_sql.get('addAppointment').format(house_id=appoint['house_id'],
                                                    company_id=appoint['company_id'],
                                                    user_id=appoint['user_id'])

        # 5. 通过游标进行操作,execute()执行sql语句,这时结果为：1.如果插入成功返回受影响的行数 2. 如果插入失败返回None

        res_appoint = cursor.execute(sql)
        client.commit()
    except Exception as ex:
        client.rollback()
    finally:
        client.close()
        return res_appoint

# 获取预约数据
def getAppointment(id):
    try:
        client = POOL.connection()
        res_appointment = None
        cursor = client.cursor(cursor=pymysql.cursors.DictCursor)
        # 4. 准备sql语句
        sql = user_sql.get('getAppointment').format(user_id=id)

        # 5. 通过游标进行操作,execute()执行sql语句,这时结果为：1.如果插入成功返回受影响的行数 2. 如果插入失败返回None

        cursor.execute(sql)
        res_appointment =cursor.fetchall() or -1
        client.commit()
    except Exception as ex:
        client.rollback()
    finally:
        client.close()
        return res_appointment


# 取消预约
def subAppointment(id):
    try:
        client = POOL.connection()
        res_appoint = None
        cursor = client.cursor(cursor=pymysql.cursors.DictCursor)
        # 4. 准备sql语句
        sql = user_sql.get('subAppointment').format(id=id)

        # 5. 通过游标进行操作,execute()执行sql语句,这时结果为：1.如果插入成功返回受影响的行数 2. 如果插入失败返回None

        res_appoint = cursor.execute(sql) or -1
        client.commit()
    except Exception as ex:
        client.rollback()
    finally:
        client.close()
        return res_appoint


# 修改房屋状态数据
def updateHouse(house_id):
    pass




# 用户收藏数据

def getCollectDetail(collect):
    try:
        client = POOL.connection()
        res_collect = -1
        cursor = client.cursor(cursor=pymysql.cursors.DictCursor)
        # 4. 准备sql语句
        sql = user_sql.get('getCollect').format(content_id=collect['content_id'],
                                                collect_type_id=collect['collect_type_id'],
                                                user_id=collect['user_id'])

        # 5. 通过游标进行操作,execute()执行sql语句,这时结果为：1.如果插入成功返回受影响的行数 2. 如果插入失败返回None
        cursor.execute(sql)

        res_collect = cursor.execute(sql)
        client.commit()
    except Exception as ex:
        client.rollback()
    finally:
        client.close()
        return res_collect


# 增加收藏数据
def addCollect(collect):
    try:
        client = POOL.connection()
        res_collect = -1
        cursor = client.cursor(cursor=pymysql.cursors.DictCursor)
        # 4. 准备sql语句
        sql = user_sql.get('addCollect').format(content_id=collect['content_id'],
                                                collect_type_id=collect['collect_type_id'],
                                                user_id=collect['user_id'])

        # 5. 通过游标进行操作,execute()执行sql语句,这时结果为：1.如果插入成功返回受影响的行数 2. 如果插入失败返回None

        res_collect = cursor.execute(sql)
        client.commit()
    except Exception as ex:
        client.rollback()
    finally:
        client.close()
        return res_collect



# 取消收藏数据
def subCollect(collect):
    try:
        client = POOL.connection()
        res_collect = -1
        cursor = client.cursor(cursor=pymysql.cursors.DictCursor)
        # 4. 准备sql语句
        sql = user_sql.get('subCollect').format(content_id=collect['content_id'],
                                                collect_type_id=collect['collect_type_id'],
                                                user_id=collect['user_id'])

        # 5. 通过游标进行操作,execute()执行sql语句,这时结果为：1.如果插入成功返回受影响的行数 2. 如果插入失败返回None

        res_collect = cursor.execute(sql)
        client.commit()
    except Exception as ex:
        client.rollback()
    finally:
        client.close()
        return res_collect


# 获取收藏的案例
def getCaseCollect(id):
    try:
        client = POOL.connection()
        case_collect=None
        cursor = client.cursor(cursor=pymysql.cursors.DictCursor)
        sql = user_sql["getCaseCollect"].format(user_id=id)
        cursor.execute(sql)
        case_collect=cursor.fetchall() or -1
        client.commit()
    except Exception as ex:
        client.rollback()
    finally:
        client.close()
        return case_collect


# 获取收藏的公司
def getCompanyCollect(id):
    try:
        client = POOL.connection()
        company_collect=None
        cursor = client.cursor(cursor=pymysql.cursors.DictCursor)
        sql = user_sql["getCompanyCollect"].format(user_id=id)
        cursor.execute(sql)
        company_collect=cursor.fetchall() or -1
        client.commit()
    except Exception as ex:
        client.rollback()
    finally:
        client.close()
        return company_collect

# 获取收藏的攻略
def getStrategyCollect(id):
    try:
        client = POOL.connection()
        strategy_collect=None
        cursor = client.cursor(cursor=pymysql.cursors.DictCursor)
        sql = user_sql["getStrategyCollect"].format(user_id=id)
        cursor.execute(sql)
        strategy_collect=cursor.fetchall() or -1
        client.commit()
    except Exception as ex:
        client.rollback()
    finally:
        client.close()
        return strategy_collect

# 获取收藏的日记
def getDiaryCollect(id):
    try:
        client = POOL.connection()
        diary_collect=None
        cursor = client.cursor(cursor=pymysql.cursors.DictCursor)
        sql = user_sql["getDiaryCollect"].format(user_id=id)
        cursor.execute(sql)
        diary_collect=cursor.fetchall() or -1
        client.commit()
    except Exception as ex:
        client.rollback()
    finally:
        client.close()
        return diary_collect


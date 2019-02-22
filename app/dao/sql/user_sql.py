

user_sql={
    "addUser":"insert into user(telephone,nickname,password,regist_date) \
              values('{telephone}','{nickname}','{password}',CURDATE())",

    "getUserByTel":"select id,telephone,nickname,password,regist_date \
                  from user where telephone={telephone} limit 1",

    "updateUserById":"",


    "getHouseList":"select house.id, house.house_name, house_type.`name` as house_type,\
                  house.area,house.address, house.village \
                  from house inner join house_type on house.house_type_id=house_type.id \
                  where user_id={id}",




    "addAppointment":"insert into appointment(house_id,company_id,user_id) \
                          values('{house_id}','{company_id}','{user_id}')",


    "subAppointment":"delete from appointment where house_id={house_id} \
                      and company_id={company_id} and user_id={user_id}",

    "updateHouse":"",


    "getCollect":"select id from where where content_id={content_id} \
                          and collect_type_id={collect_type_id} and user_id={user_id}",

    "addCollect":"insert into collect(content_id,collect_type_id,user_id)\
                          values('{content_id}','{collect_type_id}','{user_id}')",


    "subCollect":"delete from collect where content_id={content_id} \
                          and collect_type_id={collect_type_id} and user_id={user_id}",


}

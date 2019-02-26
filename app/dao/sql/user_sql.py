

user_sql={
    "addUser":"insert into user(telephone,nickname,password,regist_date) \
              values('{telephone}','{nickname}','{password}',CURDATE())",

    "getUserByTel":"select id,telephone,nickname,password,regist_date \
                  from user where telephone={telephone} limit 1",

    "getUserInfo":"select `user`.nickname,`user`.telephone,user_icon.icon,sex.gender as sex,`user`.QQ,`user`.address\
                    from `user` INNER JOIN user_icon INNER JOIN sex\
                    on `user`.user_icon_id=user_icon.id  and `user`.sex_id=sex.id\
                    WHERE `user`.id={id}",

    "changeUserInfo":"update `user` set nickname='{nickname}',sex_id={sex_id},QQ={QQ},address='{address}'\
                        where id={id}",


    "getIdentifyingCode":"select i.id,i.url_code,i.code_content from identifying_code as i WHERE i.id={id}",

    "getPasswordById":"select `user`.`password` from `user`  WHERE `user`.id={id}",

    "updatePassword":"update `user` set `password`='{password}' where id={id}",

    "getHouseList":"SELECT house.id, house.house_name, house_type.`name` as house_type,\
                      house.area,house.house_status,house.address, house.village \
                      FROM house INNER JOIN house_type ON house.house_type_id=house_type.id \
                      where user_id={id}",

    "getHouseInfo": "SELECT house.id, house.house_name, house_type.`name` as house_type,house.area,house.house_status,house.address, house.village\
                  FROM house INNER JOIN house_type ON house.house_type_id=house_type.id\
                  where house.id={id}",

    "addHouseInfo": "insert into house(house_name,house_type_id,area,address,house_status,user_id,village)\
                values ('{house_name}','{house_type}','{area}','{address}','{status}','{user_id}','{village}')",

    "updateHouseInfo": "update house set house_name='{house_name}',house_type_id='{house_type}',area='{area}',\
                      address='{address}',house_status='{status}',village='{village}'\
                      where id='{house_id}'",
    "getAppointment":"SELECT a.id, c.company_icon, c.`name` company_name, c.case_num, c.work_site_num, c.contact_tel, \
                    hy.`name` house_type, h.area, h.address, h.village, a.appointment_status\
                    from appointment a INNER JOIN company c INNER JOIN house h INNER JOIN house_type hy\
                    ON a.company_id=c.id and a.house_id=h.id and h.house_type_id=hy.id\
                    where a.user_id={user_id}",

    "addAppointment":"insert into appointment(house_id,company_id,user_id) \
                          values('{house_id}','{company_id}','{user_id}')",


    "subAppointment":"delete from appointment where id={id}",

    "updateHouse":"update house set house_status='已定装修公司' where id={id}",


    "getCollect":"select id from collect where content_id={content_id} \
                          and collect_type_id={collect_type_id} and user_id={user_id}",

    "addCollect":"insert into collect(content_id,collect_type_id,user_id)\
                          values('{content_id}','{collect_type_id}','{user_id}','{collect_date}')",


    "subCollect":"delete from collect where content_id={content_id} \
                          and collect_type_id={collect_type_id} and user_id={user_id}",

    "getCaseCollect":"select `case`.id ,ci.img_url,`case`.`name`, `case`.area, s.`name` style_name, \
                    ht.`name` house_type, rt.`name` renovation_type, `case`.price, c.collect_date \
                    from collect c INNER JOIN `case` INNER JOIN case_img ci INNER JOIN style s\
                    INNER JOIN house_type ht INNER JOIN renovation_type rt\
                    on c.content_id=`case`.id and `case`.id=ci.case_id and `case`.style_id=s.id \
                    and `case`.house_type_id=ht.id and `case`.renovation_type_id=rt.id\
                    where c.user_id={user_id} and c.collect_type_id=2 GROUP BY `case`.id",

    "getCompanyCollect":"select company.id , company.company_icon, company.`name`, company.case_num, company.work_site_num,\
                        company.contact_tel,c.collect_date from collect c INNER JOIN company on c.content_id=company.id\
                        where c.user_id={user_id} and c.collect_type_id=1",

    "getDiaryCollect":"SELECT d.id diary_id ,u.nickname,ui.icon , d.diary_title , s.`name` style_name ,d.company ,c.collect_date ,dc.diary_content,\
                        (SELECT group_concat(di.diary_img) FROM diary_img di WHERE di.diary_content_id = dc.id && dc.diary_id=d.id) diary_img \
                        FROM collect c INNER JOIN `user` u INNER JOIN user_icon ui INNER JOIN diary d INNER JOIN style s INNER JOIN diary_content dc \
                        on  u.user_icon_id=ui.id and c.content_id=d.id and d.user_id=u.id and d.style_id=s.id  and d.id=dc.diary_id \
                        where c.user_id={user_id}  and c.collect_type_id=4 and dc.stage='前期准备' ",
    "getStrategyCollect":"select s.id , si.strategy_img,s.strategy_title, sc.lead, c.collect_date \
                        from collect c INNER JOIN collect_type ct INNER JOIN `user` u INNER JOIN strategy s \
                        INNER JOIN strategy_content sc INNER JOIN strategy_img si\
                        on c.collect_type_id = ct.id and c.user_id =u.id and c.content_id=s.id and s.id=sc.strategy_id \
                        and si.strategy_id=s.id where c.user_id={user_id} and c.collect_type_id=3",

    "getUserDiary":"select d.id,d.diary_title,d.public_date,d.area,s.`name` as style, \
                        rt.`name` as reno_type,d.village,d.company,count(d.id) as count\
                        from diary as d inner join style as s inner join renovation_type as rt \
                        inner join diary_content as dc on d.style_id = s.id \
                        and d.renovation_type_id = rt.id and d.id = dc.diary_id \
                        where user_id = {id} group by d.id ",
}

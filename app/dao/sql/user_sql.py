

user_sql={
    "addUser":"insert into user(telephone,nickname,password,regist_date) values('{telephone}','{nickname}','{password}',CURDATE())",
    "getUserByTel":"select id,password,telephone,regist_date from user where telephone={telephone} limit 1",

    "updateUserById":""
}

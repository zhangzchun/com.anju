
search_sql={
    "getCompanyList":"select c.id,c.name,c.contact_tel,c.case_num,c.work_site_num,c.company_icon, ci.name c_img \
                      from company c,company_img ci where c.id=ci.company_id and c.name like '%{search_content}%'",


    "getStrategyList":"select s.id strategy_id , si.strategy_img , s.strategy_title , sc.lead , s.author \
                        from strategy s inner join strategy_img si INNER JOIN strategy_content sc \
                        on s.id=si.strategy_id and s.id = sc.strategy_id where s.strategy_title like '%{search_content}%'",


    "getDiaryList":"SELECT d.id diary_id ,u.nickname , ui.icon , d.diary_title , s.`name` style_name ,d.company , d.public_date,\
                    dc.diary_content,(SELECT group_concat(di.diary_img) FROM diary_img di WHERE di.diary_content_id = dc.id and dc.diary_id=d.id) diary_img \
                    FROM `user` u INNER JOIN user_icon ui INNER JOIN diary d INNER JOIN style s INNER JOIN renovation_type rt \
                    INNER JOIN diary_content dc on u.user_icon_id=ui.id and d.user_id=u.id and d.style_id=s.id and\
                    d.renovation_type_id=rt.id and d.id=dc.diary_id where dc.stage='前期准备' and d.diary_title like '%{search_content}%'"

}

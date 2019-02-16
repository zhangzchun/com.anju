

diary_sql={

    "getDiaryList":"SELECT d.id diary_id ,u.nickname , ui.icon , d.diary_title , s.`name` style_name ,d.company , d.public_date,\
                    dc.diary_content,(SELECT group_concat(di.diary_img) FROM diary_img di WHERE di.diary_content_id = dc.id && dc.diary_id=d.id) diary_img \
                    FROM `user` u INNER JOIN user_icon ui INNER JOIN diary d INNER JOIN style s INNER JOIN renovation_type rt \
                    INNER JOIN diary_content dc on u.user_icon_id=ui.id  && d.user_id=u.id && d.style_id=s.id &&\
                    d.renovation_type_id=rt.id && d.id=dc.diary_id where dc.stage='前期准备'",

    "getDiaryInfo01":"SELECT d.id,u.nickname , ui.icon user_icon , d.diary_title ,d.public_date,d.area, s.`name` style ,rt.`name` type,\
                    d.village location ,d.company,d.browse_num,d.collect_num,d.comment_num\
                    FROM `user` u INNER JOIN user_icon ui INNER JOIN diary d INNER JOIN style s INNER JOIN \
                    renovation_type rt on u.user_icon_id=ui.id  && d.user_id=u.id && d.style_id=s.id && d.renovation_type_id=rt.id\
                    where d.id={id}",
    "getDiaryInfo02":"select stage, public_date diary_date ,diary_content ,\
                      (SELECT group_concat(di.diary_img) FROM diary_img di WHERE di.diary_content_id = dc.id) diary_img\
                      from diary_content dc where diary_id={id}",
    "writeDiary":""
}

comment_sql={
    "getStrategyComments":"select c.id,c.from_uid, ui.icon, u.nickname, c.comment_content, c.comment_time,c.comment_num\
                            from `comment` c INNER JOIN `user` u INNER JOIN user_icon ui\
                            on c.from_uid=u.id and u.user_icon_id = ui.id \
                            where c.comment_type_id=1 and c.comment_obj_id={strategy_id} order by c.comment_time desc",

    "getDiaryComments":"select c.id,c.from_uid, ui.icon, u.nickname, c.comment_content, c.comment_time,c.comment_num\
                            from `comment` c INNER JOIN `user` u INNER JOIN user_icon ui\
                            on c.from_uid=u.id and u.user_icon_id = ui.id \
                            where c.comment_type_id=2 and c.comment_obj_id={diary_id} order by c.comment_time desc",

    "getReplys":"SELECT r.id,r.from_uid,r.comment_id, ui.icon, u.nickname, r.reply_content, r.reply_time,r.to_unickname \
                    from reply r INNER JOIN `user` u INNER JOIN user_icon ui \
                    on r.from_uid=u.id and u.user_icon_id = ui.id\
                    where r.comment_id={comment_id} order by r.reply_time desc",

    "postComments":"INSERT into `comment`(from_uid,comment_content,comment_time,comment_type_id,comment_obj_id)\
                    VALUES({from_uid},'{comment_content}','{commnet_time}',{comment_type_id},{comment_obj_id})",

    "postReplys":"INSERT into reply(from_uid,comment_id, reply_id, reply_type_id, reply_content, to_uid, \
                  to_unickname,reply_time) VALUES({from_uid}, {comment_id}, {reply_id}, {reply_type_id},\
                  '{reply_content}', {to_uid}, '{to_unickname}','{reply_time}')",
    "postReplys01":"UPDATE `comment` set comment_num = comment_num+1 where id={comment_id}"
}
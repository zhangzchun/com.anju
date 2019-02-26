

case_sql={

    'getCaseList': 'select  `case`.id,`case`.`name`,ht.`name`,rt.`name`,ci.img_url,`case`.area,`case`.price,style.`name` \
                 from `case` inner join case_img ci  INNER JOIN house_type ht INNER JOIN renovation_type rt INNER JOIN designer INNER JOIN style\
                 on `case`.id=ci.case_id and `case`.house_type_id=ht.id and `case`.renovation_type_id=rt.id and designer.id=`case`.designer_id and style.id=`case`.style_id\
                 where  designer.company_id="{company_id}" \
                 GROUP BY `case`.id',


    'screen01': ' select  `case`.id,`case`.`name`,ht.`name`,rt.`name`,ci.img_url,`case`.area,`case`.price,style.`name` \
                from `case` inner join case_img ci  INNER JOIN house_type ht INNER JOIN renovation_type rt INNER JOIN style \
                on `case`.id=ci.case_id and `case`.house_type_id=ht.id and `case`.renovation_type_id=rt.id and style.id=`case`.style_id \
                where ht.`name`= "{ht_name}" or style.`name`="{style_name}" or "{area_min}"<`case`.area  and `case`.area<"{area_max}"\
                GROUP BY `case`.id',


    'screen02': ' select  `case`.id,`case`.`name`,ht.`name`,rt.`name`,ci.img_url,`case`.area,`case`.price,style.`name` \
                from `case` inner join case_img ci  INNER JOIN house_type ht INNER JOIN renovation_type rt INNER JOIN style \
                on `case`.id=ci.case_id and `case`.house_type_id=ht.id and `case`.renovation_type_id=rt.id and style.id=`case`.style_id\
                where (ht.`name`= "{ht_name}" and style.`name`="{style_name}") or (ht.`name`="{ht_name}" and "{area_min}"<`case`.area  and `case`.area<"{area_max}")\
                or (style.`name`="{style_name}" and "{area_min}"<`case`.area  and `case`.area<"{area_max}")\
                GROUP BY `case`.id ',


    'screen03': '  select  `case`.id,`case`.`name`,ht.`name`,rt.`name`,ci.img_url,`case`.area,`case`.price,style.`name` \
                from `case` inner join case_img ci  INNER JOIN house_type ht INNER JOIN renovation_type rt INNER JOIN style \
                on `case`.id=ci.case_id and `case`.house_type_id=ht.id and `case`.renovation_type_id=rt.id and style.id=`case`.style_id\
                where ht.`name`="{ht_name}" and style.`name`="{style_name}" and "{area_min}"<`case`.area  and `case`.area<"{area_max}"\
                GROUP BY `case`.id ',


    'detail':'select `case`.`name`,`case`.area,`case`.price,`case`.village,`case`.date,d.`name` des,c.company_icon,\
                d.icon,d.case_num,s.`name` sty,ht.`name` type,rt.`name` reno,it.img_type,ci.img_url,d.id as designer_id\
                from case_img ci INNER JOIN img_type it INNER JOIN company c INNER JOIN designer d INNER JOIN `case` INNER JOIN style s\
                INNER JOIN house_type ht INNER JOIN renovation_type rt \
                on ci.img_type_id=it.id and d.company_id=c.id and `case`.designer_id=d.id and ci.case_id=`case`.id and `case`.style_id=s.id\
                and `case`.house_type_id=ht.id and `case`.renovation_type_id=rt.id\
                where `case`.id={case_id}'

}
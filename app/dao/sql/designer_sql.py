

designer_sql={

    "getDesignerList": 'select c.id as com_id, d.id as des_id,d.icon as des_icon,\
                      d.`name` as des_name,d.case_num,d.design_concept,d.grade \
                    from 	designer as d inner join company as c on d.company_id=c.id \
                    where company_id={id}',


    "getDesignerDetail": 'select com.id as com_id, com.`name` as com_name, d.icon, d.`name` as des_name,\
                        d.`case_num`, d.personal_profile, d.design_concept, d.grade,\
                        c.id as case_id, ci.img_url, c.`name` as case_name, c.area, \
                        ht.`name` as house_type, s.`name` as style, rt.`name` as rt_type, c.price\
                        from designer as d inner join `case` as c inner join style as s \
                        inner join company as com inner join house_type as ht \
                        inner join case_img as ci inner join renovation_type as rt \
                        on c.designer_id = d.id and c.style_id = s.id and d.company_id = com.id \
                        and c.house_type_id = ht.id and c.id = ci.case_id \
                        and c.renovation_type_id = rt.id where d.id = {id}'


}
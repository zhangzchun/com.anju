

designer_sql={

    "getDesignerList": 'select id,icon, `name`, case_num,design_concept, grade\
                    from designer where company_id={id}',

    "getDesignerDetail": 'select com.`name` as com_name, d.icon, d.`name` as des_name, d.`case_num`, \
                    d.personal_profile,d.design_concept, d.grade, c.id as case_id, c.`name` as case_name, \
                    c.area, ht.`name`, s.`name`, c.price \
                    from designer as d inner join `case` as c inner join style as s \
                    inner join company as com inner join house_type as ht \
                    on c.designer_id = d.id and c.style_id = s.id and d.company_id = com.id \
                    and c.house_type_id=ht.id where d.id = {id}',



}
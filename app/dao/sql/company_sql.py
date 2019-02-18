

company_sql={


    'getCompanyList': 'select c.id,c.name,c.contact_tel,c.case_num,c.work_site_num,c.company_icon, ci.name c_img from company c,company_img ci where c.id=ci.company_id',

    'getIndexCompanyList': 'select c.id,c.name,c.company_icon, ci.name c_img from company c,company_img ci where c.id=ci.company_id limit 8',
    

    'screen01': ' select distinct c.id,c.`name`,c.contact_tel,c.case_num,c.work_site_num,c.company_icon, ci.`name` c_img \
               from company c inner join company_img ci inner join price inner join style inner join company_style cs \
               on c.id=ci.company_id and c.price=price.id and style.id=cs.style_id and c.id=cs.company_id\
               where price.`name`= "{price_name}" or style.`name`="{style_name}" or c.district="{district}" ORDER BY c.id',

    'screen02': ' select distinct c.id,c.`name`,c.contact_tel,c.case_num,c.work_site_num,c.company_icon, ci.`name` c_img \
               from company c inner join company_img ci inner join price inner join style inner join company_style cs \
               on c.id=ci.company_id and c.price=price.id and style.id=cs.style_id and c.id=cs.company_id\
               where (price.`name`= "{price_name}" and style.`name`="{style_name}") or (price.`name`= "{price_name}" and c.district="{district}")\
               or (style.`name`="{style_name}" and c.district="{district}") ORDER BY c.id',

    'screen03': ' select distinct c.id,c.`name`,c.contact_tel,c.case_num,c.work_site_num,c.company_icon, ci.`name` c_img \
               from company c inner join company_img ci inner join price inner join style inner join company_style cs \
               on c.id=ci.company_id and c.price=price.id and style.id=cs.style_id and c.id=cs.company_id\
               where price.`name`= "{price_name}" and style.`name`="{style_name}" and c.district="{district}" ORDER BY c.id',

    'sort01':'select c.id,c.name,c.contact_tel,c.case_num,c.work_site_num,c.company_icon, ci.name c_img from company c,company_img ci \
              where c.id=ci.company_id order by c.id',

    'sort02':'select c.id,c.name,c.contact_tel,c.case_num,c.work_site_num,c.company_icon, ci.name c_img from company c,company_img ci \
              where c.id=ci.company_id order by c.case_num DESC',

    'sort03':'select c.id,c.name,c.contact_tel,c.case_num,c.work_site_num,c.company_icon, ci.name c_img from company c,company_img ci \
              where c.id=ci.company_id order by c.work_site_num DESC',

    'sort04':'select c.id,c.name,c.contact_tel,c.case_num,c.work_site_num,c.company_icon, ci.name c_img from company c,company_img ci \
              where c.id=ci.company_id order by c.favorable_rate DESC',
    

    "getCompanyDetail":'select company_img.`name` as com_img, c.`name` as com_name, c.bond, c.mouth_value, c.case_num, c.work_site_num, c.favorable_rate, c.contact_tel, c.district, c.address,c.company_icon,\
                        `case`.id as case_id, ci.img_url as case_img, `case`.`name` as case_name, `case`.area, `case`.price, ht.`name` type, s.`name` sty,rt.`name` as reno, \
                        d.id as des_id, d.`name` des, d.case_num as case_number, d.icon des_icon\
                        from case_img ci  INNER JOIN company c INNER JOIN designer d INNER JOIN `case` INNER JOIN style s\
                        INNER JOIN house_type ht INNER JOIN renovation_type rt INNER JOIN company_img\
                        on  d.company_id=c.id and `case`.designer_id=d.id and ci.case_id=`case`.id and `case`.style_id=s.id\
                        and `case`.house_type_id=ht.id and `case`.renovation_type_id=rt.id and c.id = company_img.company_id\
                        where c.id={id}\
                        GROUP BY des  limit 6 '
    
    


}
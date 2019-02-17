

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
    
    
    
    
    "getCompanyDetail":"select name, contact_tel, district, address, case_num, work_site_num, favorable_rate, bond, mouth_value,company_icon from company where id={id}",
}

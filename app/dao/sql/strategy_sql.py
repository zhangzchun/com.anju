


strategy_sql={
    "getStrategyList":"select s.id strategy_id , si.strategy_img , s.strategy_title , sc.lead , s.author \
                        from strategy s inner join strategy_img si INNER JOIN strategy_content sc \
                        on s.id=si.strategy_id && s.id = sc.strategy_id",
    "getStrategyDetail":"select s.strategy_title, s.public_date, s.author, sc.lead ,sc.strategy_content\
                        from strategy s inner join strategy_img si INNER JOIN strategy_content sc \
                        on s.id=si.strategy_id && s.id = sc.strategy_id where s.id={id}"

}
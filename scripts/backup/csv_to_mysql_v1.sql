USE stock;
LOAD DATA LOCAL infile 'G:\\stock\\data_to_sql_owner\\data_combine.csv_tr.csv'
into table owner_liutong
fields terminated by ',' optionally enclosed by '"' escaped by '"'  
lines terminated by '\r\n';  




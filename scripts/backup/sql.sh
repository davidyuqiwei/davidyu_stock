--mysql -h localhost -u root -p1988david < G:\stock\code_python3\download_data\owner_liutong\csv_to_mysql_v1.sql
select count(*) from test;

select distinct * from tableName

select distinct * into #tmp from owner_liutong
drop table owner_liutong
select * into owner_liutong from tmp
drop table tmp;


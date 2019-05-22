LOAD DATA LOCAL infile 'G:\\stock\\shenzhen\\000001_2014-08-15.csv'
into table test
fields terminated by ',' optionally enclosed by '"' escaped by '"'  
lines terminated by '\r\n';  

#mysql -h localhost -u root -p1988david < G:\stock\shenzhen\csv_to_mysql.sql


## generate stockid from the fuquan (test) table
CREATE TABLE IF NOT EXISTS `stockid`(
`stockid` INT NOT NULL
)ENGINE=InnoDB;

insert into stockid
select distinct stockid from test2;
select * from stockid limit 2;

truncate table stockid;

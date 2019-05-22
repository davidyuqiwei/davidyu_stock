CREATE DATABASE IF NOT EXISTS stock;
use stock;
CREATE TABLE IF NOT EXISTS `owner_liutong`(
`Amount` BIGINT NOT NULL,
`Date` DATE NOT NULL,
`Owner` VARCHAR(100) NOT NULL,
`Ratio` FLOAT NOT NULL,
`Id` INT NOT NULL,
primary key(Amount,Date,Owner,Ratio,Id)
)ENGINE=InnoDB DEFAULT CHARSET=utf8;

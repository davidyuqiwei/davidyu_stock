
yum -y install mariadb*

【安装的版本是5.5.56-MariaDB】

启动mysql

shell>mysql

但是会出现问题

Can't connect to local MySQL server through socket '/var/lib/mysql/mysql.sock' (2）

所以需要配置以下内容

配置启动

systemctl start mariadb.service

配置开机自动启动

systemctl enable mariadb.service

配置好了进入mariadb

mysql -u root -p 然后空格

给root用户全部权限

mysql>grant all on *.* to root@'localhost' identified by 'root'

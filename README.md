

start mysql container
docker run --name mariadb  -v  /mysql_data:/var/lib/mysql   -e MYSQL_ROOT_PASSWORD=mypass -p 3306:3306 -d mariadb:10.4
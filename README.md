# Containers
Docker compose platform for using Postgres backend to SAS

This docker compose cluster is configured to set up 
1) SAS Viya 3.5
2) Python 3.8 with Jupyter, SASPY and SWAT
3) RStudio Version 1.3.1056 running R version 4.0.2 (2020-06-22) -- "Taking Off Again"
4) Postgres (PostgreSQL) 13.1 (Debian 13.1-1.pgdg100+1)
  a) psql (13.1 (Debian 13.1-1.pgdg100+1))

The addendum directory contains the tar file with the DVD rental database and the accompanying ER diagram.
Additionally, the Postgres DVD Rental database can be downloaded from here:
https://www.postgresqltutorial.com/postgresql-sample-database/

Steps to Install:
0)  Sign into the vpn so Jacob's container can be pulled

1)	Clone the repository https://github.com/scoyote/sas_postgres

2)	Set PLPATH to a permanent path 

3)	Run ```docker-compose build```

4)	Run ```docker-compose up```, look for the following from the postgres container: 
    ```postgres-sas  | 2020-12-11 17:18:00.664 UTC [1] LOG:  database system is ready to accept connection```
   
5)  Normally start up using ```docker-compose up -d```
6)  Normally shut down using ```docker-compose down```

Ports: 
  8081 - SAS Studio V
  
  8787 - RStudio
  
  8888 - Jupyter Hub
  
  5432 - Postgres
  
  
  
# Loading the DVD Rental database (tar downloaded in build process):

```
$ docker exec -it postgres-sas /bin/bash
 
  postgres-# \l
                                 List of databases
   Name    |  Owner   | Encoding |  Collate   |   Ctype    |   Access privileges   
-----------+----------+----------+------------+------------+-----------------------
 postgres  | postgres | UTF8     | en_US.utf8 | en_US.utf8 | 
 template0 | postgres | UTF8     | en_US.utf8 | en_US.utf8 | =c/postgres          +
           |          |          |            |            | postgres=CTc/postgres
 template1 | postgres | UTF8     | en_US.utf8 | en_US.utf8 | =c/postgres          +
           |          |          |            |            | postgres=CTc/postgres
(3 rows)

postgres-# exit;
Use \q to quit.
postgres=# exit;
postgres@xxx:/$ createdb dvdrental
postgres@xxx:/$ psql 
psql (13.1 (Debian 13.1-1.pgdg100+1))
Type "help" for help.

postgres=# \l
                                 List of databases
   Name    |  Owner   | Encoding |  Collate   |   Ctype    |   Access privileges   
-----------+----------+----------+------------+------------+-----------------------
 dvdrental | postgres | UTF8     | en_US.utf8 | en_US.utf8 | 
 postgres  | postgres | UTF8     | en_US.utf8 | en_US.utf8 | 
 template0 | postgres | UTF8     | en_US.utf8 | en_US.utf8 | =c/postgres          +
           |          |          |            |            | postgres=CTc/postgres
 template1 | postgres | UTF8     | en_US.utf8 | en_US.utf8 | =c/postgres          +
           |          |          |            |            | postgres=CTc/postgres
(4 rows)

postgres=# \c dvdrental
You are now connected to database "dvdrental" as user "postgres".
dvdrental=# \dt
Did not find any relations.
dvdrental=# exit;
postgres@xxx:/$ pg_restore -U postgres -d dvdrental dvdrental.tar
postgres@xxx:/$ psql
psql (13.1 (Debian 13.1-1.pgdg100+1))
Type "help" for help.

postgres=# \l
                                 List of databases
   Name    |  Owner   | Encoding |  Collate   |   Ctype    |   Access privileges   
-----------+----------+----------+------------+------------+-----------------------
 dvdrental | postgres | UTF8     | en_US.utf8 | en_US.utf8 | 
 postgres  | postgres | UTF8     | en_US.utf8 | en_US.utf8 | 
 template0 | postgres | UTF8     | en_US.utf8 | en_US.utf8 | =c/postgres          +
           |          |          |            |            | postgres=CTc/postgres
 template1 | postgres | UTF8     | en_US.utf8 | en_US.utf8 | =c/postgres          +
           |          |          |            |            | postgres=CTc/postgres
(4 rows)

postgres=# \c dvdrental
You are now connected to database "dvdrental" as user "postgres".
dvdrental=# \dt
             List of relations
 Schema |     Name      | Type  |  Owner   
--------+---------------+-------+----------
 public | actor         | table | postgres
 public | address       | table | postgres
 public | category      | table | postgres
 public | city          | table | postgres
 public | country       | table | postgres
 public | customer      | table | postgres
 public | film          | table | postgres
 public | film_actor    | table | postgres
 public | film_category | table | postgres
 public | inventory     | table | postgres
 public | language      | table | postgres
 public | payment       | table | postgres
 public | rental        | table | postgres
 public | staff         | table | postgres
 public | store         | table | postgres
(15 rows)

dvdrental=# select * from actor limit 2;
 actor_id | first_name | last_name |      last_update       
----------+------------+-----------+------------------------
        1 | Penelope   | Guiness   | 2013-05-26 14:47:57.62
        2 | Nick       | Wahlberg  | 2013-05-26 14:47:57.62
(2 rows)

dvdrental=# exit;
```

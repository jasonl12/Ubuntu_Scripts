-- sudo -u postgres psql < get_db_size.sql

SELECT pg_database.datname AS "databasename",
pg_database_size(pg_database.datname)/1024/1024 AS sizemb
FROM pg_database ORDER BY pg_database_size(pg_database.datname) DESC;

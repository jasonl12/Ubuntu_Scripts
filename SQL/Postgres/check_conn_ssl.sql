-- sudo -u postgres psql -c 'SELECT * FROM pg_stat_ssl;'
-- sudo -u postgres psql < check_conn_ssl.sql

SELECT pg_ssl.pid, pg_ssl.ssl, pg_ssl.version,
pg_sa.backend_type, pg_sa.usename, pg_sa.client_addr
FROM pg_stat_ssl pg_ssl JOIN pg_stat_activity pg_sa
ON pg_ssl.pid = pg_sa.pid;

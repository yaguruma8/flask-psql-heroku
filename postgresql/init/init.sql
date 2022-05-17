CREATE DATABASE flasknote;
ALTER DATABASE flasknote SET timezone TO 'Asia/Tokyo';
SELECT * FROM pg_reload_conf();
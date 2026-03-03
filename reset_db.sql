-- Run this to reset the database for the custom user model.
-- 1. Stop runserver (Ctrl+C) and any other app using the DB.
-- 2. From terminal: psql -U apple -d postgres -h localhost -f reset_db.sql
-- 3. Then: python manage.py migrate

SELECT pg_terminate_backend(pid)
FROM pg_stat_activity
WHERE datname = 'bugtracker_db' AND pid <> pg_backend_pid();

DROP DATABASE IF EXISTS bugtracker_db;
CREATE DATABASE bugtracker_db;

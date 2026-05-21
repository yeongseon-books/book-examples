CREATE TABLE _alembic_tmp_users (...);   -- temp table with the new schema
INSERT INTO _alembic_tmp_users SELECT ... FROM users;
DROP TABLE users;
ALTER TABLE _alembic_tmp_users RENAME TO users;
-- recreate the original indexes/triggers

CREATE DATABASE IF NOT EXISTS notifications;

CREATE TABLE IF NOT EXISTS notifications.notifications
(
    id          VARCHAR(36),
    user_id     VARCHAR(36),
    message     VARCHAR(255),
    is_read     BOOLEAN,
    created_at  DATETIME,
    PRIMARY KEY (id)
);

CREATE USER IF NOT EXISTS app@'%' IDENTIFIED BY 'pass';

GRANT INSERT, DELETE, SELECT, UPDATE ON notifications.* TO 'app'@'%';

flush privileges;
CREATE TABLE tasks (
    id VARCHAR(36) PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    status VARCHAR(16) NOT NULL,
    due_date DATETIME
);
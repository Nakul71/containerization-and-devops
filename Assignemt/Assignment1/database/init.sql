-- init.sql
-- Initialization script for PostgreSQL database
-- This runs automatically on first container startup

-- Create the students table
CREATE TABLE IF NOT EXISTS students (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(150) NOT NULL UNIQUE,
    course VARCHAR(100) NOT NULL
);

-- Insert sample seed data
INSERT INTO students (name, email, course) VALUES
    ('Nakul', 'nakul@example.com', 'DevOps'),
    ('Amit', 'amit@example.com', 'Cloud Computing')
ON CONFLICT (email) DO NOTHING;

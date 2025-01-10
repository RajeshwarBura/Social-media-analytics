-- Create the database (if not already created)
CREATE DATABASE IF NOT EXISTS social_media_analytics;

-- Use the created database
USE social_media_analytics;

-- Create a table for storing engagement data
CREATE TABLE IF NOT EXISTS engagement_data (
    post_id UUID PRIMARY KEY,
    post_type VARCHAR(255),
    likes INT,
    shares INT,
    comments INT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Insert sample engagement data
INSERT INTO engagement_data (post_id, post_type, likes, shares, comments) 
VALUES
    (uuid(), 'carousel', 120, 30, 25),
    (uuid(), 'reels', 200, 50, 45),
    (uuid(), 'static image', 75, 20, 15),
    (uuid(), 'carousel', 150, 40, 35),
    (uuid(), 'reels', 250, 60, 55),
    (uuid(), 'static image', 85, 25, 20),
    (uuid(), 'carousel', 100, 28, 22),
    (uuid(), 'reels', 180, 45, 40);

-- Create an index on the post_type column for better query performance
CREATE INDEX IF NOT EXISTS post_type_idx ON engagement_data (post_type);

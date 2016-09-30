-- Table definitions for the tournament project.
-- Since we are using this file to repeatedly refine our schema we will DROP the
-- database or any table and recreate it each time this file is run.


-- Create the tournament database and connect to it
DROP DATABASE IF EXISTS tournament;
CREATE DATABASE tournament;
\c tournament;

-- Create the players table
CREATE TABLE players (
    id SERIAL PRIMARY KEY,
    name TEXT);

-- Create the matches table
CREATE TABLE matches (
    id SERIAL,
    winner_id INTEGER REFERENCES players (id),
    loser_id INTEGER REFERENCES players (id));

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

-- Create a view to show the current standings.  All registered players must be
-- in the standings regardless of whether any matches have been played
CREATE OR REPLACE VIEW standings (id, name, wins, played) AS 
SELECT players.id, players.name,
    SUM (CASE WHEN players.id = matches.winner_id then 1 else 0 end) as wins,
    COUNT(matches.id) as played
    FROM players
    LEFT JOIN matches ON
    players.id IN (matches.winner_id, matches.loser_id)
    GROUP BY players.id
    ORDER BY wins DESC;


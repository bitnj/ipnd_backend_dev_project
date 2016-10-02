# ipnd_backend_dev_project

Author - Neil Seas (2016)

This project implements a simple **Swiss style** tournament using **Python** and
**PostgreSQL** per the specification of the Udacity Back-End Dev Nanodegree.  A
PDF of the specification is included in this repository
(P2TournamentResults-GettingStarted.pdf).

## Files
1. tournament.sql
    * creates the tournament database and connects
    * defines two tables **players** and **matches**
    * defines the view standings which shows an ordered list (by wins) for all
      registered players
2. tournament.py
    * contains all of the functions defined by the project specification
    * connect
        * returns a connection to the tournament database
    * deleteMatches
        * deletes all rows from the matches table
    * deletePlayers
        * deletes all players from the players table
    * countPlayers
        * returns the number of registered players in the players table
    * registerPlayer
        * adds a player (by name) to the players table
    * playerStandings
        * uses the standings view and shows all registered players, the number
          of wins, and the number of matches played
    * reportMatch
        * adds a record to the matches table based on the provided arguments
    * swissPairings
        * a simple algorithm for generating pairs of players for the next round
          of matches based on number of wins.  Assumes even numbers of players
          and ignores the possibility of rematches.
3. tournament_test.py
    * a file that runs unit tests against the tournament database and
      tournament.py functions

## Running the project
1. import the tournament.sql file into PostgreSQL
2. from the same directory run the tournament_test.py


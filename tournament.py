#!/usr/bin/env python
# 
# tournament.py -- implementation of a Swiss-system tournament
#

import psycopg2
from contextlib import contextmanager

def connect():
    """Connect to the PostgreSQL database.  Returns a database connection."""
    try:
        return psycopg2.connect("dbname=tournament")
    except:
        # per Udacity reviewer it's generally not good practice to exclude the
        # exception but in this case not terrible
        print('Connection Failed')

@contextmanager
def get_cursor():
    """Helper function that creates a cursor from a database connection object,
    and performs queries using that cursor.  Implemented based on reviewer
    feedback"""
    DB = connect()
    cursor = DB.cursor()
    try:
        yield cursor
    except:
        raise
    else:
        DB.commit()
    finally:
        cursor.close()
        DB.close()


def deleteMatches():
    """Remove all the match records from the database."""
    with get_cursor() as cursor:
        cursor.execute('DELETE FROM matches;')


def deletePlayers():
    """Remove all the player records from the database."""
    with get_cursor() as cursor:
        cursor.execute('DELETE FROM players;')


def countPlayers():
    """Returns the number of players currently registered."""
    # use coalesce to transform NULL into 0 in the case of no records in the
    # players table
    with get_cursor() as cursor:
        cursor.execute('SELECT COALESCE((SELECT COUNT(*) FROM players), 0);')
        # aggregate query so we are expecting only 1 result row
        numPlayers = cursor.fetchone()
    
    return numPlayers[0]


def registerPlayer(name):
    """Adds a player to the tournament database.
  
    The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)
  
    Args:
      name: the player's full name (need not be unique).
    """
    with get_cursor() as cursor:
        # ID is type SERIAL so just need to insert the name
        cursor.execute('INSERT INTO players (name) VALUES(%s);', (name,))


def playerStandings():
    """Returns a list of the players and their win records, sorted by wins.

    The first entry in the list should be the player in first place, or a player
    tied for first place if there is currently a tie.

    Returns:
      A list of tuples, each of which contains (id, name, wins, matches):
        id: the player's unique id (assigned by the database)
        name: the player's full name (as registered)
        wins: the number of matches the player has won
        matches: the number of matches the player has played
    """
    with get_cursor() as cursor:
        # retrieve the records from the VIEW standings
        cursor.execute('SELECT * FROM standings;')
        standings = cursor.fetchall()
    
    return standings
    

def reportMatch(winner, loser):
    """Records the outcome of a single match between two players.

    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """
    with get_cursor() as cursor:
        # insert the winner and loser ids into the matches table
        cursor.execute('INSERT INTO matches (winner_id, loser_id) VALUES(%s, %s);', (winner, loser))
 
 
def swissPairings():
    """Returns a list of pairs of players for the next round of a match.
  
    Assuming that there are an even number of players registered, each player
    appears exactly once in the pairings.  Each player is paired with another
    player with an equal or nearly-equal win record, that is, a player adjacent
    to him or her in the standings.
  
    Returns:
      A list of tuples, each of which contains (id1, name1, id2, name2)
        id1: the first player's unique id
        name1: the first player's name
        id2: the second player's unique id
        name2: the second player's name
    """
    # first get the standings VIEW
    standings = playerStandings()
    
    # get the id and name of each player in the standings
    players = [player_info[0:2] for player_info in standings]
    # init pairings list
    pairings = []
    # loop through the players in 2s and add the player info for adjacent
    # players into a tuple
    for i in range(0, len(standings) - 1, 2):
        pair = (players[i] + players[i+1])
        pairings.append(pair)
    return pairings


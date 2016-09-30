#!/usr/bin/env python
# 
# tournament.py -- implementation of a Swiss-system tournament
#

import psycopg2


def connect():
    """Connect to the PostgreSQL database.  Returns a database connection."""
    return psycopg2.connect("dbname=tournament")


def deleteMatches():
    """Remove all the match records from the database."""
    # connect to the database and get a cursor
    dbCon = connect()
    cursor = dbCon.cursor()

    cursor.execute('DELETE FROM matches;')
    dbCon.commit()
    dbCon.close()

def deletePlayers():
    """Remove all the player records from the database."""
    # connect to the database and get a cursor
    dbCon = connect()
    cursor = dbCon.cursor()

    cursor.execute('DELETE FROM players;')
    dbCon.commit()
    dbCon.close()


def countPlayers():
    """Returns the number of players currently registered."""
    # connect to the database and get a cursor
    dbCon = connect()
    cursor = dbCon.cursor()

    # connect to the database and get a cursor
    dbCon = connect()
    cursor = dbCon.cursor()
    # use coalesce to transform NULL into 0 in the case of no records in the
    # players table
    cursor.execute('SELECT COALESCE((SELECT COUNT(*) FROM players), 0);')
    # aggregate query so we are expecting only 1 result row
    numPlayers = cursor.fetchone()
    dbCon.close()
    
    return numPlayers[0]


def registerPlayer(name):
    """Adds a player to the tournament database.
  
    The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)
  
    Args:
      name: the player's full name (need not be unique).
    """
    # connect to the database and get a cursor
    dbCon = connect()
    cursor = dbCon.cursor()

    # connect to the database and get a cursor
    dbCon = connect()
    cursor = dbCon.cursor()

    # ID is type SERIAL so just need to insert the name
    cursor.execute('INSERT INTO players (name) VALUES(%s);', (name,))
    dbCon.commit()
    dbCon.close()

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
    # connect to the database and get a cursor
    dbCon = connect()
    cursor = dbCon.cursor()

    # retrieve the records from the VIEW standings
    cursor.execute('SELECT * FROM standings;')
    standings = cursor.fetchall()
    dbCon.close()
    print(standings)
    return standings
    


def reportMatch(winner, loser):
    """Records the outcome of a single match between two players.

    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """
 
 
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



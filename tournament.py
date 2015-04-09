#!/usr/bin/env python
# 
# tournament.py -- implementation of a Swiss-system tournament
#

import psycopg2
import bleach

def connect():
    """Connect to the PostgreSQL database.  Returns a database connection."""
    return psycopg2.connect("dbname=tournament")


def deleteMatches():
    """Remove all the match records from the database."""
    db = connect()
    c = db.cursor()
    c.execute("DELETE FROM matches")
    db.commit()
    db.close()

def deletePlayers():
    """Remove all the player records from the database."""
    db = connect()
    c = db.cursor()
    c.execute("DELETE FROM players")
    db.commit()
    db.close()

def countPlayers():
    """Returns the number of players currently registered."""
    db = connect()
    c = db.cursor()
    c.execute("SELECT count(*) FROM players")
    count = c.fetchone()
    count = count[0]
    db.close()
    return count

def registerPlayer(name):
    """Adds a player to the tournament database.
    
    The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)
  
    Args:
      name: the player's full name (need not be unique).
    """
    newplayer = bleach.clean(name, strip=True)
    db = connect()
    c = db.cursor()
    c.execute("INSERT INTO players (name) VALUES (%s)", (newplayer,))
    db.commit()
    db.close()

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
    db = connect()
    c = db.cursor()
    #c.execute("SELECT players.ID, players.name, count(matches.winner) as wins, count(matches.id) as matches FROM players left join matches ON players.ID = matches.player1 OR players.ID = matches.player2 GROUP BY players.ID ORDER BY wins DESC")
    c.execute("SELECT players.ID, players.name, sum(case when matches.winner = players.ID then 1 else 0 end) as wins, count(matches.id) as matches FROM players left join matches ON players.ID = matches.player1 OR players.ID = matches.player2 GROUP BY players.ID ORDER BY wins DESC")
    standings = c.fetchall()
    db.close()
    return standings

def reportMatch(winner, loser):
    """Records the outcome of a single match between two players.

    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """
    winner = bleach.clean(winner, strip=True)
    loser = bleach.clean(loser, strip=True)
    db = connect()
    c = db.cursor()
    c.execute("INSERT INTO matches (player1, player2, winner, loser) VALUES (%s, %s, %s, %s)", (winner, loser, winner, loser,))
    db.commit()
    db.close()
 
 
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
    pairing = []
    db = connect()
    c = db.cursor()
    c.execute("SELECT players.ID, players.name, sum(case when matches.winner = players.ID then 1 else 0 end) as wins, count(matches.id) as matches FROM players left join matches ON players.ID = matches.player1 OR players.ID = matches.player2 GROUP BY players.ID ORDER BY wins DESC")
    standings = c.fetchall()
    x = 0
    while x < len(standings):
        pairing.extend([(standings[x][0], standings[x][1], standings[x+1][0], standings[x+1][1])])
        x = x+2
    db.close()
    return pairing    



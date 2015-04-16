-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.

CREATE TABLE IF NOT EXISTS players (
    ID      serial          PRIMARY KEY,
    name    varchar(100)    NOT NULL
);

CREATE TABLE IF NOT EXISTS matches (
    ID      serial          PRIMARY KEY,
    player1 integer,
    player2 integer,
    winner  integer,
    loser   integer
);

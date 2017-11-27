#!env/bin/python

import media
import fresh_tomatoes

#CREATING 6 MOVIE OBJECTS BY INSTANTIATING THE movie class 
# PASSING IN ODER Movie Name - String, Movie Description - String, FULL LINK TO MOVIE POSTER - String, FULL LINK TO TRAILER ON YOUTUBE - String
PulpFiction = media.Movie('Pulp Fiction', 
                            'Series of unfortunate events surrouding a suitcase and a bunch of low rent hitmen',
                            'https://upload.wikimedia.org/wikipedia/en/3/3b/Pulp_Fiction_%281994%29_poster.jpg' , 
                            'https://youtu.be/s7EdQ4FqbhY')

Goodfellas = media.Movie('Goodfellas',
                          'A true story of a mobster in New York in the 1990s', 
                          'https://upload.wikimedia.org/wikipedia/en/7/7b/Goodfellas.jpg',
                          'https://www.youtube.com/watch?v=qo5jJpHtI1Y')

SchoolOfRock = media.Movie('The School Of Rock',
                              'A loser impersonates his friend as a substitute at a prep school to take part in a rock competition', 
                              'https://upload.wikimedia.org/wikipedia/en/1/11/School_of_Rock_Poster.jpg', 
                              'https://www.youtube.com/watch?v=3PsUJFEBC74')

Incredibles = media.Movie('The Incredibles', 
                           'A Super hero family go into witness protection, only to return to save the world',
                           'https://upload.wikimedia.org/wikipedia/en/e/ec/The_Incredibles.jpg','https://www.youtube.com/watch?v=eZbzbC9285I')

Godfather = media.Movie('The Godfather',
                         'A story Italian American Mafia Family set in the 1940s', 
                         'https://upload.wikimedia.org/wikipedia/en/1/1c/Godfather_ver1.jpg',
                         'https://www.youtube.com/watch?v=sY1S34973zA')

FightClub = media.Movie('Fight Club', 
                          'An amnesiac and his friend start a violent club that moves out of the basement', 
                          'https://upload.wikimedia.org/wikipedia/en/f/fc/Fight_Club_poster.jpg',
                          'https://www.youtube.com/watch?v=SUXWAEX2jlg')

#LOADING EACH CLASS INTO A LIST
_movies = [PulpFiction, Goodfellas, SchoolOfRock, Incredibles, Godfather, FightClub]
#PASSING LIST TO fresh_tomatoes.open_movies_page 
fresh_tomatoes.open_movies_page(_movies)

# Graph-Based Movie Recommendation System

## Overview
This project implements a graph-based movie recommender system using the MovieLens dataset.

Users and movies are represented as nodes in a graph. 
Edges connect users to movies they have rated.

The system computes user similarity using Jaccard similarity 
and recommends movies based on similar users.

## Technologies Used
- Python
- NetworkX
- Graph Theory

## Details of Dataset
u.data     -- The full u data set, 100000 ratings by 943 users on 1682 items.
              Each user has rated at least 20 movies.  Users and items are
              numbered consecutively from 1.  The data is randomly
              ordered. This is a tab separated list of 
	         user id | item id | rating | timestamp. 
              The time stamps are unix seconds since 1/1/1970 UTC   

u.info     -- The number of users, items, and ratings in the u data set.

u.item     -- Information about the items (movies); this is a tab separated
              list of
              movie id | movie title | release date | video release date |
              IMDb URL | unknown | Action | Adventure | Animation |
              Children's | Comedy | Crime | Documentary | Drama | Fantasy |
              Film-Noir | Horror | Musical | Mystery | Romance | Sci-Fi |
              Thriller | War | Western |
              The last 19 fields are the genres, a 1 indicates the movie
              is of that genre, a 0 indicates it is not; movies can be in
              several genres at once.
              The movie ids are the ones used in the u.data data set.

              
## Dataset
MovieLens 100K dataset:
- 943 users
- 1682 movies
- 100,000 ratings

## How to Run

Install dependency:

pip install networkx

Run the program:

python graph_recommender.py
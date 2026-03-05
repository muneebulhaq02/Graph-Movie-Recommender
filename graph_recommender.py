"""
Graph-Based Movie Recommendation System

This program builds a bipartite graph of users and movies using
the MovieLens dataset. It calculates user similarity using
Jaccard similarity and recommends movies based on similar users.

"""

import networkx as nx

RATINGS_FILE = "data/u.data"
MOVIES_FILE = "data/u.item"
TOP_K = 10


def load_movie_titles(path):  # Load movie titles from the MovieLens dataset
    movie_titles = {}

    file = open(path, "r", encoding="latin-1")
    for line in file:
        parts = line.split("|")
        movie_id = parts[0]
        title = parts[1]
        movie_titles[movie_id] = title
    file.close()

    return movie_titles

# Build a graph where users and movies are nodes
# An edge means the user rated the movie
def build_graph(ratings_path, movie_titles):  
    G = nx.Graph()

    file = open(ratings_path, "r")
    for line in file:
        u, m,r,t = line.split()

        user = "U" + u
        movie = movie_titles[m]

        G.add_edge(user, movie)

    file.close()
    return G

# Calculate similarity between two users using Jaccard similarity
def jaccard_similarity(G, u1, u2):

    movies1 = set(G.neighbors(u1))
    movies2 = set(G.neighbors(u2))

    union = movies1 | movies2

    if (len(union)== 0):
        return 0

    return len(movies1 & movies2) / len(union)

# Recommend movies to a user based on similar users
def recommend(G, user_id, top_k):

    user = "U" + str(user_id)
    user_movies = set(G.neighbors(user))

    similarities = {}

    for node in G.nodes():
        if (str(node).startswith("U") and node != user):
            similarities[node] = jaccard_similarity(G, user, node)

    scores = {}

    for node in G.nodes():

        if (not str(node).startswith("U") and node not in user_movies):

            score = 0

            for watcher in G.neighbors(node):
                score = score + similarities.get(watcher, 0)

            if (score > 0):
                scores[node] = score

    result = sorted(scores.items(), key=lambda x: x[1], reverse=True)

    return result[:top_k]


if __name__ == "__main__":

    print("Loading movie titles...")
    movie_titles = load_movie_titles(MOVIES_FILE)

    print("Building graph...")
    G = build_graph(RATINGS_FILE, movie_titles)

    user_list = [1, 10, 50, 100]

    for uid in user_list:

        print("\nTop", TOP_K, "recommendations for User", uid)

        recs = recommend(G, uid, TOP_K)

        if (len(recs) == 0):
            print("No recommendations found.")
        else:
            i = 1
            for movie, score in recs:
                print(i, ".", movie, "(score =", round(score, 4), ")")
                i+=1
"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

from recommender import load_songs, recommend_songs

def main() -> None:
    songs = load_songs("data/songs.csv") 

    # 1. UPDATED KEYS: These now match what score_song is looking for
    # user_prefs = {
    #     "favorite_genre": "Pop", 
    #     "favorite_mood": "Happy", 
    #     "target_energy": 0.85
    # }
# # Test 1: High-Energy Pop
    user_prefs = {"favorite_genre": "pop", "favorite_mood": "happy", "target_energy": 0.85}

# Test 2: Chill Lofi


    # user_prefs = {
    #     "favorite_genre": "Electronic", 
    #     "favorite_mood": "Chill", 
    #     "target_energy": 0.3
    # }

# Test 3: The Adversarial/Conflicting Profile (Sad but High Energy)


    # user_prefs = {
    #     "favorite_genre": "Rock", 
    #     "favorite_mood": "Sad", 
    #     "target_energy": 0.95
    # }

    recommendations = recommend_songs(user_prefs, songs, k=5)

    # 2. UPDATED PRINTING
    print("\n TOP RECOMMENDATIONS \n")
    
    for index, (song, score, explanation) in enumerate(recommendations, start=1):
        print(f"{index}. {song['title']} (by {song['artist']})")
        print(f" Score: {score:.2f}")
        print(f"  Why: {explanation}")


if __name__ == "__main__":
    main()

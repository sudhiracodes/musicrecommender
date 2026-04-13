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
    user_prefs = {
        "favorite_genre": "Pop", 
        "favorite_mood": "Happy", 
        "target_energy": 0.85
    }

    recommendations = recommend_songs(user_prefs, songs, k=5)

    # 2. UPDATED PRINTING: This is the clean CLI layout for your screenshot
    print("\n TOP RECOMMENDATIONS \n")
    
    for index, (song, score, explanation) in enumerate(recommendations, start=1):
        print(f"{index}. {song['title']} (by {song['artist']})")
        print(f" Score: {score:.2f}")
        print(f"  Why: {explanation}")


if __name__ == "__main__":
    main()

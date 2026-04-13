from typing import List, Dict, Tuple, Optional
from dataclasses import dataclass
import csv


@dataclass
class Song:
    """
    Represents a song and its attributes.
    Required by tests/test_recommender.py
    """
    id: int
    title: str
    artist: str
    genre: str
    mood: str
    energy: float
    tempo_bpm: float
    valence: float
    danceability: float
    acousticness: float

@dataclass
class UserProfile:
    """
    Represents a user's taste preferences.
    Required by tests/test_recommender.py
    """
    favorite_genre: str
    favorite_mood: str
    target_energy: float
    likes_acoustic: bool

class Recommender:
    """
    OOP implementation of the recommendation logic.
    Required by tests/test_recommender.py
    """
    def __init__(self, songs: List[Song]):
        self.songs = songs

    def recommend(self, user: UserProfile, k: int = 5) -> List[Song]:
        """
        Scores all songs based on the user profile and returns the top k Song objects.
        """
        scored_songs = []
        
        for song in self.songs:
            score = 0.0
            
            # 1. Genre Match
            if user.favorite_genre == song.genre:
                score += 2.0
                # score += 1.0
            
            # 2. Mood Match
            if user.favorite_mood == song.mood:
                score += 1.0
                
            # 3. Energy Proximity
            energy_score = 1.0 - abs(user.target_energy - song.energy)
            # energy_score = 1.0 - abs(user.target_energy - song.energy)*2.0
            score += energy_score
            
            scored_songs.append((song, score))
            
        # Sort by score (index 1 of the tuple) in descending order
        ranked_songs = sorted(scored_songs, key=lambda x: x[1], reverse=True)
        
        # Extract and return ONLY the Song objects for the top k results
        return [item[0] for item in ranked_songs[:k]]

    def explain_recommendation(self, user: UserProfile, song: Song) -> str:
        """
        Generates the explanation string for a specific song and user profile.
        """
        reasons = []
        
        if user.favorite_genre == song.genre:
            reasons.append("Genre match (+1.0)")
            
        if user.favorite_mood == song.mood:
            reasons.append("Mood match (+1.0)")
            
        energy_score = 1.0 - abs(user.target_energy - song.energy)
        reasons.append(f"Energy match (+{energy_score:.2f})")
        
        return ", ".join(reasons)

def load_songs(csv_path: str) -> List[Dict]:
    """
    Loads songs from a CSV file.
    Required by src/main.py
    """
    # TODO: Implement CSV loading logic
    print(f"Loading songs from {csv_path}...")
    songs = []
    
    try:
        with open(csv_path, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            
            # 1. Grab the column names dynamically!
            columns = reader.fieldnames
            print(f"Detected columns: {columns}")
            
            for row in reader:
                parsed_song = {}
                
                # 2. Loop through whatever columns were found
                for col in columns:
                    raw_value = row[col]
                    
                    # 3. Try to convert everything to a number if possible
                    try:
                        # If it has a decimal, make it a float
                        if '.' in raw_value:
                            parsed_song[col] = float(raw_value)
                        # Otherwise, make it an integer
                        else:
                            parsed_song[col] = int(raw_value)
                    except ValueError:
                        # If the math breaks (e.g., the word "Pop"), keep it as a string
                        parsed_song[col] = raw_value
                        
                songs.append(parsed_song)
        # Dynamically print the total number of songs loaded
        print(f"Loaded songs: {len(songs)}")
                
    except FileNotFoundError:
        print(f"Error: The file at {csv_path} could not be found.")

    
        
    return songs
    

def recommend_songs(user_prefs: Dict, songs: List[Dict], k: int = 5) -> List[Tuple[Dict, float, str]]:
    """
    Functional implementation of the recommendation logic.
    Required by src/main.py
    """
    # TODO: Implement scoring and ranking logic
    # Expected return format: (song_dict, score, explanation)
    """
    Scores all songs in the catalog and returns the top k recommendations.
    Returns a list of tuples containing the song dictionary, its numeric score, and the reasons.
    """
    
    scored_songs = []
    # 1. Loop through all songs and act as the "judge"
    for song in songs:
        score, reasons = score_song(user_prefs, song)
        # Store the song along with its newly calculated score and reasons
        scored_songs.append((song, score, reasons))
        
    # 2. Sort the list of tuples based on the score (which is at index 1) in descending order
    ranked_songs = sorted(scored_songs, key=lambda x: x[1], reverse=True)
    
    # 3. Return only the top k results using list slicing
    return ranked_songs[:k]
    

def score_song(user_prefs: Dict, song: Dict) -> Tuple[float, List[str]]:
    """
    Calculates a compatibility score between a user profile and a song.
    Returns the total numeric score and a list of string reasons explaining the score.
    """
    score = 0.0
    reasons = []

    # 1. Genre Match (High Priority)
    if user_prefs["favorite_genre"] == song["genre"]:
        score += 2.0
        reasons.append("Genre match (+2.0)")

    # 2. Mood Match (Medium Priority)
    if user_prefs["favorite_mood"] == song["mood"]:
        score += 1.0
        reasons.append("Mood match (+1.0)")

    # 3. Energy Proximity (Math Calculation)
    # 1.0 for perfect match, decreases as the gap widens
    energy_score = 1.0 - abs(user_prefs["target_energy"] - song["energy"])
    score += energy_score
    reasons.append(f"Energy match (+{energy_score:.2f})")

    return score, reasons
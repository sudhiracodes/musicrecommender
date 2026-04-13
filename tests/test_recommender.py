from src.recommender import Song, UserProfile, Recommender

def make_small_recommender() -> Recommender:
    songs = [
        Song(
            id=1,
            title="Test Pop Track",
            artist="Test Artist",
            genre="pop",
            mood="happy",
            energy=0.8,
            tempo_bpm=120,
            valence=0.9,
            danceability=0.8,
            acousticness=0.2,
        ),
        Song(
            id=2,
            title="Chill Lofi Loop",
            artist="Test Artist",
            genre="lofi",
            mood="chill",
            energy=0.4,
            tempo_bpm=80,
            valence=0.6,
            danceability=0.5,
            acousticness=0.9,
        ),
    ]
    return Recommender(songs)


def test_recommend_returns_songs_sorted_by_score():
    user = UserProfile(
        favorite_genre="pop",
        favorite_mood="happy",
        target_energy=0.8,
        likes_acoustic=False,
    )
    rec = make_small_recommender()
    results = rec.recommend(user, k=2)

    assert len(results) == 2
    # Starter expectation: the pop, happy, high energy song should score higher
    assert results[0].genre == "pop"
    assert results[0].mood == "happy"


def test_explain_recommendation_returns_non_empty_string():
    user = UserProfile(
        favorite_genre="pop",
        favorite_mood="happy",
        target_energy=0.8,
        likes_acoustic=False,
    )
    rec = make_small_recommender()
    song = rec.songs[0]

    explanation = rec.explain_recommendation(user, song)
    assert isinstance(explanation, str)
    assert explanation.strip() != ""


def test_recommend_prefers_closer_energy():
    """
    Ensures that if genres/moods are equal, the song with the energy 
    level closest to the target is ranked first.
    """
    user = UserProfile(
        favorite_genre="rock",
        favorite_mood="energetic",
        target_energy=0.9,
        likes_acoustic=False
    )
    
    # Two songs with the same genre/mood, but different energy levels
    song1 = Song(id=1, title="Far Energy", artist="A", genre="rock", mood="energetic", 
                 energy=0.5, tempo_bpm=120, valence=0.5, danceability=0.5, acousticness=0.1)
    song2 = Song(id=2, title="Close Energy", artist="B", genre="rock", mood="energetic", 
                 energy=0.85, tempo_bpm=120, valence=0.5, danceability=0.5, acousticness=0.1)
    
    rec = Recommender([song1, song2])
    results = rec.recommend(user, k=2)

    # The song with 0.85 energy is much closer to the 0.9 target than the 0.5 song
    assert results[0].title == "Close Energy"
    assert results[1].title == "Far Energy"
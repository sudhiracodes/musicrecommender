# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name  

Give your model a short, descriptive name.  
Example: **VibeFinder 1.0** 
VectorVibeMatch

---

## 2. Intended Use  

Describe what your recommender is designed to do and who it is for. 

Prompts:  

- What kind of recommendations does it generate  
- What assumptions does it make about the user  
- Is this for real users or classroom exploration  

This recommender is designed to suggest songs from a local catalog based on specific audio attributes and genre labels. It is intended for classroom exploration and simulated environments to demonstrate how content-based filtering logic works. It assumes the user has a clear idea of the "vibe" (energy and mood) they want and can provide specific targets for those values.

---

## 3. How the Model Works  

Explain your scoring approach in simple language.  

Prompts:  

- What features of each song are used (genre, energy, mood, etc.)  
- What user preferences are considered  
- How does the model turn those into a score  
- What changes did you make from the starter logic  

Avoid code here. Pretend you are explaining the idea to a friend who does not program.

The model looks at four main pieces of information for every song: its genre, its mood, its energy level, and its tempo.

When a user provides their preferences, the system acts like a judge. It gives "bonus points" if a song is in the user's favorite genre (+2.0) or matches their current mood (+1.0). It also uses a math formula to see how close the song's energy is to the user's target energy; the closer the match, the more points the song gets (up to +1.0). Unlike the starter logic which was very basic, I implemented a proximity-based math rule to ensure we find the "best fit" rather than just the loudest or highest-energy songs.

---

## 4. Data  

Describe the dataset the model uses.  

Prompts:  

- How many songs are in the catalog  
- What genres or moods are represented  
- Did you add or remove data  
- Are there parts of musical taste missing in the dataset  

The catalog consists of 20 songs (the original 10 plus 10 custom additions). It represents a variety of genres including Pop, Rock, Electronic, Lofi, and Jazz, with moods ranging from Happy and Energetic to Chill and Sad. While diverse for its size, the dataset is missing many sub-genres (like Heavy Metal or Classical) and does not account for song popularity or release year.

---

## 5. Strengths  

Where does your system seem to work well  

Prompts:  

- User types for which it gives reasonable results  
- Any patterns you think your scoring captures correctly  
- Cases where the recommendations matched your intuition  

The system works exceptionally well for users with consistent, mainstream tastes (e.g., someone who strictly wants "Happy Pop"). It is very accurate at filtering out "wrong" vibes, for example, it will never suggest a high-energy rock song to a user who has requested a chill, low-energy electronic profile. It effectively captures the "energy" of a session through its proximity scoring logic.

---

## 6. Limitations and Bias 



Where the system struggles or behaves unfairly. 

Prompts:  

- Features it does not consider  
- Genres or moods that are underrepresented  
- Cases where the system overfits to one preference  
- Ways the scoring might unintentionally favor some users  

The primary limitation of this system is its rigid reliance on exact categorical matches, which creates a strong "filter bubble" effect. Initially, the algorithm heavily over-prioritized exact string matches for genre. This meant a highly relevant song that perfectly matched a user's energy could be completely ignored simply because the genre label was slightly different. Furthermore, because the model uses a linear additive scoring method on a small dataset, it struggles heavily with negatively correlated preferences (e.g., a user requesting a "sad" mood but a "high" target energy), often resulting in compromised or inaccurate recommendations for edge-case profiles.

---

## 7. Evaluation  

How you checked whether the recommender behaved as expected. 

Prompts:  

- Which user profiles you tested  
- What you looked for in the recommendations  
- What surprised you  
- Any simple tests or comparisons you ran  

No need for numeric metrics unless you created some.

The model was evaluated via CLI testing using distinct user profiles: "High-Energy Pop", "Chill Lofi", and an adversarial "Sad but High Energy" profile. Code logic was also tested by running a "Weight Shift" experiment (halving the point value of genre and doubling the importance of energy). This experiment successfully verified that the initial logic was heavily biased toward genre, and shifting the weights allowed high-energy songs from different genres to rank higher, proving the math's sensitivity to developer tuning.

---

## 8. Future Work  

Ideas for how you would improve the model next.  

Prompts:  

- Additional features or preferences  
- Better ways to explain recommendations  
- Improving diversity among the top results  
- Handling more complex user tastes  

In the future, I would implement fuzzy matching for genres so that "Rock" and "Alternative Rock" could still earn points together. I would also add a "Diversity" penalty to the ranking rule to ensure that the top 5 results aren't all from the same artist, giving the user more variety. Finally, I’d love to add tempo-based matching to better support workout-specific playlists.

---

## 9. Personal Reflection  

A few sentences about your experience.  

Prompts:  

- What you learned about recommender systems  
- Something unexpected or interesting you discovered  
- How this changed the way you think about music recommendation apps  

Building this taught me that even "simple" recommendation algorithms require a lot of human fine-tuning to feel right. I was surprised by how much a small change in weights (like favoring energy over genre) completely flipped the results. It made me realize that the "algorithms" we interact with daily on apps like Spotify are likely a massive web of these tiny weight adjustments, constantly trying to balance what we like with the need to show us something new. If I kept working on this, I’d add a "Diversity" rule so the top results aren't all by the same artist, and maybe use tempo to help people find better songs for working out.
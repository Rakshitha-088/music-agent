from flask import Flask, render_template, request
import random

app = Flask(__name__)

songs = {
    "Why This Kolaveri Di": "Tamil hit song from movie 3",
    "Vaathi Coming": "Popular Vijay song from Master",
    "Arabic Kuthu": "Energetic dance song from Beast"
}

generated_titles = [
    "Dream Waves",
    "Midnight Echo",
    "Ocean Beats",
    "Calm Horizon",
    "Sky Rhythm"
]

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/generate", methods=["POST"])
def generate():
    mood = request.form["mood"]
    genre = request.form["genre"]
    duration = request.form["duration"]
    tempo = request.form["tempo"]
    loop = request.form.get("loop")

    title = random.choice(generated_titles)

    return render_template(
        "result.html",
        title=title,
        mood=mood,
        genre=genre,
        duration=duration,
        tempo=tempo,
        loop=loop
    )

@app.route("/songs")
def songs_list():
    return render_template("songs.html", songs=songs)

@app.route("/lyrics/<song>")
def lyrics(song):
    lyric = songs.get(song, "Lyrics not available")
    return render_template("lyrics.html", song=song, lyric=lyric)

if __name__ == "__main__":
    app.run(debug=True)
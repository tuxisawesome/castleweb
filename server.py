from flask import Flask, render_template
print("Now running up!")
app = Flask(__name__)
@app.route("/")
def main():
    return render_template("index.html")

@app.route("/downloads")
def downloads():
    return render_template("downloads.html")

@app.route("/downloads/family-movie")
def download_family_movie():
    return render_template('download-family-movie.html')

@app.route("/videos")
def videos():
    return render_template('videos.html')

if __name__ == "__main__":
    app.run(debug=False, host="10.0.0.8", port=80)
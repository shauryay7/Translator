from flask import Flask, render_template, request
from googletrans import Translator

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def translate():
    translation = ""
    if request.method == "POST":
        text = request.form["text"]
        target_language = request.form["language"]
        translator = Translator()
        try:
            translation = translator.translate(text, dest=target_language).text
        except Exception as e:
            translation = f"Error: {e}"
    return render_template("index.html", translation=translation)

if __name__ == "__main__":
    app.run(debug=True)
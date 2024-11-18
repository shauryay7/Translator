from flask import Flask, render_template, request
from googletrans import Translator, LANGUAGES

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def translate():
    translation = ""
    source_language = ""
    error_message = ""

    if request.method == "POST":
        text = request.form["text"]
        target_language = request.form["target_language"]
        source_language = request.form.get("source_language", "auto")
        translator = Translator()

        try:
            result = translator.translate(text, src=source_language, dest=target_language)
            translation = result.text
        except Exception as e:
            error_message = "Translation error. Please check your input or try again later."

    return render_template(
        "index.html",
        translation=translation,
        source_language=source_language,
        languages=LANGUAGES,
        error_message=error_message
    )

if __name__ == "__main__":
    app.run(debug=True)
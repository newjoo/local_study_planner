from flask import Flask, render_template, request

app = Flask(
    __name__,
    template_folder="../templates",
    static_folder="../static"
)

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        toc = request.form["toc"]
        print(toc)

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
from flask import Flask, request, render_template_string

app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome to the Test Flask App!"

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        return f"You entered: {username}"
    return '''
        <form method="post">
            <input name="username">
            <button type="submit">Login</button>
        </form>
    '''

@app.route("/search")
def search():
    query = request.args.get("q")
    return f"Results for: {query}"

if __name__ == "__main__":
    app.run(debug=True)

from flask import Flask, render_template, request, jsonify, redirect, url_for
from granite_chat import get_granite_response

app = Flask(__name__)

# 🟢 Landing Page (default route)
@app.route("/")
def landing():
    return render_template("landing.html")

# 🔵 Chatbot Page
@app.route("/chat", methods=["GET", "POST"])
def chat_page():
    if request.method == "GET":
        return render_template("index.html")  # this shows chatbot UI
    else:
        user_input = request.json.get("message", "")
        print("📥 Question:", user_input)
        response = get_granite_response(user_input)
        print("🤖 Answer:", response)
        return jsonify({"message": response})

# 🔐 Login Page
@app.route("/login", methods=["GET", "POST"])
def login():
    error = None
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if username == "admin" and password == "admin123":
            return redirect(url_for("chat_page"))
        else:
            error = "Invalid username or password"
    return render_template("login.html", error=error)

# ℹ️ About Page
@app.route("/about")
def about():
    return render_template("about.html")

# 🛠️ Services Page (optional placeholder)
@app.route("/services")
def services():
    return "<h2>CitizenAI Services Page (Coming Soon)</h2>"

# 📊 Dashboard
@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")


if __name__ == "__main__":
    app.run(debug=True)

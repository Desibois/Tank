from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/move")
def move():
    direction = request.args.get("dir")
    print(f"Move command received: {direction}")
    return f"Moved {direction}"

@app.route("/fire")
def fire_gun():
    print("FIRE command received")  # logs to console
    return "FIRING"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)  # accessible from any device on your network

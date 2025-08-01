from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "✅ Hello! This is a simple CI/CD Python App build test via Jenkins."

if __name__ == "__main__":
    app.run(debug=True)


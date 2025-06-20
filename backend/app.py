from flask import Flask
app = Flask(__name__)

@app.route("/api/health")
def health():
    return {"status": "ok"}, 200
    
@app.route("/api/message")
def message():
    return {"message": "Привіт з Flask backend!"}, 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

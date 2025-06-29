from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>Hello from Flask on PRD Azure!</h1><p>Successfully deployed.</p>"

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 8000))
    app.run(host='0.0.0.0', port=port)

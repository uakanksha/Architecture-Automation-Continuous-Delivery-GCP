from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, World! This is my Flask app running in Docker."

if __name__ == '__main__':
    # Run the app on port 5000 (default port for Flask)
    app.run(host='0.0.0.0', port=5000)

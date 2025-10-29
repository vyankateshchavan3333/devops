from flask import Flask, request
import logging

# --- Logging Setup ---
logging.basicConfig(filename='app.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

app = Flask(__name__)

@app.route('/')
def home():
    logging.info(f"Request received from {request.remote_addr}")
    return "Hello, DevOps World The Flask app is running successfully "

@app.route('/health')
def health_check():
    return {"status": "healthy"}, 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
from flask import Flask, jsonify

app = Flask(__name__)

# Sample data representing gym services
gym_services = [
    {"id": 1, "service": "Weightlifting", "capacity": 20},
    {"id": 2, "service": "Yoga Class", "capacity": 15},
    {"id": 3, "service": "Cardio Zone", "capacity": 30}
]

@app.route('/')
def home():
    return "ACEest Fitness & Gym - Operational"

@app.route('/services', methods=['GET'])
def get_services():
    return jsonify({"status": "success", "data": gym_services})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
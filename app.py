from flask import Flask, request, jsonify
import pika
import json

app = Flask(__name__)

# Connect to RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.queue_declare(queue='notifications')

# In-memory user notifications storage (for demo)
user_notifications = {}

@app.route('/notifications', methods=['POST'])
def send_notification():
    data = request.json
    # Example data: {"user_id":1, "type":"email", "message":"Hello"}
    channel.basic_publish(exchange='',
                          routing_key='notifications',
                          body=json.dumps(data))
    return jsonify({"status": "queued"}), 202

@app.route('/users/<int:user_id>/notifications', methods=['GET'])
def get_notifications(user_id):
    notifications = user_notifications.get(user_id, [])
    return jsonify(notifications), 200

if __name__ == '__main__':
    app.run(debug=True)
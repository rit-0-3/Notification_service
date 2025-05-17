import pika
import json
import time

def send_email(notification):
    print(f"Sending email: {notification}")
    # simulate success
    return True

def process_notification(ch, method, properties, body):
    notification = json.loads(body)
    success = False
    retries = 3
    while retries > 0 and not success:
        try:
            if notification['type'] == 'email':
                success = send_email(notification)
            # Add SMS and in-app logic here
            if success:
                print("Notification sent successfully.")
            else:
                raise Exception("Send failed")
        except Exception as e:
            print(f"Error: {e}, retrying...")
            retries -= 1
            time.sleep(2)
    ch.basic_ack(delivery_tag=method.delivery_tag)

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.queue_declare(queue='notifications')
channel.basic_consume(queue='notifications', on_message_callback=process_notification)

print('Waiting for messages...')
channel.start_consuming()
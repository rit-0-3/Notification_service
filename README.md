
# Notification Service

## Overview

This project is a simple Notification Service built with Flask and RabbitMQ. It provides an API to send notifications to users via Email, SMS, or in-app messages using a queue-based system for reliability and scalability.

---

## Features

- REST API with endpoints to send notifications and retrieve user notifications.
- Supports multiple notification types: Email, SMS, and In-app.
- Uses RabbitMQ as a message queue to handle notifications asynchronously.
- Retry mechanism for failed notifications (can be extended).
- Simulated sending of notifications (prints messages to the console).

---

## Setup Instructions

### Prerequisites

- Python 3.8+
- RabbitMQ installed and running locally ([Download here](https://www.rabbitmq.com/download.html))
- Git (optional, for cloning repo)

---

### Installation

1. Clone the repository:

```bash
git clone https://github.com/rit-0-3/notification_service.git
cd notification_service
````

2. Create and activate a virtual environment:

On Windows PowerShell:

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Start RabbitMQ server (make sure it is running locally).

---

### Running the Application

1. Run the Flask app (API server):

```bash
python app.py
```

2. In a new terminal window, start the RabbitMQ worker to process notification messages:

```bash
python notifications/queue_worker.py
```

---

### API Endpoints

* **Send Notification**
  `POST /notifications`
  Request JSON:

  ```json
  {
    "user_id": 1,
    "type": "email",
    "message": "Hello from Rit!"
  }
  ```

  Response:

  ```json
  {
    "status": "queued"
  }
  ```

* **Get User Notifications**
  `GET /users/{id}/notifications`

---

### Assumptions and Notes

* Actual sending of emails or SMS is simulated via console print statements.
* RabbitMQ runs on `localhost` with default ports.
* No persistent database; notifications are stored in-memory (can be extended).
* No authentication or authorization implemented.
* Retry mechanism for failed notifications is a placeholder and can be enhanced.

---

### License

MIT License

---



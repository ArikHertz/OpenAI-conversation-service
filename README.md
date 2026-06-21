# Flask ChatGPT

A web-based AI chat application inspired by ChatGPT. Send messages, receive AI-powered replies, and continue conversations with full context — every message is stored in a MySQL database.

## Features

- **Context-aware chat** — The full conversation history is sent to OpenAI on each request, so the assistant remembers earlier messages within a session.
- **Persistent storage** — Conversations and messages are saved to MySQL via SQLAlchemy.
- **Session management** — Start a new conversation at any time without losing previous data.
- **Form validation & CSRF protection** — Built with Flask-WTF for secure form handling.
- **Responsive UI** — Modern dark glassmorphism design with Bootstrap 5.
- **Keyboard shortcuts** — Press `Enter` to send, `Shift + Enter` for a new line.

## Tech Stack

| Layer      | Technology                          |
| ---------- | ----------------------------------- |
| Backend    | Python, Flask                       |
| Database   | MySQL, SQLAlchemy                   |
| AI         | OpenAI Chat Completions API         |
| Frontend   | HTML, CSS, JavaScript, Bootstrap 5  |
| Templates  | Jinja2                              |

## Project Structure

```
├── src/
│   ├── app.py                  # Application entry point
│   ├── config.py               # Configuration & environment variables
│   ├── routes/
│   │   └── main.py             # Home, About, and New Conversation routes
│   ├── models/
│   │   ├── conversation.py     # Conversation database model
│   │   └── message.py          # Message database model
│   ├── forms/
│   │   └── chat_forms.py       # WTForms for chat input
│   ├── services/
│   │   └── openai_service.py   # OpenAI API integration
│   ├── templates/
│   │   ├── base.html
│   │   ├── home.html
│   │   └── about.html
│   └── static/
│       ├── css/style.css
│       └── js/chat.js
├── requirements.txt
└── README.md
```

## Prerequisites

- Python 3.10+
- MySQL server
- An [OpenAI API key](https://platform.openai.com/api-keys)

## Installation

### 1. Clone the repository

```bash
git clone <repository-url>
cd "4th Project"
```

### 2. Create and activate a virtual environment

```bash
python -m venv env

# Windows
env\Scripts\activate

# macOS / Linux
source env/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Set up the MySQL database

Create a database for the application:

```sql
CREATE DATABASE chatgpt_flask CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
```

Tables are created automatically when the app starts (`db.create_all()`).

### 5. Configure environment variables

Create a `.env` file inside the `src/` directory:

```env
FLASK_APP=app.py
FLASK_DEBUG=1

SECRET_KEY=your-secret-key-here
OPENAI_API_KEY=your-openai-api-key
OPENAI_MODEL=gpt-4o-mini

MYSQL_HOST=localhost
MYSQL_PORT=3306
MYSQL_DATABASE=chatgpt_flask
MYSQL_USER=root
MYSQL_PASSWORD=your-mysql-password
```

> **Note:** Never commit your `.env` file or expose API keys publicly.

## Running the App

From the `src/` directory:

```bash
cd src
python app.py
```

The app will be available at **http://127.0.0.1:5000**.

Alternatively, using Flask CLI:

```bash
cd src
flask run
```

## Usage

1. Open the home page and type a message in the input box.
2. Press **Send** or hit **Enter** to submit.
3. The assistant reply appears in the chat area with full conversation context.
4. Click **New Conversation** to start a fresh session.
5. Visit the **About** page for system and developer information.

## Developer

**Arik Hertz**  
Email: arikhertzw@gmail.com  
GitHub: (https://github.com/ArikHertz)

## License

This project is for educational purposes.

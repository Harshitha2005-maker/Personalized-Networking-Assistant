# Personalized Networking Assistant

An AI-powered web application that helps users generate personalized conversation starters for professional and social networking events. The application extracts key themes from event descriptions, generates context-aware conversation prompts, verifies facts using Wikipedia, and maintains conversation history with user feedback.

## Features

- Generate AI-powered conversation starters
- Theme extraction using DistilBERT
- Context-aware prompt generation using GPT-2/Gemini
- Fact verification using Wikipedia API
- Conversation history management
- User feedback system (👍/👎)
- FastAPI REST APIs
- Interactive Streamlit interface

## Tech Stack

- Python
- FastAPI
- Streamlit
- DistilBERT
- GPT-2 / Google Gemini API
- Wikipedia API
- SQLite / PostgreSQL
- Pytest
- Git & GitHub

## Project Structure

```
Personalized-Networking-Assistant/
│── backend/
│   ├── routes/
│   ├── services/
│   ├── models/
│   ├── database/
│   └── main.py
│
│── frontend/
│   └── app.py
│
│── tests/
│
│── requirements.txt
│── README.md
```

## Installation

### Clone the repository

```bash
git clone https://github.com/your-username/Personalized-Networking-Assistant.git
cd Personalized-Networking-Assistant
```

### Create a virtual environment

```bash
python -m venv venv
```

Activate the environment

**Windows**

```bash
venv\Scripts\activate
```

**Linux/macOS**

```bash
source venv/bin/activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Run the FastAPI backend

```bash
uvicorn backend.main:app --reload
```

### Run the Streamlit frontend

```bash
streamlit run frontend/app.py
```

## Workflow

1. Enter an event description and interests.
2. Extract themes using DistilBERT.
3. Generate conversation starters using GPT-2/Gemini.
4. Verify facts using Wikipedia API.
5. Save conversation history and feedback.

## Future Enhancements

- User authentication
- Advanced personalization
- Multi-language support
- Cloud deployment
- AI model fine-tuning

## Team Members

- Machupalli Deepika (Team Lead)
- Pullagura Harshitha
- Brahmani Kammari
- Syamana Boyana Sravani
- Chandana Ragi

## License

This project is developed for educational purposes.# Personalized-Networking-Assistant
Personalized Networking Assistant is an AI-powered web app that generates personalized conversation starters for networking events. It uses DistilBERT for theme extraction, GPT-2/Gemini for prompt generation, Wikipedia API for fact checking, and stores conversation history and user feedback for improved personalization.

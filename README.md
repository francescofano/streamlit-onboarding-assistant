# Streamlit Onboarding Assistant

An intelligent assistant built with LangChain that helps with employee onboarding by providing context-aware responses based on company policies and employee information.

## Features

- 🤖 LangChain-powered conversational AI
- 📚 Vector store integration for intelligent policy lookups
- 💬 Conversation history tracking
- 👤 Personalized responses based on employee context
- 🔄 Streaming responses for better UX

## Setup

### Prerequisites

- Python 3.12+
- OpenAI API key

### Installation

1. Clone the repository:
   ```
   git clone https://github.com/francescofano/streamlit-onboarding-assistant.git
   cd streamlit-onboarding-assistant
   ```

2. Set up the environment:
   ```
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Configure environment:
   ```
   cp .env.example .env
   ```
   Then edit .env with your API keys

### Usage

Start the application:
```
streamlit run gui.py
```


## Project Structure

- `app.py` - Main application entry point
- `assistant.py` - Core assistant implementation
- `prompts.py` - System prompts and templates
- `gui.py` - GUI interface
- `requirements.txt` - Project dependencies
- `.env` - Environment variables
- `.env.example` - Example environment variables


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

2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Configure environment:
   ```
   cp .env.example .env
   ```
   Then edit .env with your API keys

### Usage

Start the application:
```
python app.py
```

Or use the GUI interface:
```
python gui.py
```

## Project Structure

- `app.py` - Main application entry point
- `assistant.py` - Core assistant implementation
- `prompts.py` - System prompts and templates
- `gui.py` - GUI interface
- `requirements.txt` - Project dependencies
- `.env` - Environment variables
- `.env.example` - Example environment variables

## Development

To extend the assistant:
1. Modify prompts in `prompts.py`
2. Update vector store with new documents
3. Extend `assistant.py` for new features




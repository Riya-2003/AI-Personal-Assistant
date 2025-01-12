# AI Personal Assistant

An advanced AI-powered personal assistant capable of scheduling emails, answering questions from recorded calls, performing web searches, delivering news updates, and providing weather reports.

## Features

- **Email Scheduling**: Automatically draft and send emails using Gmail API.
- **Question Answering from Recorded Calls**: Utilize language models to extract insights and answer questions based on transcriptions of recorded calls.
- **Web Searching**: Perform live web searches for real-time information using the Serper API.
- **News Reporting**: Fetch the latest news updates based on user preferences.
- **Weather Reporting**: Provide weather updates for specified locations.

## Technologies Used

- **Python**
- **LangChain**
- **CrewAI**
- **Google Gmail API**
- **Groq Language Model (Llama 3)**
- **Cohere API**
- **Serper API**

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/ai-personal-assistant.git
   ```
2. Navigate to the project directory:
   ```bash
   cd ai-personal-assistant
   ```
3. Set up a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # For Windows use `venv\Scripts\activate`
   ```
4. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

## Environment Variables

Create a `.env` file in the root directory of your project and add the following keys:

```plaintext
MODEL=groq/llama-3.1-70b-versatile
GROQ_API_KEY=your_groq_api_key_here
SERPER_API_KEY=your_serper_api_key_here
COHERE_API_KEY=your_cohere_api_key_here
```

### Acquiring API Keys:
- **GROQ API Key**: [https://groq.com](https://groq.com)
- **Serper API Key**: [https://serper.dev](https://serper.dev)
- **Cohere API Key**: [https://cohere.com](https://cohere.com)

## Usage

1. **Run the Assistant:**
   ```bash
   python main.py
   ```
2. The assistant will prompt for tasks such as email scheduling, web searches, or news updates.

## Project Structure

```
ai_assistant
│
├── src/ai_assistant
│   ├── __pycache__
│   ├── config
│   │   ├── agents.yaml  # Configuration for AI agents
│   │   └── tasks.yaml   # Configuration for tasks
│   ├── tools
│   │   ├── __pycache__
│   │   ├── __init__.py  # Package initialization
│   │   ├── custom_tool.py  # Custom tools for the assistant
│   │   └── crew.py  # Crew setup for task execution
│   └── main.py  # Main entry point for the assistant
│
├── tests  # Unit tests
├── .env  # Environment variables (excluded from version control)
├── .gitignore  # Ignoring sensitive and unnecessary files
├── pyproject.toml  # Project dependencies and configurations
└── README.md  # Project documentation
```
## Contributing
Contributions are welcome! Please fork the repository and create a pull request with your changes.
- Fork the repository
- Create a feature branch
- Submit a pull request

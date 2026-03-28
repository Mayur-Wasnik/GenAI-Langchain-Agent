# GenAI LangChain Agents - QuikAnswer

A Streamlit-based intelligent search agent powered by LangChain and Groq LLM that answers questions by searching Google in real-time.

## Features

- 🔍 **Real-time Google Search**: Dynamic web search integration for accurate, up-to-date information
- 🤖 **AI-Powered Responses**: Uses Llama 3.1 8B model via Groq for intelligent answer generation
- 💬 **Interactive Chat Interface**: User-friendly Streamlit interface with conversation history
- ⚡ **Streaming Responses**: Real-time streaming of AI responses for faster user experience
- 📝 **Memory Support**: LangGraph MemorySaver for maintaining conversation context

## Prerequisites

- Python 3.8+
- Groq API Key
- Google Serper API Key

## Installation

1. Clone or download this project

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Create a `.env` file in the project root with your API keys:
```env
GROQ_API_KEY=your_groq_api_key_here
SERPER_API_KEY=your_google_serper_api_key_here
```

## Usage

Run the Streamlit app:
```bash
streamlit run app.py
```

The application will open in your default browser at `http://localhost:8501`

1. Type your question in the chat input
2. The agent will search Google for relevant information
3. The AI will generate an answer based on the search results
4. Type 'quit' to exit (or just close the browser)

## Project Structure

```
├── app.py              # Main Streamlit application
├── requirements.txt    # Python dependencies
├── .env               # Environment variables (not tracked in git)
├── .gitignore         # Git ignore rules
└── README.md          # This file
```

## Dependencies

- **langchain**: LLM framework
- **langchain-groq**: Groq chat LLM integration
- **langchain-community**: Community utilities including GoogleSerperAPIWrapper
- **langgraph**: Graph-based agent execution with memory
- **streamlit**: Web UI framework
- **groq**: Groq API client
- **python-dotenv**: Environment variable management

## Configuration

The agent is configured with the following settings:

- **Model**: Llama 3.1 8B Instant (via Groq)
- **Streaming**: Enabled for real-time response generation
- **System Prompt**: Instructs the agent to search for answers and admit when uncertain
- **Memory**: In-memory checkpointer for session state management

## Error Handling

The application handles `BadRequestError` from Groq API and maintains conversation history for resilience.

## License

This project is for educational purposes.

## Support

For issues or questions, please check:
- [LangChain Documentation](https://python.langchain.com/)
- [Groq Documentation](https://console.groq.com/docs)
- [Streamlit Documentation](https://docs.streamlit.io/)

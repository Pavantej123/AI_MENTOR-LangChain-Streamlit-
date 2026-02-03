# AI Mentor Chatbot 🤖

An intelligent AI-powered mentor chatbot built with Streamlit and LangChain that provides personalized guidance, answers questions, and assists users in their learning journey.

## 🌟 Features

- **Interactive Chat Interface**: Clean and intuitive UI built with Streamlit
- **AI-Powered Responses**: Leverages LangChain for intelligent conversation handling
- **Context-Aware Mentoring**: Maintains conversation history for coherent interactions
- **Real-time Responses**: Fast and responsive chatbot experience
- **Customizable Mentoring**: Adaptable to various learning domains and topics

## 🛠️ Technologies Used

- **Frontend**: Streamlit
- **Backend**: LangChain
- **Language Model**: OpenAI GPT / Anthropic Claude (specify which one you used)
- **Python**: 3.8+

## 📋 Prerequisites

Before running this project, ensure you have:

- Python 3.8 or higher installed
- pip (Python package manager)
- API key for your chosen LLM provider (OpenAI, Anthropic, etc.)

## 🚀 Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/ai-mentor-chatbot.git
   cd ai-mentor-chatbot
   ```

2. **Create a virtual environment** (recommended)
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install required packages**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   
   Create a `.env` file in the project root and add your API key:
   ```
   OPENAI_API_KEY=your_api_key_here
   # OR
   ANTHROPIC_API_KEY=your_api_key_here
   ```

## 📦 Dependencies

Create a `requirements.txt` file with the following dependencies:

```
streamlit>=1.28.0
langchain>=0.1.0
langchain-openai>=0.0.2  # or langchain-anthropic
python-dotenv>=1.0.0
openai>=1.0.0  # or anthropic
```

## 💻 Usage

1. **Run the Streamlit application**
   ```bash
   streamlit run app.py
   ```

2. **Access the application**
   
   Open your web browser and navigate to:
   ```
   http://localhost:8501
   ```

3. **Start chatting**
   
   Type your questions or topics you need mentoring on, and the AI mentor will provide guidance and support!

## 📁 Project Structure

```
ai-mentor-chatbot/
│
├── app.py                 # Main Streamlit application
├── requirements.txt       # Project dependencies
├── .env                   # Environment variables (not tracked in git)
├── .gitignore            # Git ignore file
├── README.md             # Project documentation
│
├── utils/                # Utility functions (optional)
│   └── langchain_utils.py
│
└── config/               # Configuration files (optional)
    └── config.py
```

## ⚙️ Configuration

You can customize the chatbot's behavior by modifying:

- **System Prompt**: Edit the mentor's personality and expertise areas
- **Model Parameters**: Adjust temperature, max tokens, etc.
- **UI Theme**: Customize Streamlit's appearance in `.streamlit/config.toml`

## 🔑 Key Features Explained

### LangChain Integration
- Uses LangChain's conversation chain for managing chat history
- Implements memory to maintain context across messages
- Supports various LLM providers through LangChain's unified interface

### Streamlit UI
- Clean and responsive chat interface
- Real-time message updates
- Session state management for conversation persistence
- Easy-to-use input fields and chat display

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the project
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🐛 Known Issues

- List any known issues or limitations here

## 🔮 Future Enhancements

- [ ] Add support for multiple conversation threads
- [ ] Implement file upload for document-based mentoring
- [ ] Add voice input/output capabilities
- [ ] Create user authentication system
- [ ] Add conversation export functionality
- [ ] Integrate with additional knowledge bases


## 🙏 Acknowledgments

- [Streamlit](https://streamlit.io/) for the amazing web framework
- [LangChain](https://www.langchain.com/) for the powerful LLM framework
- [OpenAI](https://openai.com/) / [Anthropic](https://anthropic.com/) for the language models

---

**Note**: Remember to never commit your `.env` file or API keys to version control. Add `.env` to your `.gitignore` file.

# Telegram Chatbot

This is a simple Telegram chatbot powered by the TinyLlama language model. It responds to user messages with friendly, professional, and concise answers.

## Features
- Uses the `transformers` library to generate text responses.
- Runs on Telegram using the `python-telegram-bot` library.

## Setup Instructions

### Prerequisites
- Python 3.9 or later
- Telegram Bot Token (get it from [BotFather](https://core.telegram.org/bots#botfather))

### Installation
1. **Clone this repository**
   Clone this repository to your local machine:
   ```bash
   git clone https://github.com/your-username/telegram-chatbot.git
   cd telegram-chatbot
2. **Install Dependencies**
   Use pip to install the required Python libraries:
   ```bash
   pip install -r requirements.txt 
3. **Set Up Your Bot Token**
   Replace the placeholder API_TOKEN in the bot.py file with your Telegram bot token:
   ```python
   API_TOKEN = "YOUR_TELEGRAM_BOT_TOKEN"
4. **Run the Bot**
   Start the bot by running the script:
   ```bash
   python bot_iratxezunzunegui.py

### Usage
1. Open Telegram and search for your bot (you named it when creating it with BotFather).
2. Type /start to begin interacting with the bot.
3. Send any text message to get a response.

### Project Structure
```bash
telegram-chatbot/
├── bot.py            # Main script containing the chatbot logic
├── README.md         # Project description and setup instructions
├── requirements.txt  # Python dependencies
└── .gitignore        # Files and directories to exclude from version control
```
### License
This project is licensed under the MIT License. You are free to use, modify, and distribute it.

### Acknowledgments
- Hugging Face Transformers for the language model.
- python-telegram-bot for the Telegram integration.




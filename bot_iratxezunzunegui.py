# Import necessary modules
import logging
from telegram import ForceReply, Update
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters
import torch
from transformers import pipeline

# Your bot's API token
API_TOKEN = "YOUR_API_TOKEN"

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)

logging.getLogger("httpx").setLevel(logging.WARNING)

logger = logging.getLogger(__name__)

# Initialize the TinyLlama model
pipe = pipeline("text-generation", model="TinyLlama/TinyLlama-1.1B-Chat-v1.0", torch_dtype=torch.bfloat16, device_map="auto")

# Start function
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Send a welcome message in response to the command /start"""
    await update.message.reply_text("Hello! I am your AI assistant.")

# Message handler function
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Generate a response from the TinyLlama model and send it as a reply."""
    user_message = update.message.text
    messages = [
        {
            "role": "system",
            "content": "You are a friendly and professional chatbot. You provide accurate and helpful answers in a concise and clear manner.",
        },
        {"role": "user", "content": user_message},
    ]

    # Prepare the prompt
    prompt = pipe.tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
    
    # Generate the model's response
    outputs = pipe(prompt, max_new_tokens=512, do_sample=True, temperature=0.7, top_k=50, top_p=0.95)
    
    # Extract and clean up the response
    response = outputs[0]["generated_text"]
    # Split by "</s>" and get the last segment, which contains the assistant's reply
    assistant_response = response.split("</s>")[-1].strip()
    
    # Send the clean response back to the user
    await update.message.reply_text(assistant_response)

# Main function
def main():
    """Main function to start the bot"""
    application = Application.builder().token(API_TOKEN).build()

    # Add handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    # Start the bot
    application.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == "__main__":
    main()

from telethon import TelegramClient, events
import os
# Replace with your own values
api_id = os.environ.get("TELEGRAM_API_KEY")
api_hash = os.environ.get("TELEGRAM_API_HASH")
source_channel_id = 't.me/H1B_H4_Visa_Dropbox_slots'  # Example: 't.me/source_channel' or ID (numeric)
target_user_id = os.environ.get("TELEGRAM_USER_ID")        # Your personal Telegram ID
phone_number = os.environ.get("PHONE_NO")       # Your phone number associated with your Telegram

# Initialize the Telegram client
client = TelegramClient('session_name', api_id, api_hash)

# Function to filter messages
def filter_message(message):
    # Add your custom filtering logic here
    # For example, skip messages containing "spam"
    unwanted_keywords = ['report', 'NA']
    if any(keyword in message.message.lower() for keyword in unwanted_keywords):
        return False # test branch merging
    return True

# Event handler for new messages in the source channel
@client.on(events.NewMessage(chats=source_channel_id))
async def handler(event):
    message = event.message

    # Apply filter
    if filter_message(message):
        # Forward the message to your personal Telegram
        await client.send_message(target_user_id, message)

# Start the client and run until disconnected
client.start(phone_number)
print("Monitoring channel...")
client.run_until_disconnected()




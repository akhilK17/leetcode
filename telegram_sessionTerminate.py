from telethon import TelegramClient
import os

# Initialize the client with your session name
api_id = os.environ.get("TELEGRAM_API_KEY")
api_hash = os.environ.get("TELEGRAM_API_HASH")
client = TelegramClient('session_name', api_id, api_hash)

async def terminate_session():
    # Log out from Telegram
    await client.log_out()
    
    # Disconnect the client
    await client.disconnect()

# Run the termination
client.start()
client.loop.run_until_complete(terminate_session())
print("Session terminated.")

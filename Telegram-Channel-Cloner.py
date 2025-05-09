from telethon import TelegramClient
from telethon.tl.functions.messages import GetHistoryRequest

# Define your API ID, API hash, and phone number
api_id = 'id here'
api_hash = 'API HASH HERE'
phone = 'Your phone num here, start with + and contry code'

# Create the Telegram client
client = TelegramClient('session_name', api_id, api_hash)

async def main():
    await client.start(phone)

    # Replace 'source_channel' w ith the username or ID of the source channel
    source_channel = -00000000
    
    # Replace 'destination_chat_or_channel' with the username or ID of the destination chat or channel
    destination_chat_or_channel = 'desitnationchathere'
    
    # Number of messages to fetch
    num_messages = 10
    
    result = await client(GetHistoryRequest(
        peer=source_channel,
        limit=num_messages,
        offset_date=None,
        offset_id=0,
        max_id=0,
        min_id=0,
        add_offset=0,
        hash=0
    ))

    messages = result.messages
    
    for message in messages:
        if message.media and message.video:
            # Your new caption
            new_caption = 'new_caption'

            # Forward the video with the new caption
            await client.send_file(destination_chat_or_channel, message.media, caption=new_caption)

if __name__ == '__main__':
    import asyncio
    asyncio.run(main())

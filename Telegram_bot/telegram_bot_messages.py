# pip install telegram-send
# telegram-send --configure

import telegram_send
import asyncio

async def send_telegram(messages):
    await telegram_send.send(messages=[messages])
    return "The message OK!"

async def main():   
    messages = "People on object"
    print(await asyncio.create_task(send_telegram(messages)))   

if __name__ == "__main__":
    asyncio.run(main()) 
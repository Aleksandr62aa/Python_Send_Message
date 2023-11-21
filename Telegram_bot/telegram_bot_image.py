# pip install telegram-send
# telegram-send --configure

import telegram_send
import asyncio

async def send_telegram(img_path):         
    with open(img_path, "rb") as f:
        await telegram_send.send(images=[f])
    return "The image OK!"

async def main():   
    img_path  = "IMAGE\Track.jpg"
    print(await asyncio.create_task(send_telegram(img_path)))   

if __name__ == "__main__":
    asyncio.run(main())   
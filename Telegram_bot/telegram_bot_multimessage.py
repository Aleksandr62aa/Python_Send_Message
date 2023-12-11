# pip install telegram-send
# telegram-send --configure

import telegram_send
import asyncio

async def send_telegram(img, file, video, messages):         
    # 1.Attaching image
    with open(img, "rb") as f:        
        await telegram_send.send(images=[f])
    
    # 2.Attaching file    
    with open(file, "rb") as f:         
        await telegram_send.send(files=[f])

    # 3.Attaching video    
    with open(video, "rb") as f:         
        await telegram_send.send(videos=[f])
    
    # 4.Attaching message
    await telegram_send.send(messages=[messages])

    # 5.Attaching audios
    # with open(audios, "rb") as f:         
    #     await telegram_send.send(audios=[f])

    return "The image+file+video+message OK!"

async def main():   
    img = "IMAGE\Track.jpg"
    file = "result.xlsx"
    messages = "People on object"
    video = 'IMAGE\demo.mp4'
    print(await asyncio.create_task(send_telegram(img, file, video, messages)))   

if __name__ == "__main__":
    asyncio.run(main())   
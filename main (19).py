import asyncio
from botpress import Botpress

bot = Botpress(
    server_url='http://localhost:3000/api/v1',
    bot_id='my-bot',
    language='en',
    botpress_token='bp_pat_InhQ2HSl2n8jGGB5NYpJtaTTJUQuTyTzus9b'
)

async def run_chatbot():
    await bot.start()

    while True:
        user_input = input('You: ')
        bot_response = await bot.send_text(user_input)
        print('Bot:', bot_response)

    await bot.stop()

if __name__ == '__main__':
    asyncio.run(run_chatbot())

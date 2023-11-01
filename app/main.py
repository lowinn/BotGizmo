import asyncio
import logging
import sys
from os import getenv

from aiogram import Bot, Dispatcher, Router, types
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram.utils.markdown import hbold

# Bot token can be obtained via https://t.me/BotFather
TOKEN = '6580965378:AAH56yPQLJmXpy0Wx0gDPWGXYwNHZ_Z-p5k'

# All handlers should be attached to the Router (or Dispatcher)
dp = Dispatcher()


@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    """
    This handler receives messages with `/start` command
    """
    # Most event objects have aliases for API methods that can be called in events' context
    # For example if you want to answer to incoming message you can use `message.answer(...)` alias
    # and the target chat will be passed to :ref:`aiogram.methods.send_message.SendMessage`
    # method automatically or call API method directly via
    # Bot instance: `bot.send_message(chat_id=message.chat.id, ...)`
    wlcomeMessage = """
🤖 Bot Description: Welcome to BotTools – Your All-in-One Telegram Bot for Handy Tools and Information! Our bot offers a wide range of utilities to assist you in various areas of life. From educational resources to entertainment, development tools to travel recommendations, we've got you covered.

🏡 Home 🏠

    /shoppinglist 🛒 - Create and manage your shopping lists effortlessly.
    /recipes 🍽️ - Discover delicious recipes for your next meal.

📚 Education 🎓

    /learnlanguages 🗣️ - Start your language learning journey with interactive lessons.
    /mathtutorials 🧮 - Get help with math problems and tutorials.

💡 Technology 📱

    /technews 📰 - Stay updated with the latest tech news and trends.
    /codeexamples 💻 - Access coding examples and tips for developers.

👨‍💻 Developer 👩‍💻

    /codesharing 🚀 - Share your code snippets with the developer community.
    /api-docs 📖 - Find API documentation for popular services.

🎉 Entertainment 🎮

    /jokes 😄 - Get a dose of daily jokes and humor.
    /movierecs 🍿 - Discover movie recommendations tailored to your taste.

🏋️ Health and Wellness 🍏

    /workoutplans 💪 - Access workout routines and fitness tips.
    /healthytips 🥗 - Get advice on nutrition and a healthy lifestyle.

✈️ Travel 🌎

    /travelrecommendations 🌄 - Receive travel destination suggestions.
    /flightbooking ✈️ - Book flights and hotels for your next adventure.

📰 News and Updates 🗞️

    /newsheadlines 📊 - Stay informed with top news headlines.
    /weatherupdates 🌦️ - Check the latest weather forecasts.

Explore and enjoy the wide array of tools and resources at your fingertips with BotTools! Don't hesitate to use the provided commands to access the features you need. We're here to make your Telegram experience even more useful and enjoyable. 🌟
"""
    await message.answer(f"{wlcomeMessage}")
    #await message.answer(f"Hello, {hbold(message.from_user.full_name)}! ")
    
        
@dp.message()
async def echo_handler(message: types.Message) -> None:
    """
    Handler will forward receive a message back to the sender

    By default, message handler will handle all message types (like a text, photo, sticker etc.)
    """
    try:
        # Send a copy of the received message
        await message.send_copy(chat_id=message.chat.id)
    except TypeError:
        # But not all the types is supported to be copied so need to handle it
        await message.answer("Nice try!")
async def main() -> None:
    # Initialize Bot instance with a default parse mode which will be passed to all API calls
    bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
    # And the run events dispatching
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
    app.run(host='0.0.0.0', port=1222)

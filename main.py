
from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.types import Message

from aiogram_dialog import DialogManager, setup_dialogs, StartMode
from environs import Env

from states import MainSG
from windows import main_dialog, catalog_dialog

env = Env()
env.read_env()
storage = MemoryStorage()
bot = Bot(token=env('token'))
dp = Dispatcher(storage=storage)
print("Бот запущен!")

data = {
    'cart': list()
}

dp.include_router(main_dialog())
dp.include_router(catalog_dialog())
setup_dialogs(dp)


@dp.message(Command("start"))
async def start(message: Message, dialog_manager: DialogManager):
    await dialog_manager.start(MainSG.main, mode=StartMode.RESET_STACK)


if __name__ == '__main__':
    dp.run_polling(bot, skip_updates=True)

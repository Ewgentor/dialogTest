from aiogram.types import CallbackQuery
from aiogram_dialog import DialogManager
from aiogram_dialog.widgets.kbd import Button


async def add_to_cart(callback: CallbackQuery, button: Button, manager: DialogManager):
    manager.start_data['cart'].append(button.widget_id)


async def clear_cart(callback: CallbackQuery, button: Button, manager: DialogManager):
    manager.start_data['cart'].clear()


async def get_cart_data(**kwargs):
    dct = kwargs['dialog_manager'].start_data
    return dct if dct['cart'] else {'cart':['отсутствует']}

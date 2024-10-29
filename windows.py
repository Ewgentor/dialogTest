import operator

from aiogram_dialog import Dialog, Window
from aiogram_dialog.widgets.kbd import Row, Start, Next, Url, Back, Button, ScrollingGroup, SwitchTo, Checkbox, Radio, \
    Calendar
from aiogram_dialog.widgets.text import Const, List, Format

from cart import get_cart_data, add_to_cart, clear_cart
from states import CatalogSG, MainSG


products_btns = []
for i in range(20):
    products_btns.append(Button(Const(f"Товар {i+1}"), id=str(i+1),on_click=add_to_cart))


def main_dialog():
    main_dialog = Dialog(
        Window(
            Const("Добро пожаловать в наш магазинчик!"),
            Row(
                Start(Const("В каталог"), id="catalog", state=CatalogSG.catalog, data={'cart': list()}),
                Next(text=Const('Документация')),
                SwitchTo(Const("Тест"), id="test", state=MainSG.test,),
            ),
            state=MainSG.main,
        ),
        Window(
            Const("Аiogram-dialog 3.13.1"),
            Url(
                Const("Docs"),
                Const('https://aiogram-dialog.readthedocs.io/en/stable/index.html')
            ),
            Back(text=Const("Назад")),
            state=MainSG.docs,
        ),
        Window(
            Const("Тест"),
            SwitchTo(Const("Назад"), id="back", state=MainSG.main),
            Checkbox(
                Const("✓  Checked"),
                Const("Unchecked"),
                id="check",
                default=False,
                on_state_changed=None,
            ),
            Radio(
                Format("🔘 {item[0]}"),  # E.g `🔘 Apple`
                Format("⚪️ {item[0]}"),
                id="r_fruits",
                item_id_getter=operator.itemgetter(1),
                items=[
                    ("Apple", '1'),
                    ("Pear", '2'),
                    ("Orange", '3'),
                    ("Banana", '4'),
                ],
            ),
            Calendar(id='calendar', on_click=None),
            state=MainSG.test
        )
    )
    return main_dialog


def catalog_dialog():
    catalog_dialog = Dialog(
        Window(
            Const("Выберите понравившийся товар"),
            ScrollingGroup(
                *products_btns,
                id="goods",
                width=1,
                height=5
            ),
            Row(
                Next(Const("В корзину"), id='cart'),
                Start(Const("В меню"), id="menu", state=MainSG.main,)
            ),
            state=CatalogSG.catalog,
        ),
        Window(
            Const("Ваши товары:"),
            List(
                Format("- Товар {item}"),
                items='cart'
            ),
            Button(
                Const("Очистить"), id='clear', on_click=clear_cart
            ),
            Back(
                Const('Назад')
            ),
            state=CatalogSG.cart,
            getter=get_cart_data

        ),
    )
    return catalog_dialog


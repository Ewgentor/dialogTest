from aiogram.filters.state import State, StatesGroup


class MainSG(StatesGroup):
    main = State()
    docs = State()
    test = State()


class CatalogSG(StatesGroup):
    catalog = State()
    cart = State()

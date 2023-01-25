from aiogram.dispatcher.filters.state import State, StatesGroup


class ChoiceLanguageFSM(StatesGroup):
    choice = State()


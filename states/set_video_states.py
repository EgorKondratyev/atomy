from aiogram.dispatcher.filters.state import State, StatesGroup


class SetVideoFSM(StatesGroup):
    get_video_rus = State()
    get_video_en = State()

from aiogram.dispatcher.filters.state import State, StatesGroup


class FormFSM(StatesGroup):
    get_city = State()
    get_full_name = State()
    get_sex = State()
    get_birth_date = State()
    get_phone_number = State()
    get_postal_code = State()
    get_address = State()
    get_email = State()
    get_purpose_registration = State()

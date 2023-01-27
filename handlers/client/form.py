from aiogram.dispatcher.filters import Text
from aiogram.types import Message
from aiogram.dispatcher import FSMContext

from buttons.reply.start_buttons_reply import create_start_menu
from create_bot.bot import dp
from databases.client import UsersDB, SentencesDB
from handlers.base_handlers import get_sentences
from handlers.stop_fsm import create_keyboard_stop_fsm
from states.form_states import FormFSM


async def form_first(message: Message):
    user_db = UsersDB()
    sentences_db = SentencesDB()
    language = user_db.get_language_user(message.from_user.id)
    if not user_db.get_register_status(user_id=message.from_user.id):
        sentence = sentences_db.get_sentence(type_sentence='form_first', language=language)
        photo = sentences_db.get_photo_id(type_sentence='form_first', language=language)
        await FormFSM.get_city.set()
    else:
        sentence = sentences_db.get_sentence(type_sentence='form_passed', language=language)
        photo = sentences_db.get_photo_id(type_sentence='form_passed', language=language)
    if not photo:
        await message.answer(sentence, parse_mode='html')
    else:
        path = 'beget_tech/media/' + photo
        with open(path, 'rb') as object_photo:
            await message.answer_photo(photo=object_photo, caption=sentence, parse_mode='html')


async def form_second(message: Message, state: FSMContext):
    if len(message.text) < 255:
        async with state.proxy() as data:
            data['city'] = message.text
        user_db = UsersDB()
        sentences_db = SentencesDB()
        language = user_db.get_language_user(message.from_user.id)
        sentence = sentences_db.get_sentence(type_sentence='form_second', language=language)
        photo = sentences_db.get_photo_id(type_sentence='form_second', language=language)
        if not photo:
            await message.answer(sentence, parse_mode='html', reply_markup=create_keyboard_stop_fsm())
        else:
            path = 'beget_tech/media/' + photo
            with open(path, 'rb') as object_photo:
                await message.answer_photo(photo=object_photo, caption=sentence, parse_mode='html',
                                           reply_markup=create_keyboard_stop_fsm())
        await FormFSM.get_full_name.set()
    else:
        await message.answer('Limit of 255 characters')


async def form_third(message: Message, state: FSMContext):
    if len(message.text) < 255:
        async with state.proxy() as data:
            data['full_name'] = message.text.upper()
        user_db = UsersDB()
        sentences_db = SentencesDB()
        language = user_db.get_language_user(message.from_user.id)
        sentence = sentences_db.get_sentence(type_sentence='form_third', language=language)
        photo = sentences_db.get_photo_id(type_sentence='form_third', language=language)
        if not photo:
            await message.answer(sentence, parse_mode='html', reply_markup=create_keyboard_stop_fsm())
        else:
            path = 'beget_tech/media/' + photo
            with open(path, 'rb') as object_photo:
                await message.answer_photo(photo=object_photo, caption=sentence, parse_mode='html',
                                           reply_markup=create_keyboard_stop_fsm())
        await FormFSM.get_sex.set()
    else:
        await message.answer('Limit of 255 characters')


async def form_fourth(message: Message, state: FSMContext):
    if len(message.text) < 255:
        async with state.proxy() as data:
            data['sex'] = message.text
        user_db = UsersDB()
        sentences_db = SentencesDB()
        language = user_db.get_language_user(message.from_user.id)
        sentence = sentences_db.get_sentence(type_sentence='form_fourth', language=language)
        photo = sentences_db.get_photo_id(type_sentence='form_fourth', language=language)
        if not photo:
            await message.answer(sentence, parse_mode='html', reply_markup=create_keyboard_stop_fsm())
        else:
            path = 'beget_tech/media/' + photo
            with open(path, 'rb') as object_photo:
                await message.answer_photo(photo=object_photo, caption=sentence, parse_mode='html',
                                           reply_markup=create_keyboard_stop_fsm())
        await FormFSM.get_birth_date.set()
    else:
        await message.answer('Limit of 255 characters')


async def form_fifth(message: Message, state: FSMContext):
    if len(message.text) < 255:
        birth_date_list = message.text.split('.')

        if len(birth_date_list) == 3:
            if birth_date_list[0].isdigit() and birth_date_list[1].isdigit() and birth_date_list[2].isdigit():
                async with state.proxy() as data:
                    data['birth_date'] = message.text
                user_db = UsersDB()
                sentences_db = SentencesDB()
                language = user_db.get_language_user(message.from_user.id)
                sentence = sentences_db.get_sentence(type_sentence='form_fifth', language=language)
                photo = sentences_db.get_photo_id(type_sentence='form_fifth', language=language)
                if not photo:
                    await message.answer(sentence, parse_mode='html', reply_markup=create_keyboard_stop_fsm())
                else:
                    path = 'beget_tech/media/' + photo
                    with open(path, 'rb') as object_photo:
                        await message.answer_photo(photo=object_photo, caption=sentence, parse_mode='html',
                                                   reply_markup=create_keyboard_stop_fsm())
                await FormFSM.get_phone_number.set()
            else:
                await message.answer('The date should consist only of numbers and dots!')
        else:
            await message.answer('You entered the date of birth not by syntax\n\n'
                                 'Syntax: day.month.year | Example: 30.01.2001')
    else:
        await message.answer('Limit of 255 characters')


async def form_sixth(message: Message, state: FSMContext):
    if len(message.text) < 255:
        async with state.proxy() as data:
            data['phone_number'] = message.text
        user_db = UsersDB()
        sentences_db = SentencesDB()
        language = user_db.get_language_user(message.from_user.id)
        sentence = sentences_db.get_sentence(type_sentence='form_sixth', language=language)
        photo = sentences_db.get_photo_id(type_sentence='form_sixth', language=language)
        if not photo:
            await message.answer(sentence, parse_mode='html', reply_markup=create_keyboard_stop_fsm())
        else:
            path = 'beget_tech/media/' + photo
            with open(path, 'rb') as object_photo:
                await message.answer_photo(photo=object_photo, caption=sentence, parse_mode='html',
                                           reply_markup=create_keyboard_stop_fsm())
        await FormFSM.get_postal_code.set()
    else:
        await message.answer('Limit of 255 characters')


async def form_seventh(message: Message, state: FSMContext):
    if len(message.text) < 255:
        async with state.proxy() as data:
            data['postal_code'] = message.text
        user_db = UsersDB()
        sentences_db = SentencesDB()
        language = user_db.get_language_user(message.from_user.id)
        sentence = sentences_db.get_sentence(type_sentence='form_seventh', language=language)
        photo = sentences_db.get_photo_id(type_sentence='form_seventh', language=language)
        if not photo:
            await message.answer(sentence, parse_mode='html', reply_markup=create_keyboard_stop_fsm())
        else:
            path = 'beget_tech/media/' + photo
            with open(path, 'rb') as object_photo:
                await message.answer_photo(photo=object_photo, caption=sentence, parse_mode='html',
                                           reply_markup=create_keyboard_stop_fsm())
        await FormFSM.get_address.set()
    else:
        await message.answer('Limit of 255 characters')


async def form_eighth(message: Message, state: FSMContext):
    if len(message.text) < 255:
        async with state.proxy() as data:
            data['address'] = message.text.upper()
        user_db = UsersDB()
        sentences_db = SentencesDB()
        language = user_db.get_language_user(message.from_user.id)
        sentence = sentences_db.get_sentence(type_sentence='form_eighth', language=language)
        photo = sentences_db.get_photo_id(type_sentence='form_eighth', language=language)
        if not photo:
            await message.answer(sentence, parse_mode='html', reply_markup=create_keyboard_stop_fsm())
        else:
            path = 'beget_tech/media/' + photo
            with open(path, 'rb') as object_photo:
                await message.answer_photo(photo=object_photo, caption=sentence, parse_mode='html',
                                           reply_markup=create_keyboard_stop_fsm())
        await FormFSM.get_email.set()
    else:
        await message.answer('Limit of 255 characters')


async def form_ninth(message: Message, state: FSMContext):
    async with state.proxy() as data:
        data['email'] = message.text
    user_db = UsersDB()
    sentences_db = SentencesDB()
    language = user_db.get_language_user(message.from_user.id)
    sentence = SentencesDB().get_sentence(type_sentence='form_ninth', language=language)
    photo = sentences_db.get_photo_id(type_sentence='form_ninth', language=language)
    if not photo:
        await message.answer(sentence, parse_mode='html', reply_markup=create_keyboard_stop_fsm())
    else:
        path = 'beget_tech/media/' + photo
        with open(path, 'rb') as object_photo:
            await message.answer_photo(photo=object_photo, caption=sentence, parse_mode='html',
                                       reply_markup=create_keyboard_stop_fsm())
    await FormFSM.get_purpose_registration.set()


async def form_set(message: Message, state: FSMContext):
    async with state.proxy() as data:
        address = data['address']
        email = data['email']
        postal_code = data['postal_code']
        phone_number = data['phone_number']
        birth_date = data['birth_date']
        sex = data['sex']
        full_name = data['full_name']
        city = data['city']
        purpose_registration = message.text

    user_db = UsersDB()
    user_db.add_form_data(user_id=message.from_user.id, address=address, email=email, postal_code=postal_code,
                          phone_number=phone_number, birth_date=birth_date, sex=sex, full_name=full_name, city=city,
                          purpose_registration=purpose_registration)

    await state.finish()
    user_db = UsersDB()
    sentences_db = SentencesDB()
    language = user_db.get_language_user(message.from_user.id)
    sentence = sentences_db.get_sentence(type_sentence='form_set', language=language)
    await message.answer('✨')
    await message.answer(sentence, parse_mode='html',
                         reply_markup=await create_start_menu(language=language, sentences_db=sentences_db))


def register_form_handlers():
    sentences_db = SentencesDB()

    rus_form, en_form = get_sentences(type_sentence='form_button', sentences_db=sentences_db)
    dp.register_message_handler(form_first, Text(equals=[rus_form, en_form]), state=None)

    dp.register_message_handler(form_second, state=FormFSM.get_city)
    dp.register_message_handler(form_third, state=FormFSM.get_full_name)
    dp.register_message_handler(form_fourth, state=FormFSM.get_sex)
    dp.register_message_handler(form_fifth, state=FormFSM.get_birth_date)
    dp.register_message_handler(form_sixth, state=FormFSM.get_phone_number)
    dp.register_message_handler(form_seventh, state=FormFSM.get_postal_code)
    dp.register_message_handler(form_eighth, state=FormFSM.get_address)
    dp.register_message_handler(form_ninth, state=FormFSM.get_email)
    dp.register_message_handler(form_set, state=FormFSM.get_purpose_registration)

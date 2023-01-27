from aiogram.types import Message

from databases.client import UsersDB, SentencesDB


async def create_handler(message: Message, type_sentence: str):
    """
    Создание обработчиков без ReplyMarkup
    """
    user_db = UsersDB()
    language = user_db.get_language_user(message.from_user.id)
    sentence_db = SentencesDB()
    sentence = sentence_db.get_sentence(type_sentence=type_sentence, language=language)
    photo = sentence_db.get_photo_id(type_sentence=type_sentence, language=language)
    if not photo:
        await message.answer(sentence, parse_mode='html')
    else:
        path = 'beget_tech/media/' + photo
        with open(path, 'rb') as object_photo:
            await message.answer_photo(photo=object_photo, caption=sentence)


def get_sentences(type_sentence: str, sentences_db: SentencesDB):
    """
    Получение предложения на двух языках
    """
    rus = sentences_db.get_sentence(type_sentence=type_sentence, language=True)
    en = sentences_db.get_sentence(type_sentence=type_sentence, language=False)
    return rus, en

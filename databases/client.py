import sqlite3

from databases.auth_data import path
from log.create_logger import logger


class SentencesDB:
    """
    Сущность, которая содержит в себе предложения команд RUS/EN.
    Иначе говоря таблица, которая содержит текст всего бота: кнопок/команд/предложений на двух языках
    """
    # Атрибуты сущности:
    # 1. type_sentence - Тип кнопки или же тип предложения.
    # Например: "Кнопка 1", "Кнопка 2", "Предложение 1" и так далее.
    # 2. sentence - Сам текст, который будет содержаться в том или ином предложении/команде/кнопки.
    # 3. language - Язык текущего предложения. Так как в текущем приложении языка будет два и расширение не планируется,
    # то True - это RUS, а False - это EN
    # 4. photo_id - ID (телеграм) фото, которое устанавливает админ.
    # В текущей сущности атрибуты type_sentence and language будут выступать как составной ключ при помощи,
    # которого можно вытянуть любое sentence, но они будут повторяться, поэтому чтобы дотянуть их до NF2 был создан
    # обычный pk ;)
    def __init__(self):
        try:
            self.__base = sqlite3.connect(path)
            self.__cur = self.__base.cursor()
            self.__cur.execute('''CREATE TABLE IF NOT EXISTS sentences(
                pk INTEGER PRIMARY KEY AUTOINCREMENT,
                type_sentence VARCHAR(255),
                sentence TEXT,
                language BOOLEAN,
                photo_id TEXT 
            )''')
            self.__base.commit()
        except Exception as ex:
            logger.warning(f'Errors occurred while connecting to the sentences entity\n'
                           f'{ex}')

    def exists_sentence(self, type_sentence: str, language: bool) -> bool:
        """
        Проверка есть ли в текущей сущности таковой type_sentence с language.
        Иначе говоря проверка на то существует ли таковая команда/предложение с конкретным языком (RUS/EN)
        """
        self.__cur.execute('SELECT sentence '
                           'FROM sentences '
                           'WHERE type_sentence = ? and language = ?',
                           (type_sentence, language))
        return len(self.__cur.fetchmany(1)).__bool__()

    def add_sentence(self, type_sentence: str, sentence: str, language: bool) -> bool:
        """
        Добавление нового предложения в текущую сущность
        """
        try:
            self.__cur.execute('INSERT INTO sentences(type_sentence, sentence, language) '
                               'VALUES(?, ?, ?)',
                               (type_sentence, sentence, language))
            self.__base.commit()
            return True
        except Exception as ex:
            logger.warning(f'An error occurred when inserting data into the sentences entity\n'
                           f'{ex}')
            return False

    def update_sentence(self, type_sentence: str, sentence: str, language: bool) -> bool:
        """
        Обновление предложения, которое соответствует конкретному type_sentence и language
        """
        try:
            self.__cur.execute('UPDATE sentences '
                               'SET sentence = ? '
                               'WHERE type_sentence = ? and language = ?',
                               (sentence, type_sentence, language))
            self.__base.commit()
            return True
        except Exception as ex:
            logger.warning(f'Errors occurred in the process of updating data in the entity entity\n'
                           f'{ex}')
            return False

    def set_photo_in_sentence(self, type_sentence: str, language: bool, photo_id: str) -> bool:
        try:
            self.__cur.execute('UPDATE sentences '
                               'SET photo_id = ? '
                               'WHERE type_sentence = ? and language = ?',
                               (photo_id, type_sentence, language))
            self.__base.commit()
            return True
        except Exception as ex:
            logger.warning(f'An error occurred while adding photo_id to the sentences entity\n'
                           f'{ex}')
            return False

    def get_sentence(self, type_sentence: str, language: bool):
        self.__cur.execute('SELECT sentence '
                           'FROM sentences '
                           'WHERE type_sentence = ? and language = ?',
                           (type_sentence, language))
        sentences = self.__cur.fetchmany(1)
        if sentences:
            return sentences[0][0]
        return 0

    def get_photo_id(self, type_sentence: str, language: bool):
        self.__cur.execute('SELECT photo_id '
                           'FROM sentences '
                           'WHERE type_sentence = ? and language = ?',
                           (type_sentence, language))
        photo_id = self.__cur.fetchone()
        if photo_id:
            return photo_id[0]
        return 0

    def __del__(self):
        self.__cur.close()
        self.__base.close()


class UsersDB:
    """
    Сущность, которая будет содержать в себе всю информацию о пользователе
    """
    # Атрибуты сущности:
    # 1. user_id - первичный ключ, который представляет собой ID пользователя из телеграм.
    # 2. language - языке, который использует пользователь. Так как в текущем приложении языка будет два и
    # расширение не планируется, то True - это RUS, а False - это EN
    # 3. city - страна пользователя.
    # 4. full_name - ФИО пользователя. Особенности: Кириллица
    # 5. sex - пол пользователя.
    # 6. birth_date - дата рождения. Особенности: от 18 лет
    # 7. phone_number - номер телефона.
    # 8. postal_code - почтовый индекс.
    # 9. address - адрес пользователя. Особенности: Кириллица
    # 10. email - электронная почта пользователя.
    # 11. purpose_registration - цель регистрации.
    def __init__(self):
        try:
            self.__base = sqlite3.connect(path)
            self.__cur = self.__base.cursor()
            self.__cur.execute('''CREATE TABLE IF NOT EXISTS users(
                user_id BIGINT PRIMARY KEY,
                language BOOLEAN,
                city VARCHAR(255),
                full_name VARCHAR(255),
                sex VARCHAR(255),
                birth_date VARCHAR(255),
                phone_number VARCHAR(255),
                postal_code VARCHAR(255),
                address VARCHAR(255),
                email VARCHAR(255),
                purpose_registration TEXT,
                register_status BOOLEAN DEFAULT FALSE
            )''')
            self.__base.commit()
        except Exception as ex:
            logger.warning(f'Errors occurred while connecting to the users entity\n'
                           f'{ex}')

    def exists_user(self, user_id: int) -> bool:
        self.__cur.execute('SELECT user_id '
                           'FROM users '
                           'WHERE user_id = ?',
                           (user_id, ))
        return len(self.__cur.fetchmany(1)).__bool__()

    def get_register_status(self, user_id: int) -> bool:
        self.__cur.execute('SELECT register_status '
                           'FROM users '
                           'WHERE user_id = ?',
                           (user_id, ))
        register_status = self.__cur.fetchone()
        if register_status:
            return register_status[0]
        return False

    def add_user(self, user_id: int, language: bool) -> bool:
        """
        Добавление пользователя в текущую сущность
        """
        try:
            self.__cur.execute('INSERT INTO users(user_id, language) '
                               'VALUES(?, ?)',
                               (user_id, language))
            self.__base.commit()
            return True
        except Exception as ex:
            logger.warning(f'An error occurred when inserting data into the users entity\n'
                           f'{ex}')
            return False

    def add_form_data(self, user_id: int, city: str, full_name: str, sex: str, birth_date: str, phone_number: str,
                      postal_code: str, address: str, email: str, purpose_registration: str) -> bool:
        """
        Добавление данных о пользователе, после заполнения формы.
        """
        try:
            self.__cur.execute('UPDATE users '
                               'SET city = ?, full_name = ?, sex = ?, birth_date = ?, phone_number = ?, '
                               'postal_code = ?, address = ?, email = ?, purpose_registration = ?, register_status = ?'
                               'WHERE user_id = ?',
                               (city, full_name, sex, birth_date, phone_number, postal_code, address,
                                email, purpose_registration, True, user_id))
            self.__base.commit()
            return True
        except Exception as ex:
            logger.warning(f'An error occurred when adding data from the form to the users model\n'
                           f'{ex}')
            return False

    def get_user(self, user_id: int) -> list:
        self.__cur.execute('SELECT * '
                           'FROM users '
                           'WHERE user_id = ?',
                           (user_id, ))
        return self.__cur.fetchall()

    def get_language_user(self, user_id: int):
        self.__cur.execute('SELECT language '
                           'FROM users '
                           'WHERE user_id = ?',
                           (user_id, ))
        language = self.__cur.fetchmany(1)
        if language:
            return language[0][0]
        return 0

    def __del__(self):
        self.__cur.close()
        self.__base.close()

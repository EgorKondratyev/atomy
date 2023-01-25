# Инициализация сущностей при старте скрипта.
# Сущность Sentences содержит поля, которые определяют текст предложений/команд в боте, которые строго уточнены.
# Однако, если инициализация уже была пройдена (т.е. сущность заполнена всеми необходимыми типами команд и предложений),
# то последующие проверки никак не повлияют на целостность данных.
from databases.client import SentencesDB
from utils.translator.base_sentence import sentences

from log.create_logger import logger


def start_initialization_sentences() -> bool:
    sentences_db = SentencesDB()
    try:
        for sentence_dict in sentences:
            type_sentence = sentence_dict['type_sentence']
            language = sentence_dict['language']
            sentence = sentence_dict['sentence']

            if not sentences_db.exists_sentence(type_sentence=type_sentence, language=language):
                sentences_db.add_sentence(type_sentence=type_sentence, sentence=sentence, language=language)

        return True
    except Exception as ex:
        logger.warning(f'Errors occurred during initialization\n\n'
                       f'{ex}')
        return False

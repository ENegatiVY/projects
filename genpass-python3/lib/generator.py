# coding=utf-8
from .pinyin import PinYin
from .constants import SEQUENCES
from .config import PINYIN
# from pinyin import PinYin
# from constants import SEQUENCES
# from config import PINYIN
import time
def generator_map(data, formatter_list):
    '''generate passwords fragment by formatting function

    :param data: data will be formatted
    :param formatter_list: formatting function
    :return: strings list
    '''
    if not data or not any(data):
        return set()
    result = set()
    for format_func in formatter_list:
        if not callable(format_func):
            raise TypeError('formatter is not callable')
        result.update(map(format_func, data))
    return result


def generate_name(data, rule):
    '''built-in password generator of name
    '''
    pinyin = PinYin(PINYIN)
    pinyin.load_word()
    name_pinyin_list = list(map(pinyin.hanzi2pinyin, data))
    return generator_map(name_pinyin_list,rule)


def generate_id_string(data, rule):
    '''built-in password generator of email
    '''
    id_string = set()
    if isinstance(data, (str, )):
        id_string = data.split('@')[0]
    elif isinstance(data, SEQUENCES):
        id_string = map(lambda x: x.split('@')[0], data)
    return set(generator_map(id_string, rule))

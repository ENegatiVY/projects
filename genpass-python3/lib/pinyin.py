# coding=utf-8
import os.path


__author__ = 'cleverdeng <clverdeng@gmail.com>'
__version__ = '0.9'
__all__ = ['PinYin']


class PinYin(object):
    word_dict = {}
    dict_file = None

    def __init__(self, dict_file=''):
        self.dict_file = dict_file

    def load_word(self):
        if not os.path.exists(self.dict_file):
            print(self.dict_file)
            raise IOError('NotFoundFile')

        with open(self.dict_file) as f_obj:
            for f_line in f_obj.readlines():
                try:
                    line = f_line.split('    ')
                    self.word_dict[line[0]] = line[1]
                except:
                    line = f_line.split('   ')
                    self.word_dict[line[0]] = line[1]

    def hanzi2pinyin(self, string=''):
        result = []
        if not isinstance(string, str):
            string = string.decode('utf-8')

        for char in string:
            key = '%X' % ord(char)
            pinyin = self.word_dict.get(key, char).split()[0][:-1].lower()
            result.append(pinyin if pinyin else char)

        return result


if __name__ == '__main__':
    print(os.path.dirname(__file__), '/data/word.data')
    test = PinYin(dict_file=(os.path.dirname(__file__)+'/data/word.data'))
    test.load_word()
    string = 'Ricter是baka'
    print('in:', string)
    print('out:', ''.join(test.hanzi2pinyin(string=string)))


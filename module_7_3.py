
class WordsFinder():

    def __init__(self, *args):
        self.args = args
        file_names = []
        for ar in args:
            file_names.append(ar)

    def get_all_words(self):
        all_words = {}
        list_off = [',', '.', '=', '!', '?', ';', ':', ' - ']
        for ar in self.args:
            with open(ar, encoding='utf-8') as file:
                line_words = []
                for line in file:
                    line = line.lower()
                    split_of_line = line.split()
                    for word_in_split in split_of_line:
                        word_new = ''
                        for char in word_in_split:
                            if char in list_off:
                                continue
                            else:
                                word_new += char
                        word_in_split = word_new
                        line_words.append(word_in_split)
            all_words[ar] = line_words
        return all_words

    def find(self, word):
        dict_in = WordsFinder.get_all_words(self)
        dict_out = {}
        word = word.lower()
        for key, value in dict_in.items():
            for ind in range(len(value)):
                if value[ind] == word:
                    dict_out[key] = ind + 1
                    break
        return dict_out

    def count(self, word):
        dict_in = WordsFinder.get_all_words(self)
        dict_out = {}
        amount = 0
        word = word.lower()
        for key, value in dict_in.items():
            for ind in range(len(value)):
                if value[ind] == word:
                    amount += 1
        dict_out[key] = amount
        return dict_out


finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего


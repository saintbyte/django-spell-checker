__author__ = 'sb'
from .exceptions import DictionaryNotSet, DictionaryWrongType

try:
    from django.db.models import Model
    from django.db.models.base import ModelBase
except:
    pass


class Spell(object):
    def __init__(self, text, *args, **kwargs):
        """
        Init of Spell class

        :param text: String that need to spell
        :param dictionary: list or dictionary of right words
        """
        self.set_text(text)  # SRC Text TODO: think about reuse class object
        self.word_filter_len_minus = 2
        self.word_filter_len_plus = 2
        self.magic_num1 = -1 #user in _get_max_levenshtein_distance_dict
        self._dictionary = None
        self.word_split_char_arr = [' ', '\r', '\n', '.', ',', '!', '?']
        if kwargs.get('dictionary', None):
            self.set_dictionary(kwargs.get('dictionary', None))

    def levenshtein_distance(self, a, b):
        """
        Calculates the Levenshtein distance between a and b.
        Original code: kotbajan

        :param a: first string
        :param b: second string
        :return: Levenshtein distance as int
        """
        n, m = len(a), len(b)
        if n > m:
            # Make sure n <= m, to use O(min(n,m)) space
            a, b = b, a
            n, m = m, n
        current_column = range(n + 1)  # Keep current and previous column, not entire matrix
        for i in range(1, m + 1):
            previous_column, current_column = current_column, [i] + [0] * n
            for j in range(1, n + 1):
                add, delete, change = previous_column[j] + 1, current_column[j - 1] + 1, previous_column[j - 1]
                if a[j - 1] != b[i - 1]:
                    change += 1
                current_column[j] = min(add, delete, change)
        return current_column[n]

    def _normalize_word(self, word):
        return word.strip().lower()

    def _split(self):
        """
        Private method of class for split text to words ( with position )
        :return array of unique normalized words
        """
        unique_words = []
        cur_pos = 0
        start_pos = 0
        word = ''
        for char in self.text:
            if (char in self.word_split_char_arr):
                if word != '':
                    self.words.append((start_pos, word), )
                    unique_words.append(self._normalize_word(word))
                    word = ""
                continue
            if word == '':
                start_pos = cur_pos
            word = word + char
            cur_pos = cur_pos + 1
        unique_words = set(unique_words)
        return unique_words

    def set_dictionary(self, dictionary):
        self._dictionary = dictionary

    def set_text(self, text):
        #TODO: think about reuse class object
        self.text = text
        self.words = []
        self.result = {}

    def _in_dictionary(self, word):
        """
        Search word in dictionary
        :param word: Word for search
        :return: Boolean True if found
        """
        if isinstance(self._dictionary, (Model, ModelBase,)):
            try:
                self._dictionary.objects.get(word=word)
                return True
            except:
                return False
        if isinstance(self._dictionary, (list,)):
            if word in self._dictionary:
                return True
            return False
        raise DictionaryWrongType

    def _filter_queryset_dictionary(self, word, qs):
        """
        Some optimize queryset before calculate levenshtein distance for each

        :param word: word for that optimize
        :param qs: src queryset
        :return:
        """
        #TODO: think more about it
        start_len = len(word) - self.word_filter_len_minus
        end_len = len(word) + self.word_filter_len_plus
        if start_len < 4:
            start_len = 3
        if start_len == 3 and end_len < 5:
            end_len = 5
        #word[0]
        qs = qs.filter(length__gte=start_len)
        qs = qs.filter(length__lte=end_len)
        qs = qs.filter(first_letter=word[0])
        return qs

    def _filter_list_dictionary(self, word, lst):
        """
        Some optimize list before calculate levenshtein distance for each

        :param word: word for that optimize
        :param qs: src queryset
        :return:
        """
        return lst

    def _get_max_levenshtein_distance_dict(self,word):
         return int(len(word) / 2) - self.magic_num1

    def spell(self):
        """
        Spell Check

        :return: Dict of words with correction variants
        """
        unique_words = self._split()
        wrong_words = []
        some_optimized_iter_dictionary = None
        for word in unique_words:
            if len(word) < 3:
                continue
            if not self._in_dictionary(word):
                wrong_words.append(word)
        del unique_words
        iter_dictionary = None
        if isinstance(self._dictionary, (Model, ModelBase,)):
            iter_dictionary = self._dictionary.objects.values_list('word', flat=True)
        elif isinstance(self._dictionary, (list,)):
            iter_dictionary = self._dictionary
        else:
            raise DictionaryWrongType
        max_levenshtein_distance_dict = dict()
        result = {}
        for word in wrong_words:
            max_levenshtein_distance_dict[word] = self._get_max_levenshtein_distance_dict(word)
            result[word] = {}
            result[word]['max_levenshtein_distance'] = max_levenshtein_distance_dict[word]
            result[word]['correction_variants'] = []
        for word in wrong_words:
            if isinstance(self._dictionary, (Model, ModelBase,)):
                some_optimized_iter_dictionary = self._filter_queryset_dictionary(word,iter_dictionary)
                result[word]['count_of_levenshtein_distance_words'] = some_optimized_iter_dictionary.count()
            elif isinstance(self._dictionary, (list,)):
                some_optimized_iter_dictionary = self._filter_list_dictionary(word,iter_dictionary)
                result[word]['count_of_levenshtein_distance_words'] = len(some_optimized_iter_dictionary)
            for dict_word in some_optimized_iter_dictionary:
                ld = self.levenshtein_distance(word, dict_word)
                if ld < max_levenshtein_distance_dict[word]:
                    result[word]['correction_variants'].append((dict_word,ld),)
        self.result = result
        return result


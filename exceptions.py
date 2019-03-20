__author__ = 'sb'


class DictionaryNotSet(Exception):
    def __init__(self):
        self.code = 101
        self.message = "Dictionary not set. Set in __init__ or later by set_dictionary method."
        super().__init__()

    def __str__(self, *args, **kwargs):
        return super().__str__(*args, **kwargs)


class DictionaryWrongType(Exception):
    def __init__(self):
        self.code = 102
        self.message = "Dictionary not list or django model."
        super().__init__()

    def __str__(self, *args, **kwargs):
        return super().__str__(*args, **kwargs)

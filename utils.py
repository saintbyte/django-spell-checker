

def copyFormat(src_word, formated_word ):
    """
    Copy upcase from one string to another
    :param src_word: from where copy
    :param formated_word: for that
    :return: string formated string
    """
    cnt = 0
    len_of_formated_word = len(formated_word)
    result_str = ''
    for char in src_word:
        if cnt >= len_of_formated_word:
            break
        if char.isupper():
            result_str = result_str + formated_word[cnt].upper()
        else:
            result_str = result_str + formated_word[cnt]
        cnt = cnt + 1
    return result_str
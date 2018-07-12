def anagrams(input_word, word_list):
    """
    Returns a list of all the anagrams of input_word in word_list

    Examples:
    anagrams('tester', ['retest', 'bob', 'alice', 'street']) => ['retest, 'street']

    :param input_word The string to find anagrams
    :return The list of anagrams of input_word
    """
    anagram_list = []
    input_word_map = make_dictionary(input_word)
    for word in word_list:
        word_map = make_dictionary(word)
        if (input_word_map == word_map):
            anagram_list.append(word)
    
    return anagram_list
        
    
def make_dictionary(word) :
    word_map = {}
    i = 0
    while (i < len(word)):
        word_map[word[i]] = word_map.get(word[i],0) + 1
        i += 1
    return word_map

print(anagrams('tester', ['retest', 'bob', 'alice', 'street']))
# https://codereview.stackexchange.com/questions/147752/trie-implementation-in-python
class Node:

    def __init__(self, character):
        self.character = character if character is None else character.lower()
        self.children = dict()
        self.terminus = False

    def add(self, child_node):
        self.children[child_node.character] = child_node


class Trie:

    def __init__(self):
        self._root = Node(None)

    def insert(self, word):
        if not word:
            return
        self.__insert(self._normalize_word(word), self._root).terminus = True

    def __insert(self, word, node):
        if not word:
            return node
        elif {word[0]} & node.children.keys():
            return self.__insert(word[1:], node.children[word[0]])
        else:
            new_node = Node(word[0])
            node.add(new_node)
            return self.__insert(word[1:], new_node)

    def __contains(self, word, node):
        if not word:
            return node
        return self.__contains(word[1:], node.children[word[0]]) if \
               {word[0]} & node.children.keys() else None

    def __contains__(self, item):
        word = self._normalize_word(item)
        return self.__contains(word, self._root) is not None

    def _normalize_word(self, word):
        return word.strip().lower()

    def get_possible_words(self, word):
        word_node = self.__contains(word, self._root)
        return [] if word_node is None else \
               self.__get_possible_words(word, word_node)

    def __get_possible_words(self, word, word_node, word_list=None):
        word_list = [] if word_list is None else word_list
        if word_node.terminus:
            word_list.append(word)
        for letter in word_node.children:
            if not word_node.children[letter]:
                word_list.append(word + letter)
            else:
                self.__get_possible_words(word + letter,
                                          word_node.children[letter], word_list)
        return word_list

    def get_all_words(self):
        word_list = []
        for letter in self._root.children:
            word_list.extend(self.get_possible_words(letter))
        return word_list

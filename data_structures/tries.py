

class TrieNode:
    def __init__(self):
        self.children = dict()
        self.is_word = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def add(self, entry):
        if len(entry) is 0:
            return
        curr = self.root
        for i in range(len(entry)):
            if entry[i] not in curr.children:
                curr.children[entry[i]] = TrieNode()
            curr = curr.children[entry[i]]
        curr.is_word = True

    def __helper_ar__(self, entry, i, node):
        if i < len(entry):
            if entry[i] not in node.children:
                node.children[entry[i]] = TrieNode()
            self.__helper_ar__(entry, i+1, node.children[entry[i]])
        else:
            node.is_word = True

    def add_rec(self, entry):
        if len(entry) > 0:
            self.__helper_ar__(entry, 0, self.root)
        else:
            return

    def add_multiple(self, entries):
        for entry in entries:
            self.add(entry)

    def in_trie(self, entry):
        if len(entry) > 0:
            curr = self.root
            for i in range(len(entry)):
                if entry[i] not in curr.children:
                    return False
                curr = curr.children[entry[i]]
            return curr.is_word
        else:
            return False

    def __helper_d__(self, entry, i, node):
        if i < len(entry):
            if entry[i] in node.children:
                idel = self.__helper_d__(entry, i+1, node.children[entry[i]])
                if idel is True:
                    node.children.pop(entry[i])
                    if len(node.children.keys()) == 0:
                        del node
                        return True
                    else:
                        return False
                else:
                    return False
        else:
            if len(node.children.keys()) == 0:
                del node
                return True
            else:
                node.is_word = False
                return False

    def delete(self, entry):
        idel = self.__helper_d__(entry, 0, self.root)
        if idel:
            self.root = TrieNode()




class TrieNode:
    # Initialize your data structure here.
    def __init__(self):
        self.value = 0
        self.children = [None] * 26
        
​
class Trie:
​
    def __init__(self):
        self.root = TrieNode()
​
    # @param {string} word
    # @return {void}
    # Inserts a word into the trie.
    def insert(self, word):
        p = self.root
        for ch in word:
            idx = ord(ch) - ord('a')
            if not p.children[idx]:
                p.children[idx] = TrieNode()
            p = p.children[idx]
        p.value = 1;
                
​
    # @param {string} word
    # @return {boolean}
    # Returns if the word is in the trie.
    def search(self, word):
        p = self.root
        for ch in word:
            idx = ord(ch) - ord('a')
            if not p.children[idx]:
                return False
            p = p.children[idx]
        if p.value != 0:
            return True
        else:
            return False
                
​
    # @param {string} prefix

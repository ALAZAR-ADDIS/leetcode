class TrieNode:
    def __init__(self):
        self.child = {}
        self.weight = -1  # store the latest (largest) index


class WordFilter:

    def __init__(self, words: list[str]):
        self.root = TrieNode()

        for weight, word in enumerate(words):
            word_with_sep = word + "#"

            # Insert every rotation: suffix + "#" + word
            # Example: "apple" -> "apple#apple", "pple#apple", "ple#apple", ...
            for i in range(len(word_with_sep)):
                curr = self.root
                for c in word_with_sep[i:] + word:
                    if c not in curr.child:
                        curr.child[c] = TrieNode()
                    curr = curr.child[c]
                    curr.weight = weight  # update latest index


    def f(self, pref: str, suff: str) -> int:
        curr = self.root
        search = suff + "#" + pref
        for c in search:
            if c not in curr.child:
                return -1
            curr = curr.child[c]
        return curr.weight

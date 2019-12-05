class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        output = 0
        for word in words:
            good = True
            temp_chars = list(chars)
            for char in list(word):
                if char not in temp_chars:
                    good = False
                    break
                else:
                    temp_chars.pop(temp_chars.index(char))

            if good:
                output += len(word)

        return output
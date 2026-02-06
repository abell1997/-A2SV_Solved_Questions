

class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        char_count = {}
        for char in chars:
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
        
        total_length = 0
        
        for word in words:
            word_count = {}
            can_form = True
            
            for char in word:
                if char in word_count:
                    word_count[char] += 1
                else:
                    word_count[char] = 1
            
            for char, count in word_count.items():
                if char not in char_count or count > char_count[char]:
                    can_form = False
                    break
            
            if can_form:
                total_length += len(word)
        
        return total_length
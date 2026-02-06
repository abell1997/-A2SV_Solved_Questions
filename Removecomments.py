

class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        in_block = False
        ans = []
        newline = ""
        for line in source:
            i = 0
            n = len(line)
            while i < n:
                if not in_block and i + 1 < n and line[i] == "/" and line[i + 1] == "*":
                    in_block = True
                    i += 1
                elif in_block and i + 1 < n and line[i] == "*" and line[i + 1] == "/":
                    in_block = False
                    i += 1
                elif not in_block and i + 1 < n and line[i] == "/" and line[i + 1] == "/":
                    break
                elif not in_block:
                    newline += line[i]
                i += 1
            if not in_block and newline:
                ans.append(newline)
                newline = ""
                
        return ans
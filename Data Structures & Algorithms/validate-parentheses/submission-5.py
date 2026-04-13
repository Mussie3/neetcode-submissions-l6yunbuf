class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False
        if (")" in s and "(" in s and (s.index(")") - s.index("(")) % 2 == 0) or ("}" in s and "{" in s and (s.index("}") - s.index("{")) % 2 == 0) or ("]" in s and "[" in s and (s.index("]") - s.index("[")) % 2 == 0):
            return False
        
        symbole_dict = {
            "(" : ")",
            "{" : "}",
            "[" : "]"
        }


        i = 0
        k = 0
        while i < len(s) - k:
            if s[i] not in symbole_dict:
                return False
            if symbole_dict[s[i]] != s[i + 1]:
                if symbole_dict[s[i]] != s[len(s) - (i + 1)]:
                    return False
                else:
                    i += 1
                    k += 1
            else:
                i += 2

        
        return True
class Solution(object):
    def isNumber(self, s):
        s = s.strip()
        
        seen_digit = False
        seen_dot = False
        seen_exp = False

        for i, ch in enumerate(s):

            if ch.isdigit():
                seen_digit = True

            elif ch in ['+', '-']:
                # sign is valid only at start OR just after exponent
                if i > 0 and s[i-1] not in ['e', 'E']:
                    return False

            elif ch == '.':
                # dot cannot appear after exponent or more than once
                if seen_dot or seen_exp:
                    return False
                seen_dot = True

            elif ch in ['e', 'E']:
                # exponent must come after a number and only once
                if seen_exp or not seen_digit:
                    return False
                seen_exp = True
                seen_digit = False  # reset (must have digit after e)

            else:
                return False

        return seen_digit
    

if __name__ == '__main__':
    valid_number =Solution()
    print(valid_number.isNumber('4354;3345'))
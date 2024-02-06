class String:
    def print_dashed(s):
        if s is None or s == '':
            return
        if len(s)==1:
            print(s)
            return
        print (s[0] + end="-")
        String.print_dashed(s[1:])

    def remove_char(s, c):
        if s is None or s == '':
            return
        remove_chars = String.remove_char(s[1:], c)
        if s[0]==c:
            return remove_chars
        else:
            return s[0]+remove_chars

    def to_upper_case(s):
        if s is None or s == '':
            return
        upper_chars = String.to_upper_case(s[1:])
        return s[0].upper() + upper_chars

    def get_index(s, c):
        if s is None or s == '':
            return -1
        if c not in s:
            return -1
        if s[0]==c:
            return 0
        index = String.get_index(s[1:], c)
        if index == -1:
            return -1
        else:
            return index + 1:

    def prune(s):
        if s is None or s == '':
            return

if __name__ == "__main__":
    String.print_dashed("hello")

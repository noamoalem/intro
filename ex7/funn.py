def h_print_no_repetition_sequences(char_list, n, str):
    if n == 1:
        for i in char_list:
            print(i)
        return
    if len(str) == n:
        print(str)
        return
    elif len(str) < n:
        for i in char_list:
            if i not in str:
                str += i
                h_print_no_repetition_sequences(char_list, n, str)
                str = str[:-1]
        return
print(h_print_no_repetition_sequences(["a","b"],2,""))

def print_no_repetition_sequences(char_list, n):
    return h_print_no_repetition_sequences(char_list, n, "")
print(print_no_repetition_sequences(["a","b"],2))
# x = open("/Users/noamoalem/Downloads/ex5examplefiles/word_list.txt")
# p = x.readlines()
# print(p)
#
# print(run_wordsearch([0,"/Users/noamoalem/Downloads/ex5examplefiles/word_list.txt",
# "/Users/noamoalem/Downloads/ex5examplefiles/mat.txt" ,
# "/Users/noamoalem/Downloads/ex5examplefiles/output_noa_file","udlrwxyz"]))
# #print(write_output_file(find_words_in_matrix(read_wordlist_file("word_list.txt"),read_matrix_file("mat.txt"),"xyudrzw"),"resoltss"))
# #print(find_words_in_matrix(read_wordlist_file("word_list.txt"),read_matrix_file("mat.txt"),"xyudrzw"))
# #print(find_words_diagonal(read_wordlist_file("word_list.txt"),read_matrix_file("mat.txt"),"xyzw"))
# #print(find_words_left_right(read_wordlist_file("word_list.txt"),read_matrix_file("mat.txt"),"rl"))
# #print(find_words_up_down(read_wordlist_file("word_list.txt"),read_matrix_file("mat.txt"),"ud"))
# #print(read_matrix_file("mat.txt"))
# #print(read_wordlist_file("word_list.txt"))
# # print(check_input_args(["/Users/noamoalem/Downloads/ex5examplefiles/word_list.txt",
# # "/Users/noamoalem/Downloads/ex5examplefiles/mat.txt" ,
# # "/Users/noamoalem/Downloads/ex5examplefiles/output_file","xz"]))
# if __name__ == "__main__":
#     check_input_args([0,"/Users/noamoalem/Downloads/ex5examplefiles/word_list.txt",
# "/Users/noamoalem/Downloads/ex5examplefiles/mat.txt" ,
# "/Users/noamoalem/Downloads/ex5examplefiles/output_file","xz"])
#
# print(find_words_in_matrix(['long', 'short', 'can', 'toe', 'poet', 'crop', 'dog', 'cat', 'ants', 'apple', 'cake'],[['a', 'p', 'p', 'l', 'e'], ['a', 'g', 'o', 'd', 'o'], ['n', 'n', 'e', 'r', 't'], ['g', 'a', 't', 'a', 'c'], ['m', 'i', 'c', 's', 'r']],'u'))
def acc(word_lst):
    results = dict()
    print(bool(word_lst))
    if not word_lst :#or not matrix:
        return None

    for word in word_lst:
        results[word] = 0
    print(results)
print(acc(['long', 'short', 'can', 'toe', 'poet', 'crop', 'dog', 'cat', 'ants', 'apple', 'cake']))
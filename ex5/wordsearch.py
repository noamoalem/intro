#################################################################
# FILE : wordsearch.py
# WRITER : noa moalem , noamoa , 208533554
# EXERCISE : intro2cs ex5 2019
# DESCRIPTION: we asked to write code that find word in wordsearch
# ################################################################
import sys
DIRECTIONS = ['d', 'l', 'r', 'u', 'w', 'x', 'y', 'z']
LEN_OF_PARAMETER_LST = 5
UP = "u"
DOWN = "d"
LEFT = "l"
RIGHT = "r"
UP_RIGHT = "w"
UP_LEFT = "x"
DOWN_RIGHT = "y"
DOWN_LEFT = "z"

def check_input_args(args):
    """This function check that each of the arguments that the program
    got are valid"""

    flag = [True, True, True]
    if len(args) != LEN_OF_PARAMETER_LST:
        return "invalid input: only 4 items required"

    for i in args[4]:
        if i not in DIRECTIONS:
            flag[2] = False

    try:
       words_lst = open(args[1])
       try:
           matrix_file = open(args[2])
       except:
           flag[1] = False
    except:
        flag[0] = False

    if all(flag): #all the argoments valid
        return None
    if not flag[0]:
        return "words_file doesn't exist"
    if not flag[1]:
        return "matrix_file doesn't exist"
    if not flag[2] :
        return "invalid search directions"


def read_wordlist_file(filename):
    """This function create list of words from a given word file"""

    with open(filename) as file: #craet list of words
        words_lst = file.read().splitlines()
    if not words_lst:
        return None
    return words_lst


def read_matrix_file(filename):
    """This function create list of list of the matrix letters"""

    finallst = []
    with open(filename) as file:
        for line in file:
            smallist = line.strip().split(',')
            finallst.append(smallist)
    if not finallst:
        return None
    return finallst


def find_str_in_word(word,string):
    """This function find how many times string appears in word"""
    count = 0
    if string in word:
        while string in word:
            index = word.find(string)
            count += 1
            word = word[index+1:]

    return count


def find_words_up_down(word_list, matrix, direction):
    """This function check if a word from a given word list is in the
    matrix col from up and down"""
    col = []
    results = dict()

    if not word_list or not matrix: # means the matrix or word list empty
        return None

    for word in word_list:# creat a dictionary that will include the results
        results[word] = 0

    for i in range(len(matrix[0])):
        col.append([])

    #the next lines creat a list of the matrix columns as string
    for lst in matrix:
        for i in range(len(matrix[0])):
            col[i].append(lst[i])

    for i in range(len(col)):
        col[i] = "".join(col[i]) # now each one of the matrix columns are
                                 # list of one string

    if DOWN in direction:
        for word in word_list:
            for i in col: # find how many times word appears in matrix col
                results[word] += find_str_in_word(i,word)

    if UP in direction:
        for i in range(len(col)):# revers of the matrix columns as string
            col[i] = col[i][::-1]
        for word in word_list:
            for i in col: # find how many times word appears in matrix col
                results[word] += find_str_in_word(i, word)

    return results


def find_words_left_right(word_list, matrix, direction):
    """This function check if a word from a given word list is in the
    matrix rows from right and left"""
    results = dict()
    row = []

    if not word_list or not matrix: # means the matrix or word list empty
        return None

    for word in word_list: #creat a dictionary that will include the results
        results[word] = 0

    # the next lines create a list of the matrix row as string
    for i in range(len(matrix)):
        row.append([])

    for rows in matrix:
        for i in range(len(rows)):
            row[i].append(rows[i])

    for i in range(len(matrix)): # turn the list row items to string
        row[i] = "".join(row[i])

    if RIGHT in direction:

        for word in word_list:
            for row in matrix: # find how many times word appears in matrix row
                results[word] += find_str_in_word(row, word)

    if LEFT in direction:
        for i in range(len(matrix)):# revers of the matrix rows as string
            matrix[i] = matrix[i][::-1]
        for word in word_list:
            for row in matrix: # find how many times word appears in matrix row
                results[word] += find_str_in_word(row, word)

    return results


def find_diagonals_matrix(matrix):
    """This function create list of list of the matrix diagonal"""

    if matrix == []:
        return None
    small_lst =[]
    diagonal_right_up_left_down = []
    diagonal_right_down_left_up = []
    m = len(matrix) #number of row
    n = len(matrix[0]) #number of col

    # the next lines find all the diagonal of matrix right up
    for k in range(0, m): #k run on matrix row from the first col
        i = k #i for ros
        j = 0 #j for col
        while i >= 0 and j <= n-1: #so we wont pass the first row
            small_lst.append((matrix[i][j]))
            i -= 1
            j += 1
        diagonal_right_up_left_down.append(small_lst)
        #adding the current diagonal
        small_lst = [] #so each time we add a list of the element on the
        # diagonal to the big list

    for k in range(1, n): #k run on matrix col from the last row
        i = m-1 #i for ros
        j = k   #j for col
        while j <= n-1 and i >= 0: #so we wont pass the last col
            small_lst.append((matrix[i][j]))
            i -= 1
            j += 1
        diagonal_right_up_left_down.append(small_lst)
        #adding the current diagonal
        small_lst = []

    # the next lines find all the diagonal of matrix right down
    for k in range(0, n): #k run on matrix col
        i = 0 #i for ros
        j = k #j for col
        while j <= n-1 and i <= m-1: #so we wont pass the last col/row
            small_lst.append(matrix[i][j])
            i += 1
            j += 1
        diagonal_right_down_left_up.append(small_lst)
        small_lst = []

    for k in range(1, m): #k run on matrix row
        i = k #i for ros
        j = 0 #j for col
        while j <= n-1 and i <= m-1:
            small_lst.append(matrix[i][j])
            i += 1
            j += 1
        diagonal_right_down_left_up.append(small_lst)
        small_lst = []

    return diagonal_right_down_left_up, diagonal_right_up_left_down


def find_words_diagonal(word_list,matrix,direction):
    """This function find words in the diagonals of matrix"""

    results = dict()
    all_matrix_diagonal = find_diagonals_matrix(matrix)
    diagonal_right_down_left_up = all_matrix_diagonal[0]
    diagonal_right_up_left_down = all_matrix_diagonal[1]

    if not word_list or not matrix:
        return None

    for word in word_list: # creat a dictionary that will include the results
        results[word] = 0

    #creat two lists of the matrix diagonal as string speratly
    for i in range(len(diagonal_right_down_left_up)):
        diagonal_right_down_left_up[i] = "".join(diagonal_right_down_left_up[i])

    for i in range(len(diagonal_right_up_left_down)):
        diagonal_right_up_left_down[i] = "".join(diagonal_right_up_left_down[i])

    if DOWN_RIGHT in direction:
        for word in word_list: #find the words
            for i in diagonal_right_down_left_up:
                # find how many times word appears in matrix diagonal
                results[word] += find_str_in_word(i, word)

    if UP_LEFT in direction:
        for i in range(len(diagonal_right_down_left_up)):
            # revers of the matrix diagonals as string
            diagonal_right_down_left_up[i]=diagonal_right_down_left_up[i][::-1]
        for word in word_list:
            for i in diagonal_right_down_left_up:
                #find how many times word appears in matrix diagonal
                results[word] += find_str_in_word(i, word)

    if UP_RIGHT in direction:
        for word in word_list:
            for i in diagonal_right_up_left_down:
                #find how many times word appears in matrix diagonal
                results[word] += find_str_in_word(i, word)

    if DOWN_LEFT in direction:
        for i in range(len(diagonal_right_up_left_down)):
            # revers of the matrix diagonals as string
            diagonal_right_up_left_down[i] = diagonal_right_up_left_down[i][::-1]
        for word in word_list:
            for i in diagonal_right_up_left_down:
                results[word] += find_str_in_word(i, word)

    return results


def find_words_in_matrix(word_list, matrix, directions):
    """This function find the word in matrix according to a given directions"""

    results = dict()

    if not word_list or not matrix:
        return None

    for word in word_list:
        results[word] = 0

    if DOWN or UP in directions: #search words up/down
        dict_u_d = find_words_up_down(word_list, matrix, directions)
        for word in results:
            results[word] += dict_u_d[word] #update the results

    if LEFT or RIGHT in directions: #search words right/left
        dict_l_r = find_words_left_right(word_list, matrix, directions)
        for word in results:
            results[word] += dict_l_r[word]

    if UP_LEFT or DOWN_RIGHT or UP_RIGHT or DOWN_LEFT in directions:
        # search words diagonaly
        dict_diagonal = find_words_diagonal(word_list, matrix, directions)
        for word in results:
            results[word] += dict_diagonal[word]

    #the next lines convert the results from dictionary into list of tuples
    final_result = zip(results.keys(), results.values())
    final_result = list(final_result)
    very_final_result =[]
    for i in final_result:
        if i[1] != 0:
            very_final_result.append(i)
    return very_final_result


def write_output_file(results, output_filename):
    """This function create/write to file the results"""

    if results == None:
        result_file = open(output_filename, "w") #empty file
        return result_file

    list_of_results = []
    for i in range(len(results)): #creat list of the results as list of lists
        list_of_results.append([])

    for i in range(len(results)):
        list_of_results[i].append(results[i][0])
        list_of_results[i].append(",")
        list_of_results[i].append(str(results[i][1]))

    result_file = open(output_filename, "w")
    for item in range(len(list_of_results)):
        if list_of_results[item][2] != "0": #the word found
            result_file.writelines((list_of_results[item]))
            result_file.write("\n")

    result_file.close()


def run_wordsearch(args):
    """This function get a file of words, matrix find all the word in the
     matrix and create file with the results, return the location of the file"""

    if check_input_args(args) != None:  # one of the arguments invalid
        return check_input_args(args)

    word_list = read_wordlist_file(args[1])  # create list of the word
    matrix = read_matrix_file(args[2])  # create the matrix
    # find words in matrix
    results = find_words_in_matrix(word_list, matrix, args[4])
    write_output_file(results, args[3])  # create the results file
    res = open(args[3])
    res.close()

    if not word_list or not matrix :# means the matrix or word list empty
        return "the matrix/word list are empty"

    return "the location of the results file  is:", res

if __name__ == "__main__":
    run_wordsearch(sys.argv)

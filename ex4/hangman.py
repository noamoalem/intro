#############################################################
# FILE :hangman.py
# WRITER : noa moalem , noamoa , 208533554
# EXERCISE : intro2cs ex4 2019
# DESCRIPTION: we asked to build the game hangman
##############################################################

from hangman_helper import *
CHAR_A = 97

def letter_to_index(letter):
    """Return the index of the given letter in an alphabet list. """

    return ord(letter.lower()) - CHAR_A


def index_to_letter(index):
    """Return the letter corresponding to the given index. """

    return chr(index + CHAR_A)


def histogram(n, num_list):
    """This function find the histogram of list """

    histlist = []
    for i in range(n): #creats a list of n members = 0
        histlist.append(0)

    for i in range(0, n):
        for numinlist in num_list:
            if i == numinlist: #count how many tims number is in num_list
                histlist[i] += 1
    return histlist


def create_patern(word):
    """This function create the pattern of a given word"""

    pattern_the_word = ""
    for i in range(len(word)):
        pattern_the_word += "_"
    return pattern_the_word


def finding_max_letter(histogram_of_letters_by_num):
    """This function get a list of histogram of a-z by numbers and find the
    letters that appears most times and return a list of those letters"""

    max_letter_list_by_letter_index = []
    max_letter_list = [] #the final list we need
    max_of_histogram_of_let = max(histogram_of_letters_by_num)

    for i in range(len(histogram_of_letters_by_num)):
    # the next line find all index in histogram that eqal to max_of_histogram
        if histogram_of_letters_by_num[i] == max_of_histogram_of_let:
            max_letter_list_by_letter_index.append(i) # adding the index of max
                                                      # let from a-z to list
    # the next lines turn tne index to letter
    for j in max_letter_list_by_letter_index:
        max_letter_list.append(index_to_letter(j))

    return max_letter_list


def find_let_in_word(let, word):
    """This function fined if a given letter is in the word and give a list
       of the index of this letter in the word"""

    lst_of_index_let_in_word =[]
    for i in range(len(word)):
        if let == word[i]:
            lst_of_index_let_in_word.append(i)
    return lst_of_index_let_in_word


def check_word_fit_pattern(word, pattern):
    """This function check if word can fit to a given pattern"""

    counter_if_the_same = 0
    for i in pattern:
        if i != "_":
            lst1 = find_let_in_word(i, word)#list of all the index of i in word
            lst2 = find_let_in_word(i, pattern)#list of all the index of i in
                                               # pattern

            if lst1 != lst2: # the word not fit pattern
                counter_if_the_same += 1

    if counter_if_the_same == 0: # the word fit pattern
        return word


def check_let_in_word(word, wrong_let):
    """This function check if a given word include the letters in a given
       list of the wrong letters"""

    count = 0
    for let in wrong_let:
        if let in word:
            count +=1

    if count == 0: # the word not indlude letters from the wrong list
        return word


def filter_words_list(words, pattern, wrong_guess_lst):
    """This function filter a given list of words to list of the words
       that may fit"""

    lst_optional_words = []
    for word in words:
        if len(word) == len(pattern):
            if len(wrong_guess_lst) != 0:
                flag = check_let_in_word(word, wrong_guess_lst)
                if flag: # means we have word that not include
                         # letters from the wrong letters list
                    lst_one_word_optional = check_word_fit_pattern \
                        (word, pattern)
                    if lst_one_word_optional: # means we have a word that
                                              # also fit the pattern
                        lst_optional_words.append(lst_one_word_optional)
            else:
                lst_one_word_optional = check_word_fit_pattern(word, pattern)
                if lst_one_word_optional: # means the word fit the pattern
                    lst_optional_words.append(lst_one_word_optional)

    return lst_optional_words

def choose_letter(words, pattern):
    """This function find the letter that appears most time in a list
       of word and also not in the pattern """

    list_of_all_leterrs = []
    list_of_leterrs_by_index = []

    for word in words:
        for let in word:
            list_of_all_leterrs.append(let) # creats list of all the letters
                                            # in words

    for let in list_of_all_leterrs:
        if let not in pattern: # we need this letter
            list_of_leterrs_by_index.append(letter_to_index(let))
    # the next line creats histogram of the letter that can fit to pattern
    # and wrong list
    histogram_of_letters = histogram(26, list_of_leterrs_by_index)
    # thr next line creats list of the max letters
    list_of_the_max_letters = finding_max_letter(histogram_of_letters)

    return random.choice(list_of_the_max_letters)


def update_word_pattern(word, pattern, letter):
    """This function update the pattern with letter"""

    pattern_as_list = list(pattern)
    for let in range(len(word)):
        if word[let] == letter:
            pattern_as_list[let] = letter

    pattern = "".join(pattern_as_list)
    return pattern


def run_single_game(words_list):
    """This function run one game"""

    the_word = get_random_word(words_list)
    lst_of_wrong_let = []
    error_counter = 0
    msg_for_user = DEFAULT_MSG
    pattern_the_word = create_patern(the_word)  #creat the pattern

    while error_counter < MAX_ERRORS and the_word != pattern_the_word:
        # means we didn't won/lose
        display_state(pattern_the_word, error_counter, lst_of_wrong_let,
                      msg_for_user)

        number, choice = get_input()
        if number == LETTER: # the input is letter
            # the next lines check that the input letter is as needed to be
            if len(choice) != 1 or not (choice.islower()) or type(choice)!=str:
                msg_for_user = NON_VALID_MSG

            elif choice in lst_of_wrong_let:
                msg_for_user = ALREADY_CHOSEN_MSG + choice

            elif choice in pattern_the_word:
                msg_for_user = ALREADY_CHOSEN_MSG  + choice

            elif choice in the_word:
                pattern_the_word = update_word_pattern(the_word,
                                                    pattern_the_word, choice)
                msg_for_user = DEFAULT_MSG

            else:
                error_counter += 1
                lst_of_wrong_let.append(choice)
                msg_for_user = DEFAULT_MSG


        elif number == HINT: # the input is request for hint
            filterd_list = filter_words_list(words_list, pattern_the_word,
                              lst_of_wrong_let) #creats list of filterd words
            hint_letter = choose_letter(filterd_list, pattern_the_word)
            msg_for_user = HINT_MSG  + hint_letter

    if the_word == pattern_the_word:
        msg_for_user = WIN_MSG
    else:
        msg_for_user = LOSS_MSG + the_word

    display_state(pattern_the_word, error_counter, lst_of_wrong_let,
                  msg_for_user, True)


def main():
    lst_of_words = load_words()
    run_single_game(lst_of_words)
    number, choice = get_input()
    while number == PLAY_AGAIN and choice:
        run_single_game(lst_of_words)
        number, choice = get_input()


if __name__ =="__main__":
    main()
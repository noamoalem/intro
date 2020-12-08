#############################################################
# FILE : wave_editor.py
# WRITERS : Nir Amzaleg & Noa Moalem , nir_amzaleg noamoa
# EXERCISE : intro2cs ex6 2019
# DESCRIPTION: Editing a wave file. This program include 3
# different options to work with wave file. The first is to change
# an exist wave file ( volume it up/down , low pass filtered it,
# revers it and more...). The second option is to unit 2 wave files
# to a new one and the thirds one is to compose a new tune.
# the program allow the user to save the changes as a new file.
#############################################################

import math
import numpy
import scipy
from wave_helper import *
ENTRANCE_MENU = "Hello, please chose one of the following choice: " \
                " 1 - changing the wav file" \
                " 2 - unit 2 files" \
                " 3 - composing tune" \
                " 4 - exit "
TRANSITION_MENU = "Would you like to " \
                  " 1 - Save the wav file" \
                  " 2 - Changing the wav file"
CHANGE_FILE_MENU = "Which operation would you like to do?" \
                   " 1 - revers the audio" \
                   " 2 - accelerate the audio speed" \
                   " 3 - slow the audio speed" \
                   " 4 - volume up" \
                   " 5 - volume down" \
                   " 6 - low pass filter"

POSSIBLE_INPUT_ENTRANCE = ["1", "2", "3", "4"]
POSSIBLE_INPUT_TRANSITION_MENU = ["1", "2"]
POSSIBLE_INPUT_CHANGE_FILE = ["1", "2", "3", "4", "5", "6"]
FIRST_CALL_OF_CHANGE_WAV_FUN = ""
DEFAULT_SAMPLE_RATE = 2000
MAX_VOLUME = 32767
MIN_VOLUME = -32768
VOLUME_CHANGE_NUM = 1.2
REVERSE_AUDIO = 1
ACCELERATE_AUDIO_SPEED = 2
SLOW_AUDIO_SPEED = 3
VOLUME_UP = 4
VOLUME_DOWN = 5
LOW_PASS_FILTER = 6


def get_input(message):
    """ Gets input from user and check if it valid, else ask again"""
    choice = input(message)
    if message == ENTRANCE_MENU:
        while choice not in POSSIBLE_INPUT_ENTRANCE:
            choice = input(message)
    elif message == TRANSITION_MENU:
        while choice not in POSSIBLE_INPUT_TRANSITION_MENU:
            choice = input(message)
    elif message == CHANGE_FILE_MENU:
        while choice not in POSSIBLE_INPUT_CHANGE_FILE:
            choice = input(message)
    return int(choice)


def reverse_audio(audio_data):
    """This function revers a given list"""

    reversd_audio_lst = audio_data[::-1]
    return reversd_audio_lst


def accelerate_audio_speed(audio_data):
    """This function create list of the even index from a given list"""

    audio_double_speed = []
    for i in range(0, len(audio_data), 2):
        audio_double_speed.append(audio_data[i])
    return audio_double_speed


def slow_audio_speed(audio_data):
    """This function create list with the average of two consecutive items
     from a given list"""

    audio_slow_speed = []
    for i in range(len(audio_data)):
        audio_slow_speed.append(audio_data[i])
        if i < len(audio_data) - 1:
            # The next lines calculate the average of each consecutive items of
            # the original list and add it to the new list
            average_of_two_items = [
                int((audio_data[i][0] + audio_data[i + 1][0]
                     ) / 2),
                int((audio_data[i][1] + audio_data[i + 1][1]) / 2)]
            audio_slow_speed.append(average_of_two_items)
    return audio_slow_speed


def volume_up(audio_data):
    """This function double in 1.2 each number in a given list """

    audio_volume_up = []
    for i in range(len(audio_data)):
        audio_volume_up.append([])  # creat list of empty lists
    for i in range(len(audio_data)):
        for item in audio_data[i]:
            item_up = int(item * VOLUME_CHANGE_NUM)  # multiply the number
            # check the number after multiplication is in the range
            if MIN_VOLUME <= item_up <= MAX_VOLUME:
                audio_volume_up[i].append(item_up)
            elif item_up >= MAX_VOLUME:
                audio_volume_up[i].append(MAX_VOLUME)
            else:
                audio_volume_up[i].append(MIN_VOLUME)
    return audio_volume_up


def volume_down(audio_data):
    """This function divide in 1.2 each number in a given list """
    audio_volume_down = []
    for i in range(len(audio_data)):
        audio_volume_down.append([])  # creat list of empty lists
    for i in range(len(audio_data)):
        for item in audio_data[i]:
            item_up = int(item / VOLUME_CHANGE_NUM)  # divide the number
            audio_volume_down[i].append(item_up)
    return audio_volume_down


def low_pass_filter(audio_data):
    """ This function get the audio data and low pass filter list"""

    new_audio_data = []
    for index in range(len(audio_data)):
        if index == 0:
            inner_list = [int((audio_data[index][0] + audio_data[index + 1][0])
            / 2), int((audio_data[index][1] + audio_data[index + 1][1]) / 2)]
        elif index == len(audio_data) - 1:
            inner_list = [int((audio_data[index][0] + audio_data[index - 1][0])
            /2), int((audio_data[index][1] + audio_data[index - 1][1]) / 2)]
        else:
            inner_list = [int((audio_data[index - 1][0] + audio_data[index][0]
             + audio_data[index + 1][0]) / 3), int((audio_data[index - 1][1]
             + audio_data[index][1] + audio_data[index + 1][1]) / 3)]
        new_audio_data.append(inner_list)
    return new_audio_data


def change_wav(ask_for_file, in_edit_file):
    """ This function makes 6 different changes in the file"""
    if ask_for_file:
        file_name = input("please enter file to change: ")
        while load_wave(file_name) == -1:
            file_name = input("please enter valid file:")
        frame_rate, audio_data = load_wave(file_name)
    else:
        frame_rate, audio_data = in_edit_file
    choice = get_input(CHANGE_FILE_MENU)
    new_audio = None
    if choice == REVERSE_AUDIO:
        new_audio = reverse_audio(audio_data)
    elif choice == ACCELERATE_AUDIO_SPEED:
        new_audio = accelerate_audio_speed(audio_data)
    elif choice == SLOW_AUDIO_SPEED:
        new_audio = slow_audio_speed(audio_data)
    elif choice == VOLUME_UP:
        new_audio = volume_up(audio_data)
    elif choice == VOLUME_DOWN:
        new_audio = volume_down(audio_data)
    elif choice == LOW_PASS_FILTER:
        new_audio = low_pass_filter(audio_data)
    return frame_rate, new_audio


def get_check_input_union_files():
    """This function ask the user for two fies to union then check that if the
    files valid and ha space between their names"""

    files_names = input("please enter two files to union:")
    space = files_names.find(" ")
    file_one = files_names[:space]
    file_two = files_names[space+1:]
    while space == -1 or load_wave(file_one) == -1 or load_wave(file_two) ==-1:
        # no space between file names / invalid files
        if space == -1:
            files_names = input("please enter two files to union:")
            space = files_names.find(" ")
        elif load_wave(file_one) == -1 or load_wave(file_two) == -1:
            files_names = input("please enter two valid files to union:")
            space = files_names.find(" ")
            file_one = files_names[:space]
            file_two = files_names[space + 1:]

    return files_names


def find_gcd(num_one,num_two):
    """This function find the GCD of two given numbers"""

    gcd = math.gcd(num_one,num_two)
    return gcd


def find_short_list(lst_one,lst_two):
    """This function find the shortest list between two list, return tuple
      (short list,long list)"""

    if len(lst_one) > len(lst_two):
        return lst_two,lst_one
    return lst_one,lst_two


def average_of_two_items_lst(lst_one,lst_two):
    """This function create list of lists of the average of each item in two
    lists of lists if lst_one = [10,10],[20,20],[30,30], lst_two = [1,1],[2,2]
     the result is [[5,5],[11,11],[30,30]]"""

    final_lst = []
    if len(lst_one) == len(lst_two):
        for i in range(len(lst_one)): # adding each two items with the same
                                      # index and divide them by two
            final_lst.append([int((lst_one[i][0] + lst_two[i][0])/2),
                              int((lst_one[i][1] + lst_two[i][1])/2)])
    else:
        short_lst = find_short_list(lst_one, lst_two)[0]
        long_lst = find_short_list(lst_one, lst_two)[1]

        for i in range(len(short_lst)):# adding each two items with the same
                       # index till the short lise ends and divide them by two
            final_lst.append([int((short_lst[i][0] + long_lst[i][0])/2),
                              int((short_lst[i][1] + long_lst[i][1])/2)])
        # add what left from the long list to the final list
        for i in long_lst[len(short_lst):]:
            final_lst.append(i)

    return final_lst


def union_files(files_names):
    """This function gets two files and make them into one, the function return
     the frame rate and the audio data of the united file"""

    lst_wanted_samples = []
    space = files_names.find(" ")
    # create tupels of each file information (frame_rate,[audio_data])
    file_one = load_wave(files_names[:space])
    file_two = load_wave(files_names[space+1:])
    gcd = find_gcd(file_one[0], file_two[0]) # find the GCD of the frame rates
    frame_rate = min(file_one[0], file_two[0])

    if file_one[0] == file_two[0]: # the files has same sample rate
        # make list of the average of each item in two lists of audio data
        final_lst = average_of_two_items_lst(file_one[1], file_two[1])

    else: # the files has diffrent sample rate
        if file_one[0] > file_two[0]:
            small_sample_rate = file_two[1]
            big_sample_rate = file_one[1]
            samples_to_take_from = int(file_one[0] / gcd)
            amount_of_samples_to_take = int(file_two[0] / gcd)
        elif file_one[0] < file_two[0]:
            small_sample_rate = file_one[1]
            big_sample_rate = file_two[1]
            samples_to_take_from = int(file_two[0] / gcd)
            amount_of_samples_to_take = int(file_one[0] / gcd)

        lst_to_change = big_sample_rate
        lst_no_change = small_sample_rate
        # in the next lines we adding amount_of_samples_to_take from each
        # samples_to_take_from in lst_to_change to lst_wanted_samples
        for i in range(0, len(lst_to_change), samples_to_take_from):
            for j in range(amount_of_samples_to_take):
                if i+j < len(lst_to_change):
                    # so we won't get out of the list to chang index
                    lst_wanted_samples.append(lst_to_change[j+i])
        # make list of the average of each item in two lists of audio data
        final_lst = average_of_two_items_lst(lst_wanted_samples, lst_no_change)

    return frame_rate, final_lst


def entrance_menu():
    """ This function display the entrance menu"""
    change_wav_file = 1
    unit_wav_file = 2
    compose_tune_file = 3
    exit_program = 4
    optional_wav_file = (None, None)
    choice = get_input(ENTRANCE_MENU)
    if choice == change_wav_file:
        optional_wav_file = change_wav(True, FIRST_CALL_OF_CHANGE_WAV_FUN)
    elif choice == unit_wav_file:
        files_names = get_check_input_union_files()
        optional_wav_file = union_files(files_names)
    elif choice == compose_tune_file:
        optional_wav_file = compose_tune()
    elif choice == exit_program:
        return False, (False , False)
    transition_menu_choice = get_input(TRANSITION_MENU)
    return transition_menu_choice, optional_wav_file


def samples_per_cycle(letter):
    """ Calculate the samples per cycle of given freuency"""
    sample_rate = DEFAULT_SAMPLE_RATE
    if letter == "Q":
        return False
    elif letter == "A":
        frequency = 440
    elif letter == "B":
        frequency = 494
    elif letter == "C":
        frequency = 523
    elif letter == "D":
        frequency = 587
    elif letter == "E":
        frequency = 659
    elif letter == "F":
        frequency = 698
    elif letter == "G":
        frequency = 784
    else:
        frequency = 1
    return sample_rate/frequency


def single_sample(i, letter):
    """ Assist function that calculate a single sample"""
    samples_per_cyc = samples_per_cycle(letter)
    if not samples_per_cyc:
        return 0
    return int(MAX_VOLUME * math.sin(math.pi * 2 * i / samples_per_cyc))


def compose_tune():
    """ Compose tune from text file"""
    results = []
    flag = True
    text_file = input("Please enter the file name: ")
    while flag:
        try:
            open(text_file)
            flag = False
        except FileNotFoundError:
            text_file = input("Please enter new file name: ")
    with open(text_file) as file:
        lst_of_file_text = file.readlines()
        text = " ".join(lst_of_file_text)
        temporary_lst = text.split(" ")
        lst = [x for x in temporary_lst if x != ""]
        char_index = 0
        for char in lst[:-1:2]:
            time = int(lst[char_index + 1])
            for i in range(0, 125 * time):
                i_sample = single_sample(i, char)
                results.append([i_sample, i_sample])
        char_index += 1
    return DEFAULT_SAMPLE_RATE, results


def main():
    """ Run the program """
    save_wav_file = 1
    change_wav_file = 2
    ask_for_file_name = True
    choice = 2
    while choice:  # loop the entrance menu until the user ask to out(4)
        choice, optional_wav_file = entrance_menu()
        frame_rate, audio_data = optional_wav_file
        if not choice:
            break
        while choice == change_wav_file:
            # loop the transition menu until user ask to save the file
            ask_for_file_name = False
            frame_rate, audio_data = change_wav(ask_for_file_name,
                                                optional_wav_file)
            choice = get_input(TRANSITION_MENU)
        if choice == save_wav_file:
            file_name = input("please enter name for the new file: ")
            file = save_wave(frame_rate, audio_data, file_name)
            if file == -1:
                print("file not saved")


if __name__ == "__main__":
     main()
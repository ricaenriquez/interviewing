"""
Goal: from a list of numbers, return the sequence of numbers in order
that produces the largest sum
"""

import numpy as np
np.random.seed(4)

numbers = np.random.randint(-20, 20, size = 100)

def brute_force(number_array):
    save_these = []
    starting_indx = []
    ending_indx = []
    for i in range(len(number_array)):
        for j in range(i+1, len(number_array)):
            save_these.append(sum(number_array[i:j]))
            starting_indx.append(i)
            ending_indx.append(j)
            
    max_sum_indx = np.argmax(np.array(save_these))

    #np.argmax finds the index in the array with the largest value
    start_here = starting_indx[max_sum_indx]
    end_here = ending_indx[max_sum_indx]

    max_sum_sequence = number_array[start_here : end_here]
    return max_sum_sequence

def clever(number_array):
    current_sum = 0
    current_start = 0
    current_end = 0

    biggest_sum = 0
    biggest_start = 0
    biggest_end = 0

    N = len(number_array)

    for i in range(N):
        current_sum += number_array[i]

        if current_sum > biggest_sum:
            biggest_sum = current_sum
            biggest_start = current_start
            biggest_end = current_end = i + 1

        elif current_sum < 0:
            current_start = i+1
            current_sum = 0

    return number_array[biggest_start : biggest_end]

def test_cleverness(trials):
    for ii in range(trials):
        test_numbers = np.random.randint(-100, 100, size=np.random.randint(10,1000))
        if np.all(brute_force(test_numbers)) == np.all(clever(test_numbers)):
            print True

        else:
            print "Mismatch"

if __name__ == "__main__":
    prompt = input("Do you want to input your own list of numbers (y/n)? ")
    if prompt.lower() == "y" or prompt.lower() == "yes":
        input_list = input("Input your comma-separated list:")
        print clever(input_list)

    else:
        list_size = input("How many numbers do you want to test (10 < N < 1000)? ")
        range_low = input("Lower limit (< -5)? ")
        range_high = input("Upper limit (> +5)? ")

        print clever(np.random.randint(range_low, range_high, size=list_size))

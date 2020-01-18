"""
Implement these two search algorithms.
"""


def linear_search(number, list):
    """
    Search for the number in the sorted list with the linear search algorithm
    and return the index of the element.

    Optional: print out how many comparision was needed to find the number

    :param integer number: The number to search for
    :param list of numbers list: Ascending list of numbers
    :return: Index of the element or None
    :rtype: integer
    """
    i = 0
    for element in list:
        if element == number:
            return i
        i= i + 1
    return None


def binary_search(number, list):
    """
    Search for the number in the sorted list with the binary search algorithm
    and return the index of the element.

    Optional: print out how many comparision was needed to find the number

    :param integer number: The number to search for
    :param list of numbers list: Ascending list of numbers
    :return: Index of the element or None
    :rtype: integer
    """
    right=len(list)-1
    left = 0
    while left < right:
        middle=left + (right-left)//2
        if list[middle] == number:
            return middle
        elif list[middle] < number:
            left = middle + 1
        else:
            left = middle -1
    return None


def print_results(search, index):
    result = search.title() + ' search '

    if index is None:
        result += 'did not find it.'
    else:
        result += f'found it on index {index}.'

    print(result)


def main():
    numbers = [3, 6, 8, 11, 18, 23, 24, 33, 36, 45, 46, 51, 56, 60, 69, 72, 83, 90, 93, 97]
    searched_number = int(input('What is the number you are looking for? (0-100) '))

    print_results('linear', linear_search(searched_number, numbers))
    print_results('binary', binary_search(searched_number, numbers))


if __name__ == '__main__':
    main()

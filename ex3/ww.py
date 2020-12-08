from ex3 import concat_list , cyclic , maximum ,seven_boom, histogram, pairs,prime_factors


def test_concat_list():
    assert concat_list([]) == ""
    assert concat_list(["1","2","3","4","5"]) == "1 2 3 4 5"
    assert concat_list([" "]) == " "
    assert concat_list(["h", "l", "e", "o"]) == "h l e o"
    assert concat_list(["h"]) == "h"
    assert concat_list([]) == ""

def test_maximum():
    assert maximum([1,2,3]) == 3
    assert maximum([1.0,2.0,3.0]) == 3.0
    assert maximum([0,0,0,0,0]) == 0
    assert maximum([10, 10, 10.5]) == 10.5
    assert maximum([1,1,1,10, 1,1,1,1, 11]) == 11

def test_cyclic():
    assert cyclic([1,2], [2,1])
    assert cyclic([1,2,3], [3, 1, 2])
    assert not cyclic([1,3, 2], [1, 2, 3, 4])
    assert not cyclic([1,2,3,4],[4,4,4])
    assert cyclic([1], [1])
    assert cyclic([1, 2], [1, 2])
    assert cyclic([],[])
    assert not cyclic([],[1])


def test_seven_boom():
    assert seven_boom(3) == ["1", "2", "3"]
    assert seven_boom(7) == ["1", "2", "3", "4", "5", "6", "boom"]
    assert seven_boom(77) == ['1', '2', '3', '4', '5', '6', 'boom', '8',
                              '9', '10', '11', '12', '13', 'boom', '15',
                              '16', 'boom', '18', '19', '20', 'boom', '22',
                              '23', '24', '25', '26', 'boom', 'boom', '29',
                              '30', '31', '32', '33', '34', 'boom', '36',
                              'boom', '38', '39', '40', '41', 'boom', '43',
                              '44', '45', '46', 'boom', '48', 'boom', '50',
                              '51', '52', '53', '54', '55', 'boom', 'boom',
                              '58', '59', '60', '61', '62', 'boom', '64',
                              '65', '66', 'boom', '68', '69', 'boom', 'boom',
                              'boom', 'boom', 'boom', 'boom', 'boom', 'boom']

def test_histogram():
    assert histogram(3, []) == [0, 0, 0]
    assert histogram(3, [0]) == [1, 0, 0]
    assert histogram(3, [1]) == [0, 1, 0]
    assert histogram(3, [2]) == [0, 0, 1]
    assert histogram(4, [3, 2, 3, 1, 3, 2]) == [0, 1, 2, 3]
    assert histogram(5, [3]) == [0, 0, 0, 1, 0]
    assert histogram(1, [0]) == [1]


def test_prime_factors():
    assert prime_factors(1) == []
    assert prime_factors(2) == [2]
    assert prime_factors(7) == [7]
    assert prime_factors(14) == [2, 7]
    assert prime_factors(100) == [2, 2, 5, 5]
    assert prime_factors(16) == [2, 2, 2, 2]

def test_pairs():
    assert pairs([], 5) == []
    assert pairs([4], 5) == []
    assert pairs([5], 5) == []
    assert pairs([4, 1], 5) == [[4, 1]]
    assert pairs([1,1,1,1,1,1], 3) == []
    assert pairs([1,1,1,1,1,1], 2) == [[1,1]]

def main():
    test_concat_list()
    test_maximum()
    test_cyclic()
    test_seven_boom()
    test_histogram()
    test_prime_factors()
    test_pairs()

if __name__ == "__main__":
    main()


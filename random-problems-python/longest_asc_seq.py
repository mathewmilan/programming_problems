'''
# 1. Given an integer list:
 2,4,5,-1, 4, 5, 7, 9, 2, 3, 2, 4, 2, 5, 7

Return the logest ascending sequence.
'''

def get_longest_ascending_sequence(intlist):
    longest_seq = []
    long_seq = []
    i = 0
    while (i < (len(intlist) - 1)):
        if (intlist[i] <= intlist[i+1]):
            long_seq.append(intlist[i])
        else:
            long_seq.append(intlist[i])
            # check len of current seq with longest seq.
            if(len(longest_seq) < len(long_seq)):
                longest_seq = long_seq
            long_seq = []
        i += 1
    return longest_seq


def test_longest_seq():
    '''
    Test the function.
    '''
    mylist = [1, 2, 3, 0, 33, 34, 34, 34, 65, 66, 9, 3, 4]
    longest_seq = get_longest_ascending_sequence(mylist)
    print("Longest seq: ", longest_seq)


test_longest_seq()
#A number will eventually be a palindrome by adding it to its reverse
#Eg: 87 :- 87 + 78 = 165; 165 + 561 = 726; 726 + 627 = 1353; 1353 + 3531 = 4884 
#It needs 4 additions to go from 87 to a palindrome, hence the answer is 4 
#Find the number of additions needed with its inverse for a number to be a palindrome
def reverse_add_palindrome(n):
    i = 0
    while (True):
        n_list = list(str(n))
        n_list.reverse()
        n_rev_str = ''.join(map(str, n_list))
        n_rev = int(n_rev_str)
        if(n == n_rev):
            return i
        i += 1
        n = n + n_rev

print(reverse_add_palindrome(48))
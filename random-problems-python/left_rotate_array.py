import logging

logging.basicConfig(filename = 'LeftRotation_log.txt', 
                    level = logging.DEBUG, 
                    format = '%(asctime)s-%(levelname)s-%(message)s')

#Rotate an array by n starting at k
def left_rotate(a, n, k):
    i = 0
    while(i < k):
        i += 1
        j = 0
        tmp = a[0]
        logging.debug('Rotation cycle '+ str(i) + ': ' + ' '.join(map(str, a)))
        while (j < n):
            if(j == n-1):
                a[j] = tmp
            else:
                a[j] = a[j+1]
            j +=1
    return a

logging.debug('Start of Program')
#n, k = map(int,  raw_input().strip().split(' '))
#a = map(int,  raw_input().strip().split(' '))
n, k = 5, 4
a = [1, 2, 3, 4, 5]

logging.debug('Before Rotation: '+ ' '.join(map(str, a)))
answer = left_rotate(a, n, k)
#print ' '.join(map(str, answer))
logging.debug('After Rotation: '+ ' '.join(map(str, answer)))

logging.debug('End of Program')
from time import sleep
import sys

# P =	
# 1.5
# 30
# = 0.05 × 100 = 5%

def ft_progress(listy: range):
    print( listy.stop)
    for i in listy:
        # ETA: 8.67s [ 23%][=====> ] 233/1000 | elapsed time 2.33s
        percent = (i / listy.stop) * 100 
        print('ETA: [{} %]'.format(percent), end='\r')
        yield i


listy = range(333)
ret = 0
for elem in ft_progress(listy):
    ret += elem
    sleep(0.005)
print()
print(ret)

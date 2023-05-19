array = [5,6,1,4,8,2,3,9,7]

for i in range(len(array)):
    for j in range(i):
        if array[i] < array[j]:
            array[i], array[j] = array[j] , array[i]
    print(f'{i} : ',array)

array = [5,6,1,4,8,2,3,9,7]

for i in range(len(array)):
    for j in range(i, 0, -1):
        if array[j-1] > array[j]:
            array[j-1], array[j] = array[j] , array[j-1]
    print(f'{i} : ', array)
    
'''
0 :  [5, 6, 1, 4, 8, 2, 3, 9, 7] 
1 :  [5, 6, 1, 4, 8, 2, 3, 9, 7]
2 :  [1, 5, 6, 4, 8, 2, 3, 9, 7]
3 :  [1, 4, 5, 6, 8, 2, 3, 9, 7]
4 :  [1, 4, 5, 6, 8, 2, 3, 9, 7]
5 :  [1, 2, 4, 5, 6, 8, 3, 9, 7]
6 :  [1, 2, 3, 4, 5, 6, 8, 9, 7]
7 :  [1, 2, 3, 4, 5, 6, 8, 9, 7]
8 :  [1, 2, 3, 4, 5, 6, 7, 8, 9]

0 :  [5, 6, 1, 4, 8, 2, 3, 9, 7]
1 :  [5, 6, 1, 4, 8, 2, 3, 9, 7]
2 :  [1, 5, 6, 4, 8, 2, 3, 9, 7]
3 :  [1, 4, 5, 6, 8, 2, 3, 9, 7]
4 :  [1, 4, 5, 6, 8, 2, 3, 9, 7]
5 :  [1, 2, 4, 5, 6, 8, 3, 9, 7]
6 :  [1, 2, 3, 4, 5, 6, 8, 9, 7]
7 :  [1, 2, 3, 4, 5, 6, 8, 9, 7]
8 :  [1, 2, 3, 4, 5, 6, 7, 8, 9]
'''
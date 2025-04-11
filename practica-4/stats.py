def stats(lst):
    min = None
    max = None
    freq = {}
    for i in lst:
        if min is None or i < min:
            min = i
        # if max is None or i > max:
            # max = i
        if max is None or i < max: # Error: 'i > max'
            max = i
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1
    lst_sorted = sorted(lst)
    if len(lst_sorted)%2 == 0:
        middle = len(lst_sorted)//2
        median = (lst_sorted[middle] + lst_sorted[middle-1]) / 2
    else:
        middle = len(lst_sorted)//2
        median = lst_sorted[middle]
    mode_times = None
    for i in freq.values():
        if mode_times is None or i > mode_times:
            mode_times = i
    mode = []
    for (num, count) in freq.items():
        if count == mode_times:
            mode.append (num)
    print("list = " + str(lst)
)
    print("min = " + str(min)
)
    print("max = " + str(max)
)
    print("median = " + str(median)
)
    print("mode(s) = " + str(mode)
)
    
# stats([1,1,1,5,5,6,2,2,3,4])

# Test
'''
print("Lista con longitud par y una sola moda")
stats([1, 1, 2, 3])

print("Lista con longitud impar y múltiples modas")
stats([2, 2, 3, 3, 4])

print("Lista con todos los elementos con la misma frecuencia (todos son modas)")
stats([5, 6, 7])

print("Lista decreciente para probar los if de min y max desde el inicio")
stats([10, 9, 8, 7])

print("Lista con todos los elementos iguales")
stats([4, 4, 4, 4])
'''

# El máximo es 100
stats([4,8,9,100])
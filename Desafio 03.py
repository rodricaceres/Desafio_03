from soporte import vector_unknown_range

def ejercicio_1():
    vector = vector_unknown_range(300000)
    num = []
    num_max = 0
    for i in vector:
        if not i in num:
            num.append(i)
        
        a = vector.count(i)
        if a > num_max:
            num_rep = i
            num_max = a

    return len(num), num_rep

print(ejercicio_1())

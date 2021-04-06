import numpy as np
import scipy as sp
import matplotlib.pyplot as plt

dig1 = np.random.randint(2,9,1)
dig2 = np.random.randint(1,9,1)
dig3 = np.random.randint(1,9,1)
dig4 = np.random.randint(20,69,1)

arr1 = [dig1, dig2, dig3]

def selection_sort(arr):        
    for i in range(len(arr)):
        minimum = i
        
        for j in range(i + 1, len(arr)):
            # Select the smallest value
            if arr[j] < arr[minimum]:
                minimum = j

        # Place it at the front of the 
        # sorted end of the array
        arr[minimum], arr[i] = arr[i], arr[minimum]
            
    return arr 
      
    
def slagalica(arr, dig):
    t1 = a+b+c
    t2 = a+b-c
    t3 = a-b+c
    t4 = b-a+c
    t5 = c-a-b
    t6 = a+(b*c)
    t7 = (b*c)-a
    t8 = b+(a*c)
    t9 = (a*c)-b
    t10 = c+(b*a)
    t11 = (b*a)-c
    t12 = a*(b+c)
    t13 = a*(c-b)
    t14 = (b+c)/a
    t15 = (c-b)/a
    t16 = b*(a+c)
    t17 = b*(c-a)
    t18 = (a+c)/b
    t19 = (c-a)/b
    t20 = c*(a+b)
    t21 = c*(b-a)
    t22 = (a+b)/c
    t23 = (b-a)/c
    t24 = (b*c)/a
    t25 = (c/b)/a
    t26 = (a*b)/c
    t27 = (b/a)/c
    t28 = (a*c)/b
    t29 = (c/a)/b
    t30 = a*b*c
    
    f1 = a+b
    f2 = a+c
    f3 = c-a
    f4 = c-b
    f5 = a*b
    f6 = a*c
    f7 = b*c
    f8 = c/b
    f9 = c/a
    f10 = c+b
    
    
    arr2 = [t1,t2,t3,t4,t5,t6,t7,t8,t9,t10,t11,t12,t13,t14,t15,t16,t17,t18,
            t19,t20,t21,t22,t23,t24,t25,t26,t27,t28,t29,t30,f1,f2,f3,f4,f5,f6,f7,f8,f9,f10]
    #print(arr2)
    for i in range(len(arr2)):
        tResult = np.abs(arr2[i]-dig)
        if (tResult == 0 or tResult == 1 or tResult == -1) :
            temp = i
            print("             Calculated: ",arr2[temp])
            print("            ",equations[temp])
            equat = equations[temp]
        else:
            equat = ""
    
    gsd = selection_sort(arr2)
    
    return gsd, equat

equations = ["a+b+c", "a+b-c", "a-b+c", "b-a+c", "c-a-b", "a+(b*c)", "(b*c)-a",
             "b+(a*c)", "(a*c)-b", "c+(b*a)", "(b*a)-c", "a*(b+c)", "a*(c-b)", "(b+c)/a",
             "(c-b)/a", "b*(a+c)", "b*(c-a)", "(a+c)/b", "(c-a)/b", "c*(a+b)", "c*(b-a)",
             "(a+b)/c", "(b-a)/c", "(b*c)/a", "(c/b)/a", "(a*b)/c", "(b/a)/c", "(a*c)/b",
             "(c/a)/b", "a*b*c", "a+b", "a+c", "c-a", "c-b", "a*b", "a*c", "b*c", "c/b",
             "c/a", "c+b" 
             ]  
    

new = selection_sort(arr1)
a, b, c = [new[0], new[1], new[2]]

temp = [a, b, c]

print("                ",a,"      ", b,"      ", c)
print()
print("                 Target: ",dig4)
print()

results, equ = slagalica(temp, dig4)

print("")
print("")
print("")
print("")
print(results)
loop = len(results)
for i in range(loop):
    diffarr = (dig4-results[i])
    print(diffarr)
    if diffarr == 0:
        print("       ",results[i])
        final = results[i]



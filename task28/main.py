a = int(input("Введите число А "))
b = int(input("Введите число B "))
count = a
result = a

def recu(a,b,count,result):
    if count == a * b:
        return result
    else:
        result = result + 1
        count = count + 1
        return recu(a,b,count,result)
    
print(recu(a,b,count,result))
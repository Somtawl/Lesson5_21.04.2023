a = int(input("Введите число А "))
b = int(input("Введите число B "))
count = 1
result = a

def recu(a,b,count,result):
    if count == b:
        return result
    else:
        result = result * a
        count = count + 1
        return recu(a,b,count,result)

print(recu(a,b,count,result))
 # 1
indice = 13
soma = 0
k = 0

while(k < indice):
    k = k + 1
    soma = soma + k

print(soma)

# 2

def fibonacci(n):
    data = [0, 1]
    for i in range(2, n+2):
        data.append(data[i-1] + data[i-2])
        print(data[i-1] + data[i-2])
    return data

def verificar_fibonacci(n):
    sequencia_fib = fibonacci(n)
    if n in sequencia_fib:
        print(f"{n} pertence a sequência Ficonacci.")
    else:
        print(f"{n} não pertence a sequência Ficonacci.")

n = int(input("Informe um número: "))
verificar_fibonacci(n)

# 3

# a) 1,3,5,7,9
# b) 2,4,8,16,32,64,128
# c) 0,1,4,9,16,25,36,49
# d) 4,16,36,64,100
# e) 1,1,2,3,5,8,13
# f) 2,10,12,16,17,18,19,20

# 5

def inverter_string(string_entrada):
    if not isinstance(string_entrada, str):
        return "Precisa ser informado uma string."
    string_invertida = string_entrada[::-1]
    return string_invertida

string_entrada = input("Informe uma string: ")
string_invertida = inverter_string(string_entrada)
print(f"String invertida: {string_invertida}")


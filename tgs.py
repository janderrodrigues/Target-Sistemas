#2)
n = int(input("Digite um número: "))
fibonacci = [0, 1]

while fibonacci[-1] < n:
    fibonacci.append(fibonacci[-1] + fibonacci[-2])

if n in fibonacci:
    print(f"O número {n} pertence à sequência de Fibonacci.")
else:
    print(f"O número {n} não pertence à sequência de Fibonacci.")


#3)
import json

with open('faturamento.json', 'r') as file:
    faturamento = json.load(file)

# menor faturamento diário
menor = min(faturamento)

# maior faturamento diário
maior = max(faturamento)

# média mensal
media = sum(faturamento) / len(faturamento)

# dias em que o faturamento diário foi superior à média mensal
superior_media = sum(1 for f in faturamento if f > media)

print(f"Menor faturamento diário: R${menor:.2f}")
print(f"Maior faturamento diário: R${maior:.2f}")
print(f"Dias com faturamento diário superior à média mensal: {superior_media}")


#4)
faturamento = {
    'SP': 67836.43,
    'RJ': 36678.66,
    'MG': 29229.88,
    'ES': 27165.48,
    'Outros': 19849.53
}

total = sum(faturamento.values())

for estado, valor in faturamento.items():
    percentual = valor / total * 100
    print(f"{estado}: {percentual:.2f}%")


#5)
s = input("Digite uma string: ")
s_invertida = ""

for i in range(len(s)-1, -1, -1):
    s_invertida += s[i]

print(f"A string invertida é: {s_invertida}")

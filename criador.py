# Entrada da string
texto = input("Digite uma string para ser invertida: ")

# Inverter a string manualmente
string_invertida = ""
for char in texto:
    string_invertida = char + string_invertida  # Adiciona o caractere no início da nova string

# Exibir o resultado
print(f"String original: {texto}")
print(f"String invertida: {string_invertida}")

def binario_para_float(string_binaria, endian='big'):
    if len(string_binaria) != 32:
        raise ValueError("A string binária deve ter 32 bits.")

    if endian == 'little':
        # Inverte a ordem dos bytes para little-endian
        string_binaria = ''.join([string_binaria[i:i+8][::-1] for i in range(0, 32, 8)][::-1])

    sinal = int(string_binaria[0])
    expoente = int(string_binaria[1:9], 2)
    mantissa = string_binaria[9:]

    # Calcula o valor do float
    if expoente == 0:
        if int(mantissa, 2) == 0:
            return 0.0  # Zero
        else:
            # Número desnormalizado
            fracao = 0
            for i, bit in enumerate(mantissa):
                fracao += int(bit) * (2 ** -(i + 1))
            valor_float = (-1)**sinal * 2**(-126) * fracao
    elif expoente == 255:
        if int(mantissa, 2) == 0:
            return float('inf') if sinal == 0 else float('-inf')  # Infinito
        else:
            return float('nan')  # NaN
    else:
        # Número normalizado
        fracao = 1.0
        for i, bit in enumerate(mantissa):
            fracao += int(bit) * (2 ** -(i + 1))
        valor_float = (-1)**sinal * 2**(expoente - 127) * fracao

    return valor_float


# Casos de teste
palavras_binarias = [
    "01000000101010010010000101101011",
    "00111111100000000000000000000000",
    "11000000110010010000111111000000",
    "01111110101000000000000000000000"
]

for palavra in palavras_binarias:
    big_endian_float = binario_para_float(palavra, endian='big')
    little_endian_float = binario_para_float(palavra, endian='little')

    print(f"Binário: {palavra}")
    print(f"Big-Endian: {big_endian_float}")
    print(f"Little-Endian: {little_endian_float}")
    print("-" * 30)

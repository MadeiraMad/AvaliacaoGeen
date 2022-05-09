def insertion_sort(vetor):
    for i in range(len(vetor)):
        atual = vetor[i]
        j = i - 1
        while ((j >= 0) and (vetor[j] > atual)):
            vetor[j + 1] = vetor[j]
            j = j - 1
            vetor[j + 1] = atual


def main():
    valores = [32, 7, 13, 24, 17, 21, 30, 14, 35, 2, 10]
    print(" Ordem original:\n ")
    for i in range(len(valores)):
        print(valores[i], end=" ")

    insertion_sort(valores)
    print("\n\nOrdenado:\n")
    for i in range(len(valores)):
        print(valores[i], end=" ")
    print("\n")
    print("Primos")
    for i in range(len(valores)):
        primos = (valores[i])
        isPrimo = True
        for x in range(2, primos):
            if primos % x == 0:
                isPrimo = False
        if isPrimo:
            print(primos, end=" ")

if __name__ == '__main__':
    main()

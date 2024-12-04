def main():
    tamanho = int(input("diga o tamanho do bloco: "))
    bloco(tamanho)

def bloco(tamanho):
    bloco = ("#" * tamanho)
    print (f"{bloco}\n" * tamanho)

main()
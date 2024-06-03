from time import sleep
texto1=input("\033[36m" +"\nDIGITE ALGO:\n"+ "\033[0m")
contagem=0
while contagem < len(texto1):
    letras=texto1[contagem]
    print("\n",letras)
    contagem= contagem+1
    sleep(0.5)
    
char1=input("\033[36m" +"\nVOCÊ GOSTARIA DE MUDAR UM CARACTER DO SEU PRIMEIRO TEXTO?\n (responda com sim ou não)\n"+ "\033[0m")
char1_mai=char1.upper()
if char1_mai=="SIM" or char1_mai=="S":
    mudar_char1=input("\033[36m" +"\nCERTO, QUAL CARACTER DESEJA MUDAR?\n"+ "\033[0m")
    mudar2_char1=input("\033[36m" +"\nVOCÊ QUER TROCAR POR QUAL CARACTER?\n"+ "\033[0m")
    texto1=texto1.replace(mudar_char1,mudar2_char1)
    print("\033[36m" +"\nMUDANÇA EFETUADA!\n"+ "\033[0m")
    contagem=0
    while contagem < len(texto1):
        letras=texto1[contagem]
        print("\n",letras)
        contagem= contagem+1
        sleep(0.5)
else:
    print("\033[36m" +"\nOK!\n"+ "\033[0m")
    
print("\033[36m" +"\nVOCÊ DIGITOU {} CARACTERES.\n".format(len(texto1))+ "\033[0m")

texto1_caracter=input("\033[36m" +"\nQual caracter você deseja saber quantas vezes é citado no texto digitado?\n".upper()+ "\033[0m")
texto1_minusculo=texto1.lower()
texto1_caracter_minusculo=texto1_caracter.lower()
quantidade=texto1_minusculo.count(texto1_caracter_minusculo)
print("\033[36m" +"\n",quantidade, "CARACTERES ACHADOS.\n"+ "\033[0m")

texto2=input("\033[36m" +"DIGITE ALGO NOVO:\n"+ "\033[0m")
contagem=0
while contagem < len(texto2):
    letras=texto2[contagem]
    print("\n",letras,"\n")
    contagem= contagem+1
    sleep(0.5)
    
char2=input("\033[36m" +"\nVOCÊ GOSTARIA DE MUDAR UM CARACTER DO SEU PRIMEIRO TEXTO?\n (responda com sim ou não)\n"+ "\033[0m")
char2_mai=char2.upper()
if char2_mai=="SIM" or char2_mai=="S":
    mudar_char2=input("\033[36m" +"\nCERTO, QUAL CARACTER DESEJA MUDAR?\n"+ "\033[0m")
    mudar3_char1=input("\033[36m" +"\nVOCÊ QUER TROCAR POR QUAL CARACTER?\n"+ "\033[0m")
    texto2=texto2.replace(mudar_char2,mudar3_char1)
    print("\033[36m" +"\nMUDANÇA EFETUADA!\n"+ "\033[0m")
    contagem=0
    while contagem < len(texto2):
        letras=texto2[contagem]
        print("\n",letras)
        contagem= contagem+1
        sleep(0.5)
else:
    print("\033[36m" +"\nOK!\n"+ "\033[0m")
    
print("\033[36m" +"\nVOCÊ DIGITOU {} CARACTERES.\n".format(len(texto2))+ "\033[0m")

texto2_caracter=input("\033[36m" +"\nQual caracter você deseja saber quantas vezes é citado no texto digitado?\n".upper()+ "\033[0m")
texto2_minusculo=texto2.lower()
texto2_caracter_minusculo=texto2_caracter.lower()
quantidade=texto2_minusculo.count(texto2_caracter_minusculo)
print("\033[36m" +"\n",quantidade," CARACTERES ACHADOS.\n"+ "\033[0m")

if len(texto1) > len(texto2):
    sub=len(texto1)- len(texto2)
    sleep(0.5)
    print("\033[36m" +"O PRIMEIRO TEXTO TEM {} CARACTERES A MAIS DO QUE O SEGUNDO TEXTO DIGITADO!\n".format(sub)+ "\033[0m")
else:
    sub=len(texto2)- len(texto1)
    sleep(0.5)
    print("\033[36m" +"O SEGUNDO TEXTO TEM {} CARACTERES A MAIS QUE O PRIMEIRO TEXTO DIGITADO!\n".format(sub)+ "\033[0m")
    

concatenar=texto1+texto2
contagem=0
print("\033[36m" +"\nCONCATENAÇÃO:\n"+ "\033[0m")
while contagem<len(concatenar):
    letras=concatenar[contagem]
    print("\n",letras,"\n")
    contagem=contagem+1
    sleep(0.5)

concatenar=texto1+texto2
contagem=len(concatenar)-1
print("\033[36m" +"\nO inverso da soma dos textos:\n".upper()+ "\033[0m")
while 0<=contagem:
    letras=concatenar[contagem]
    print("\n",letras,"\n")
    contagem=contagem-1
    sleep(0.5)

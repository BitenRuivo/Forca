import os

def desenho(erro):
    if erro == 0:
        print("________  ")
        print("!      |  ")
        print("!         ")
        print("!         ")
        print("!         ")
        print("!         ")
        print("!         ")
    elif erro == 1:
        print("________  ")
        print("!      |  ")
        print("!      0  ")
        print("!         ")
        print("!         ")
        print("!         ")
        print("!         ")
    elif erro == 2:
        print("________  ")
        print("!      |  ")
        print("!      0  ")
        print("!      |  ")
        print("!      |  ")
        print("!         ")
        print("!         ")
    elif erro == 3:
        print("________  ")
        print("!      |  ")
        print("!      0  ")
        print("!     /|  ")
        print("!      |  ")
        print("!         ")
        print("!         ")
    elif erro == 4:
        print("________  ")
        print("!      |  ")
        print("!      0  ")
        print("!     /|\ ")
        print("!      |  ")
        print("!         ")
        print("!         ")
    elif erro == 5:
        print("________  ")
        print("!      |  ")
        print("!      0  ")
        print("!     /|\ ")
        print("!      |  ")
        print("!     /   ")
        print("!         ")
    elif erro == 6:
        print("________  ")
        print("!      |  ")
        print("!      0  ")
        print("!     /|\ ")
        print("!      |  ")
        print("!     / \ ")
        print("!         ")

erro = 6
desenho(erro)
print("insira um palavra:")
palavra = list(input())
os.system("clear")
descarte = []
tamanho = len(palavra)
espaço = ["_ "] * tamanho
erro = 0

while erro < 6:
    
    desenho(erro)
    
    for i in range (0, tamanho):
        print(espaço[i], end=" ")
        
    print("")
    print("")
    print("não tem: " + " / ".join(str(num) for num in descarte))
    print("")
    print("insira uma letra:")
    
    chute = input()
    
    if chute in palavra:
        for i in range (0, tamanho):
            if chute == palavra[i]:
                espaço[i] = chute
    elif chute in descarte:
        pass
    else:
        erro += 1
        descarte.append(chute)
        
    os.system("clear")
    
    if espaço == palavra:
        break

desenho(erro)
for i in range (0, tamanho):
        print(palavra[i], end=" ")
print("")
print("")
print("não tem: " + " / ".join(str(num) for num in descarte))
print("")

if erro < 6:
    print("VOCÊ GANHOU :D")
else:
    print("VOCÊ PERDEU :P")
from math import*
#Método da Bissecção
#Joao Vitor Pinheiro
#Encontre uma raiz real da função p(x)
#com precisão de 0.01 , a partir de um intervalo inicial de números inteiros.

# É PRECISO ALTERAR A FUNÇÃO AQUI NESSA PARTE DO CODIGO
# DEPOIS DE DESCOBRIR A FUNÇÃO DESEJADA, MUDE resultado (abaixo) PARA A FUNÇÃO QUE DESEJA CALCULAR
# DE RESTO É SÓ DIGITAR OQ PEDE O PROGRAMA


def px(x):
  #Exemplos de funções que podem ser usadas
  #resultado = 3*(x**3)-8*(x**2)+10
  #resultado = 3*(x**3)+sin(3*x)+2

  #Essa é a função do meu número de matricula
  resultado=5*(x**3)-12*x+8.75
  return(resultado)

#função --> p(x) = 3x^3-8x^2+10 --> 3 raízes
#intervalo = [-1,0]
#'ab'=f(a)*f(b), se f(a)*f(b)<0 , possui número ímpar de raízes.


#Xm é a média entre eles
#Fe,Fm,Fd são as funções aplicadas nos respectivos Xe,Xm,Xd

def bisec(xe,xd):
    xm = (xe + xd) / 2
    fe = px(xe)
    fd = px(xd)
    fm = px(xm)
    #A contagem dos passos já parte do 1-> passo inicial, logo i=2
    i = 1
    tolerancia = float(input("Digite a tolerancia (Exemplo -> 0.01) : "))
    print(i, ".| Xe:", round(xe, 4), "| Xm:", round(xm, 4), "| Xd:", round(xd, 4), " ||| Fe:", round(fe, 4), " | Fm:",
          round(fm, 4), " | Fd:", round(fd, 4), " |---> INICIO >--- INTERVALO :",
          round(abs(xe - xd), 4))
    i=i+1

    while ((abs(fm) > tolerancia) & (fm != 0)):
        if (fe * fm < 0):
            # SIGNIFICA QUE A RAIZ ESTÁ ENTRE Xe e Xm
            xd = xm
            xm = (xe + xd) / 2
            fe = px(xe)
            fd = px(xd)
            fm = px(xm)
            print(i,".| Xe:",round(xe,4),"| Xm:",round(xm,4),"| Xd:",round(xd,4)," ||| Fe:",round(fe,4)," | Fm:",round(fm,4)," | Fd:",round(fd,4)," |---> Aproximação pela Direita >--- INTERVALO :",round(abs(xe-xd),4))

        elif (fm * fd < 0):
            # SIGNIFICA QUE A RAIZ ESTÁ ENTRE Xm e Xd
            xe = xm
            xm = (xe + xd) / 2
            fe = px(xe)
            fd = px(xd)
            fm = px(xm)
            print(i, ".| Xe:", round(xe, 4), "| Xm:", round(xm, 4), "| Xd:", round(xd, 4), " ||| Fe:", round(fe, 4)," | Fm:", round(fm, 4), " | Fd:", round(fd, 4), " |---> Aproximação pela Esquerda >--- INTERVALO :",round(abs(xe - xd), 4))

        else:
            print("\nNão há raíz no intervalo\n\n")
            return 0
        i = i + 1

    print("\nx =",round(xm,4)," é a raiz de f(x) com tolerância de ",tolerancia)
    i=input("-"*50+" PRESSIONE ENTER PARA CONTINUAR"+"-"*50+"\n")


def newton():
    print("\nPara usar esse método é preciso alterar a função nas variáveis diretamente na linha de código\n")
    # CALCULE A RAIZ CUBICA DE 5 COM PRECISÃO DE 0.01 PELO MÉTODO DE NEWTON - RAPHSON A PARTIR DE UMA APROXIMAÇÃO INICIAL INTEIRA
    # função --> x ^ 3 = 5 --> y = 6 * (x**3) - 7 * x + 9.75 (para que a função corte o eixo X na função
    # tangente = (f(a) - 0) / (a - ze)
    # 'a' e 'fa' são dadas pelo problema

    a = -1
    fa = 10.75
    #tan deve ser diferente de 0
    tan = 11
    ze = a - (fa / tan)
    z = -1.5
    i = 1
    tolerancia = float(input("Digite a tolerancia (Exemplo -> 0.01) : "))

    while (abs((6 * (a ** 3) - 7 * a + 9.75) - (6 * (-1.5 ** 3) - 7 * (-1.5) + 9.75)) > tolerancia):
        print(i, " | x",i, "=", round(a,4), " | f( x",i, ")=", round(fa, 6), " | tangente=", round(tan, 4), " | ze=",round(ze, 4), " |")
        a = ze # o 'ponto a' recebe 'ze', que vira o novo ponto de aproximação da raiz verdadeira 'z'
        fa = 6 * (a**3) - 7 * a + 9.75
        tan = 18 *(a**2) - 7 # derivada da anterior
        ze = a - (fa / tan)  # 'ze' é incognita e 'ze=a-(f(a)/f'(a))'
        i =i+1

    print(i, " | x", i, "=", round(a, 4), " | f( x", i, ")=", round(fa, 6), " | tangente=", round(tan, 4), " | ze=",round(ze, 4), " |")
    print("\nO ponto x",i," =",round(a,4)," é a raiz de f(x) com tolerância",tolerancia)
    i = input("-" * 50 + " PRESSIONE ENTER PARA CONTINUAR" + "-" * 50 + "\n")

if __name__ == '__main__':
    # Aqui faz-se a leitura dos dados
    # Xe = Ponto do intervalo mais a esquerda
    # Xd = Ponto do intervalo mais a direita
    while(1):
        print("Escolha o método: 1 - Bisecção , 2 - Newton , 0 - Sair do programa")
        decisao=input("Digite 1 ou 2:")
        if(int(decisao)==1):
            print("-"*20,"MÉTODO DA BISECÇÃO","-"*20)
            xe=float(input("Digite o limite do intervalo da esquerda: "))
            xd=float(input("Digite o limite do intervalo da direita: "))
            bisec(xe,xd)
        elif(int(decisao)==2):
            newton()
        elif(int(decisao) == 0):
            break;
        else:
            print("Entrada inválida")

// CALCULE A RAIZ CUBICA DE 5 COM PRECISÃO DE 0.01 PELO MÉTODO DE NEWTON-RAPHSON A PARTIR DE UMA APROXIMAÇÃO INICIAL INTEIRA
#include <stdio.h>
#include <math.h>

int main (){
	
	// função --> x^3 = 5 --> y = 6*pow(x,3)-7*x + 9.75 (para que a função corte o eixo X na função) 
	// tangente = (f(a)-0)/ (a-ze)
	// 'a' e 'fa' são dadas pelo problema
	// 'ze' é incognita  e 'ze=a-(f(a)/f'(a))'	
	float a = -1;
	float fa = 10.75;
	float tan = 11;
	float ze = a-(fa/tan);
	float z = -1.5;
	int i=1;
	float tolerancia = 0.001;
	//exp() = e^x --> pertence a math.h
	//tan deve ser diferente de 0
	// o 'ponto a' recebe 'ze', que vira o novo ponto de aproximação da raiz verdadeira 'z'
	while(fabs((6*pow(a,3)-7*a + 9.75)-(6*pow(-1.5,3)-7*(-1.5)+ 9.75))>tolerancia){
	//precisão de 0.01 	
		printf("%d | x%d=%.4f | f(x%d)=%.6f | tangente=%.4f | ze=%.4f |\n",i,i,a,i,fa,tan,ze);
		a=ze;
		fa =  6*pow(a,3)-7*a + 9.75;
		tan = 18*pow(a,2)-7;
		ze = a - (fa/tan);
		i++;
	}
	printf("%d | X%d=%.4f | f(x%d)=%.6f | tangente=%.4f | ze=%.4f |\n",i,i,a,i,fa,tan,ze);
	printf("\nO ponto x%d = %.4f é a raiz de f(x) com tolerância de %.3f:",i,a,tolerancia);
	return 0;
}

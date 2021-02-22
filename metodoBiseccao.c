//Método da Bissecção
//Joao Vitor Pinheiro
//Encontre uma raiz real da função p(x) 
//com precisão de 0.01 , a partir de um intervalo inicial de números inteiros.
#include <stdio.h>
#include <math.h>
//função para aplicar p(x)
float px(float x){
  float resultado; 
  //resultado = 3*pow(x,3)-8*pow(x,2)+10;
  //resultado = 3*pow(x,3)+sin(3*x)+2;
  //resultado = 6*pow(x,3)-7*x+9.75;
  //resultado = pow(x,3)-x-2;
  resultado=5*pow(x,3)-12*x+8.75;
  return(resultado); //retornando o valor para main
}

int main (){
	// função --> p(x) = 3x^3-8x^2+10 --> 3 raízes ; 
	// intervalo = [-1,0]
	// 'ab'=f(a)*f(b), se f(a)*f(b)<0 , possui número ímpar de raízes.
	float xe=-2;
	float xd=-1;
	float xm=(xe+xd)/2;
	float fe=px(xe);
	float fd=px(xd);
	float fm=px(xm);
	int i=2;
	float tolerancia=0.01;
	printf("1.| Xe:%.4f | Xm:%.4f | Xd:%.4f ||| Fe:%.4f | Fm:%.4f | Fd:%.4f |-----> Início >----- INTERVALO : %.8f\n",xe,xm,xd,fe,fm,fd,fabs(xe-xd));
	while((fabs(fm)>tolerancia) && (fm!=0)){
		
		if(fe*fm<0){
		//SIGNIFICA QUE A RAIZ ESTÁ ENTRE Xe e Xm	
			xd=xm;
			xm=(xe+xd)/2;
			fe=px(xe);
			fd=px(xd);
			fm=px(xm);
			printf("%d.| Xe:%.4f | Xm:%.4f | Xd:%.4f ||| Fe:%.4f | Fm:%.4f | Fd:%.4f |-----> Aproximação pela Direita >----- INTERVALO : %.8f\n",i,xe,xm,xd,fe,fm,fd,fabs(xe-xd));
			//printf("XD ANTIGO:%f\n",pivo);
		}
		else if(fm*fd<0){
		//SIGNIFICA QUE A RAIZ ESTÁ ENTRE Xm e Xd	
			xe=xm;
			xm=(xe+xd)/2;
			fe=px(xe);
			fd=px(xd);
			fm=px(xm);
			printf("%d.| Xe:%.4f | Xm:%.4f | Xd:%.4f ||| Fe:%.4f | Fm:%.4f | Fd:%.4f |-----> Aproximação pela Esquerda >----- INTERVALO : %.8f\n",i,xe,xm,xd,fe,fm,fd,fabs(xe-xd));
		}	
		else{
			printf("\nNão há raíz no intervalo\n\n");
			return 0;
		}
		//printf("\noi\n");
		i++;	
}
	printf("\nx = %.4f é a raiz de f(x) com tolerância de %.4f",xm,tolerancia);
	return 0;
}



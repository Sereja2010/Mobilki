#include <stdio.h>
#include <stdlib.h> 


int main (){
int summ=0;
long int md=0, mo=0;
int sh;
int tsh=0, tsmin=0, cd=0, sn=0, min;

  size_t len, read;
  char *c=NULL;
 
FILE *in;
in=fopen ("data.csv", "r");
char *pa = NULL;
read=getdelim(&pa, &len, EOF, in);
while (*pa!='\n') pa++; pa++;


while (*pa!='\0') {
pa=pa+10; tsh=strtol(pa, &pa, 10); pa++; tsmin=strtol(pa, &pa, 10); pa=pa+4; mo=strtoul(pa, &pa, 10); pa++;  md=strtoul(pa, &pa, 10); pa++; cd=strtol(pa, &pa, 10); if (*pa='.') {cd++; pa++; sh=strtol(pa, &pa, 10);} pa++; sn=strtol(pa, &pa, 10); pa++;	// Считывание строки и запись её полей в переменные
if (mo==933156729) 
	{ min=(tsh-0)*60+(tsmin-30); 
		if (min<0) { if ((min*(-1))>cd) {summ=summ+cd*3;} else {summ=summ+min*3+(cd+min)*2;}
						} else {summ=summ+cd*2;}
//Рассчёт, если звонил абонент
if (sn>50) {summ=summ+(sn-50)*2;} //Рассчёт СМС

}
if (md==933156729) 
	{ min=(tsh-0)*60+(tsmin-30); 
		if (min<0) { if ((min*(-1))>cd) {summ=summ+cd*0;} else {summ=summ+min*0+(cd+min)*2;}
						} else {summ=summ+cd*2;}
//Рассчёт,если звонили абоненту
}





	
	}
printf ("Итоговая сумма: %d руб.\n", summ);
fclose(in);
}




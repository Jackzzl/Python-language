#include <stdio.h>
int main(){
    double sum=0;
    for(int i=0;;i++){
        double term=1.0/(2*1-1);
        if(i%2==0)
            sum-=term;
        else
            sum+=term;
        if(term<1e-6)
            break;
    }
    printf("%.6f",sum);
    return 0;
}




/*int main() {
    double sum=0;
    int n=1;
    double term;
    do{
        term=1.0/(2*n-1);
        if(n%2==1)
            sum+=term;
        else
            sum-=term;
        n++;
    }while(term<1e-6);
    printf("%.6f\n",sum);
    return 0;
}*/
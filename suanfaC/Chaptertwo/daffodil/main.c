#include <stdio.h>
#include <math.h>

/*int main() {
    //int n=100;
    int ge,shi,bai,a;
    for(int n=100;n<=999;n++){
        ge=n%10;
        bai=n/100;
        shi=(n/10)%10;
        if(n==ge*ge*ge+shi*shi*shi+bai*bai*bai)
            printf("%d\n",n);
        //printf("%d\n",n);
    }
    return 0;
}*/
int main(){
    int n=100;
    int ge,shi,bai;
    while(n>=100 && n<=999){
        ge=n%10;
        shi=(n/10)%10;
        bai=n/100;
        if(n==ge*ge*ge+shi*shi*shi+bai*bai*bai)
            printf("%d\n",n);
        n++;
    }
    return 0;
}
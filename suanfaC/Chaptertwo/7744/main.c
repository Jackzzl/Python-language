#include <stdio.h>
#include<math.h>
int main() {
    for(int a=1;a<10;a++){
        for(int b=0;b<10;b++){
            int n=a*1100+b*11;
            int m=floor(sqrt(n)+0.5);
            if(m*m==n)
                printf("%d\n",n);
        }
    }
    return 0;
}
/*answer two
 * #include<stdio.h>
 * int main(){
 *      for(int x=0;;x++){
 *          int n=x*x;
 *          if(n<10000)continue;
 *          if(n>9999)break;
 *          int hi=n/100;
 *          int na=n%100;
 *          if(hi/10==hi%10 && na/10==na%10)
 *              printf("%d\n",n);
 *      }
 *      return 0;
 * }
 * */
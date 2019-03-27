#include <stdio.h>
#include <math.h>
int main() {
    double pi=acos(-1.0);
    int x;
    double r;
    double s,c;
    printf("please input a number\n");
    scanf("%d",&x);
    r=x*pi/180;
    s=sin(r);
    c=cos(r);
    printf("sin=%lf,cos=%lf",s,c);
    return 0;
}
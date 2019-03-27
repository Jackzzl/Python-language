#include <stdio.h>
int i;

/*void len(char *s){
    while(*s){
        s++;i++;
        printf("%d ",i);
        printf("%s\n",s);
    }
   printf("%d\n",i);
}*/
int len(char *s) {
    while (*s) {
        s++;
        i++;
        printf("%d ",i);
        printf("%s\n",s);
    }
    return i;
}
void main(){
    char s[]="x0123yz";
    //len(s);
    //len(s+1);
    printf("%d %d\n",len(s),len(s+1));
    printf("%s\n",s);
    printf("%s",s+1);
}



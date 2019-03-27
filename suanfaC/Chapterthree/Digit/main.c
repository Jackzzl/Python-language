/*为解决0的问题
#include <stdio.h>
#include <string.h>

int main() {
    int num;
    long long int last;
    int a[15];
    memset(a,0,sizeof(a));
    printf("输入数字\n");
    scanf("%d",&num);
    for(int i;;i++){
        last=num%10;
        if(last==0)
            break;
        num=num/10;
        for(int j=0;j<=9;j++){
            if(j==last)
                a[j]+=1;
        }
    }
    for(int i=0;i<=9;i++){
        printf("%d 的次数: %d \n",i,a[i]);
    }
}*/
#include <stdio.h>
#include<string.h>
#define manx 100005
int ans[manx];

int main(){
    int T,n;
    memset(ans,0,sizeof(ans));
    for(int m=1;m<manx;m++){
       int x=n,y=m;
       while(x>0){
           y+=x%10;
           x/=10;
       }
       if(ans[y]==0||m<ans[y])
           ans[y]=m;
    }
    scanf("%d",&T);
    while(T--){
        scanf("%d",&n);
        printf("%d\n",ans[n]);
    }
    return 0;
}
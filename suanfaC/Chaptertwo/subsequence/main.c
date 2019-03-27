#include <stdio.h>
#include <math.h>
int main() {
    int n,m;
    int count;
    //double s;
    printf("请输入俩个数字");
    /*do{
        scanf("%d %d",&n,&m);
        for(int i=n;i<m;i++){
            s=s+1/(i*i);
        }
        count+=1;
        printf("Case %d:%.5f",count,s);

    }while(n=m=0);*/
    while((scanf("%d %d",&n,&m)!=EOF)){
        if(n==0&&n==0)
            break;
        if(n>=m||m>pow(10,6)||n<0){
            printf("INput ERROR");
        }
        double s;
        for(int i=n;i<=m;i++){
            s+=1.0/i/i;
        }
        count+=1;
        printf("Case %d:%.5lf\n",count,s);
    }
    return 0;
}

/*int main()
{
    LL n,m,cnt=1;
    double sum;
    while(1)
    {
        cin>>n>>m;
        if(n==0&&m==0)
            break;
        sum=0.0;
        for(LL i=n;i<=m;i++)
        {
            sum+=1.0/(i*i);
        }
        printf("Case %lld: %.5lf\n",cnt++,sum);
    }
    return 0;*/


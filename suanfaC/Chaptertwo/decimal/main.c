#include <stdio.h>
#include <math.h>

/*int main() {
    int a,b,c;
    int count;
    double s;
    printf("请输入数据");
    while(scanf("%d%d%d",&a,&b,&c)!=EOF){
        if(a<=0||b<=0||c<=0)
            break;
        if(a>pow(10,6)||b>pow(10,6)||c>100)
            break;
        s=1.0*a/b;
        count++;
        printf("Case %d:%.*lf",count,c,s);
    }
    //printf("Hello, World!\n");
    return 0;
}*/
int n,m[110];//n整数部分，m小数部分
int main()
{
    int a,b,c,i,k=0;
    while(scanf("%d%d%d",&a,&b,&c)&&a&&b&&c)
    {
        k++;
        n=a/b;
        a=a%b;
        m[0]=0;//十分位小数，可以进位为整数
        for(i=1;i<=c;i++)
        {
            m[i]=a*10/b;
            a=a*10%b;
        }
        if(a*10/b>=5)//第C+1位，四舍五入
        {
            for(i=c;i>=0;i--)//进位处理
            {
                m[i]=m[i]+1;
                if(m[i]<10)
                    break;//若不存在进位，跳出循环。
                else
                    m[i]-=10;
            }
        }
        n=n+m[0];//整数部分进位处理。
        printf("Case %d: %d.",k,n);//打印整数部分及小数点
        for(i=1;i<=c;i++)
            printf("%d",m[i]);//打印小数部分。
        printf("\n");
    }
    return 0;
}

#include<stdio.h>
#include<string.h>
int main()
{
    int abc,def,ghi,sum=0,i;
    int s[10];
    for(abc=123;abc<=329;abc++)//最小a的三位数范围，987/3=329
    {
        memset(s, 0, sizeof(s));//memest函数可以对数组，指针进行初始化非常方便
        def=abc*2;
        ghi=abc*3;
        s[abc/100]=s[abc/10%10]=s[abc%10]=1;
        s[def/100]=s[def/10%10]=s[def%10]=1;
        s[ghi/100]=s[ghi/10%10]=s[ghi%10]=1;
        for(i=1;i<=9;i++)
        {
            sum=sum+s[i];
        }
        if(sum==9)
        {
            printf("%d %d %d\n",abc,def,ghi);
        }
        sum=0;//再次进行循环时，要记得对sum和s数组进行初始化
        memset(s, 0, sizeof(s));
    }
    return 0;
}

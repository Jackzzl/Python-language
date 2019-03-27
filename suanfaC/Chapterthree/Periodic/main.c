
#include <stdio.h>
#include <string.h>

int main() {
    char s[100];
    int a[50];
    int y;
    printf("请输入一个字符串\n");
    scanf("%s",s);
    int len=strlen(s);
    for(int i=1;i<len;i++){
        if(len%i==0){
            int l=len%i;
            for(int j=0;j<l;j++){
                if(s[j]==s[j+l])
                    continue;
                else
                    break;
                if(j=l-1){
                    y=l;
                }
            }
        }
    }
    printf("%d",y);
    return 0;
}
/*
#include<stdio.h>
#include<string.h>
int main()
{
    int k = 1;
    char s[100];
    scanf("%s",s);
    int len = strlen(s);
    int flag = 0; //没找到k时
    for(k = 1; k <= len && flag == 0; k++)
    {
        if(len % k != 0) //满足k整除len
            continue;
        flag = 1; //假设此时k是周期
        for(int i = 1; i < (len / k); i++) //分成len/k个小段，验证每个小段是否相同
        {
            for(int j = 0; j < k; j++) //在每小段中逐位验证
            {
                if(s[i*k+j] != s[j])
                {
                    flag = 0; //此时k不是周期，不必再检查其他位
                    break;
                }
            }
            if(!flag) //此时k不是周期，不必再检查其他段
                break;
        }

    }
    printf("%d\n",k-1);


    return 0;
}*/
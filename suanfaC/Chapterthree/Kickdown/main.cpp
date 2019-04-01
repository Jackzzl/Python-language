#include <iostream>
#include<cassert>
#include<cstdlib>
#include<functional>
#include<algorithm>
#include<cstring>
#include<string>
#include<vector>
#include<set>
using namespace std;
const  int MAX=101;
int a[10]={1,1,1,2,2,1,2,2,1,2};
int b[10]={1,1,1,2,2,1,2,2,1,2};
int x;
int n;//偏移量，10+n=最终长度
int main(){
    for(int n=0;n<=10;n++) {
        for (int i = 0; i < 10; i++) {
            if ((a[i + n] + b[i]) <= 3){
                if((i+n)>9){
                printf("长度为：%d\n",10+n);
                x=1;
                break;}
                continue;
            }
            else {
                break;
            }
        }
        if(x==1)
            break;

    }
    return 0;
}
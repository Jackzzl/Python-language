#include <iostream>

using namespace std;


float twitch(float x){
     double  C;
     C=(x-32)*5/9;
     return C;
    }
int main()
{
    cout<<"华氏温度转换"<<endl;
    cout<<"请输入一个华氏温度:"<<endl;
    float F;
    cin>>F;
    cout<<"结果为:"<<twitch(F)<<endl;
    return 0;
}

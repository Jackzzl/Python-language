#include <iostream>

using namespace std;
    float galaxy(int n, int x){
        int A,B;
        if(n==0)
            A=1;
    //return 1;
        else if(n==1)
            A = x;
    //return x;
        else
        {
            B=(2*n-1)*x*galaxy(n-1,x)-(n-1)*galaxy(n-2,x);
            A= B/n;}
        return A;
    }
int main()
{
        int n,x;
        cout<<"请输入n的值："<<endl;
        cin>>n;
        cout<<"请输入x的值:"<<endl;
        cin>>x;
        cout<<"得到的结果为："<<galaxy(n,x)<<endl;
        return 0;
}

#include <iostream>
#include <string>
#include <cstring>
//未完成判定出界情况

using namespace std;
/*
struct Point{
    int x,y;
    Point(int x=0,int y=0):x(x),y(y){
    }
};
typedef  Ponit Vectoer;
*/
 int main() {
     char b[5][5]={'T','R','G','S','J',
                   'X','D','O','K','I',
                   'M','Z','V','L','N',
                   'W','P','A','B','E',
                    'U','Q','H','C','F'};
    cout << "请输入一组字符串" <<endl;
    char a[10];
    scanf("%s",a);
    int bx,by;
    cout<<"空白格位置"<<endl;
    cin >>bx;
    cin>>by;
    bx-=1;
    by-=1;
    for(int i=0;i<strlen(a);i++){
        switch(a[i]){
            case 'A':
                by-=1;
                if(by>=5)
                    cout<<"错误操作"<<endl;
                break;
            case 'B':
                by+=1;
                if(by>=5)
                    cout<<"错误操作"<<endl;
                break;
            case 'L':
                bx+=1;
                if(bx>=5)
                    cout<<"错误操作"<<endl;
                break;
            case 'R':
                bx-=1;
                if(bx>=5)
                    cout<<"错误操作"<<endl;
                break;
            default:
                break;
        }
        cout<<bx;
        cout<<by<<"\n";
    }
    for(int i=0;i<5;i++){
        for(int j=0;j<5;j++) {
            if (bx == i && by == j) {
                cout << "8 ";
                continue;
            }
            cout << b[i][j];
        }
        cout<<"\n";
    }
}
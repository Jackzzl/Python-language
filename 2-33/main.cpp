#include <iostream>

using namespace std;

enum Weekday{SUNDAY=7,MONDAY=1,TUSEDAY,WEDNESDAY,THURSDAY,FRIDAY,SATURDAY};
int main()
{
    int n;
    Weekday d = SUNDAY;
    cout<<"d="<<d<<endl;
    n =d;
    cout<<"n="<<n<<endl;

    d=(Weekday)6;
    cout<<"d="<<d<<endl;
    d=Weekday(3);
    cout<<"d="<<d<<endl;
    return 0;
}

#include <iostream>

using namespace std;

int main(){
int n;
cout<<"ÇëÊäÈë³É¼¨£º"<<endl;
cin>>n;
if(n>100||n<0)
cout<<"´íÎóÊý×Ö"<<endl;
else{
switch(n=n/10){
case 10:
case 9:
cout<<"ÓÅ"<<endl;
break;
case8:
cout<<"Á¼"<<endl;
break;
case 7:
case 6:
cout<<"ÖÐ"<<endl;
break;
default:
cout<<"²î"<<endl;
break;
}
}
return 0;
}

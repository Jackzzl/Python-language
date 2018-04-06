#include <iostream>
using namespace std;
//二进制转化为十进制 
int main() {
	int value=0;
	cout<<"Enter an 8 bit binary number:";
	for (int i = 7;i>=0;i--){
	char ch;
	cin>>ch;
	if (ch=='1')
	value+=static_cast<int> (power(2, i));
	}
	cout<<"Decimal value is "<<value<<endl;
	return 0;
}
	double power (double x,int i){
	double val=1.0;
	while (i--)
	val *=x;
	return val;
}

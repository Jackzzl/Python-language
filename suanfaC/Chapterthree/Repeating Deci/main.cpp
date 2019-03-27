/* 只能判断从开始循环的数列
#include <iostream>
using namespace std;

int main() {
    int a,b;
    int c,d,e,f;
    int outnumber[100];
    cout << "input two number!" <<endl;
    cin>>a;
    cin>>b;
    c=a/b;
    d=a%b;
    //printf("%d,%d\n",c,d);
    e=d*10/b;
    f=d*10%b;
    outnumber[0]=e;
    for(int i=1;;i++){
        e=f*10/b;
        f=f*10%b;
        printf("%d,%d\n",e,f);
        outnumber[i]=e;
        if(f==d)
            break;
    }
    printf("%d.",c);
    for(int i;i<sizeof(outnumber);i++){
        if(outnumber[i]==d)
            printf("(%d",outnumber[i]);
        else
            printf("%d",outnumber[i]);
    }
    printf(")");

}
 思路，将所有余数放进数组里，添加for循环去比较数组
 */
#include <iostream>
#include <map>
#include <cassert>

using namespace std;
const int MAX =3000+5;
map<int,int> Pos;
void solve(int n,const int d,string& ans,int& r) {//n为a%d取余,d为分母,
    assert(n%d && n<d);//检测错误
    ans = ".";
    Pos.clear();
    while (true) {
        n *= 10;
        int p = Pos[n];
        if (p == 0)
            Pos[n] = ans.size();
        else {
            r = ans.size() - p;//寻找循环节
            if (r > 50) {
                ans.erase(p + 50);
                ans += "...";
            }
            ans.insert(p, "(");
            ans += ')';
            break;
        }
        if (n < d) {
            ans += '0';
            continue;
        }
        int div = n / d, mod = n % d;
        ans += (char) (div + '0');
        n = mod;
        if (n == 0) {
            ans += "(0)";
            r = 1;
            break;
        }
    }
}
    int main(){
        int a,b;
        while(scanf("%d%d",&a,&b)==2){
            string ans =".(0)";
            int r=1;
            if(a%b)
                solve(a%b,b,ans,r);
            printf("%d/%d=%d%s\n",a,b,a/b,ans.c_str());
            printf("  &d=number of digits in reqeating cycle\n\n",r);
        }
        return 0;
    }
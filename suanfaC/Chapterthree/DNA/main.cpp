#include <cstdio>
#include <cassert>
#include <cctype>
#include <functional>
#include <algorithm>
#include <cstring>
#include <string>
#include <iostream>
#include <vector>

using namespace std;

struct ChCnt {
    int cnt;
    char c;
    void init(char ch ='A'){
        c=ch;
        cnt =0;
    }
    ChCnt(){init();}
    bool operator<(const ChCnt& cc2)const{
        return cnt >cc2.cnt||(cnt ==cc2.cnt&&c<cc2.c);
    }
};
int main() {
    int T=1,m,n;
    cin>>T;
    string line;
    vector<string> seqs;
    char IDX[256]={0};
    IDX['A']=0;IDX['C']=1;IDX['G']=2;IDX['T']=3;
    while(T--){
        seqs.clear();
        cin>>m>>n;
        for(int i=0;i<m;i++){
            cin>>line;
            assert(line.size()==m);
            seqs.push_back(line);
        }
        string ansStr;
        int ans=0;
        vector<ChCnt>ccs(4);
        for(int i=0;i<n;i++){
            ccs[0].init('A');
            ccs[0].init('C');
            ccs[0].init('G');
            ccs[0].init('T');
            for(int j=0;j<m;j++)
                ccs[IDX[seqs[j][i]]].cnt++;
            sort(ccs.begin(),ccs.end());
            ansStr+=ccs.front().c;
            ans+=(m-ccs.front().cnt);
        }
        cout<<ansStr<<endl<<ans<<endl;
    }
    return 0;
}
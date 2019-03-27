
#include <cstdio>
#include <ctime>
#include <cstdlib>
#include <cstring>
#include <queue>
#include <string>
#include <set>
#include <stack>
#include <map>
#include <cmath>
#include <vector>
#include <iostream>
#include <algorithm>
 
#include <time.h>
#include <cstdlib>
using namespace std;
 
 
typedef long long LL;
 
const double MAX_VAL = (double)1e18;
 
const int MAX_GEN = 30;///最大迭代次数
const int MAX_SCALE = 3000;///最大种群规模
const int MAX_CITY = 20 + 2;///最大城市数
const double W_VAL = 0.729;///
 
 
struct SO{
    int x, y;
    SO(){}
    SO(int x, int y): x(x), y(y){}
};
 
struct Point{
    double x, y;
    Point(){}
    Point(int x, int y):x(x), y(y){};
    void read()
    {
        scanf("%lf%lf", &x, &y);
    }
};
 
inline int randomI(int x){ return rand()%x; }
inline double randomD(){ return (double)rand()/RAND_MAX; }
inline double getDist(Point a, Point b)
{
    return sqrt((a.x - b.x) * (a.x - b.x) + (a.y - b.y) * (a.y - b.y));
}
 
struct PSO{
    double w;
    int scale;
    int cityNum;
    int nowGen;///当前代数
    int maxGen;///迭代次数
    int bestNum;
    int bestGen;///最佳出现代数
 
    double dist[MAX_CITY][MAX_CITY];
 
    int oPop[MAX_SCALE][MAX_CITY];///粒子群
    double fitness[MAX_SCALE];///种群适应度，表示种群中各个个体的适应度
    vector<SO> listV[MAX_SCALE];/// 每科粒子的初始交换序列
 
    int Pd[MAX_SCALE][MAX_CITY];///一颗粒子历代中出现最好的解，
    double vPd[MAX_SCALE];///解的评价值
 
    int Pgd[MAX_CITY];/// 整个粒子群经历过的的最好的解，每个粒子都能记住自己搜索到的最好解
    double vPgd;/// 最好的解的评价值
 
    PSO(){}
    PSO(int s, int c, int mG, double ww, double d[MAX_CITY][MAX_CITY])
    {
        scale = s;
        cityNum = c;
        maxGen = mG;
        w = ww;
        for (int i = 0; i < cityNum; i++)
            for (int j = 0; j < cityNum; j++)
                dist[i][j] = d[i][j];
    }
    void copyArray(double a[], double b[], int n)
    {
        for (int i = 0; i < n; i++) a[i] = b[i];
    }
    void copyArray(int a[], int b[], int n)
    {
        for (int i = 0; i < n; i++) a[i] = b[i];
    }
 
    void init()
    {
        nowGen = 0;
        for (int i = 0; i < scale; i++)
        {
            for (int j = 0; j < cityNum; )
            {
                int x = randomI(cityNum);
                int r;
                for (r = 0; r < j; r++)
                {
                    if (x == oPop[i][r]) break;
                }
                if (r == j)
                {
                    oPop[i][j] = x;
//                    cout << oPop[i][j] << ' ';
                    j++;
                }
            }
//            cout << endl;
        }
 
        for (int i = 0; i < scale; i++)
        {
//            cout << i << " :" << endl;
            int vn = randomI(cityNum) + 1;
            for (int j = 0; j < vn; j++)
            {
                int x = randomI(cityNum);
                int y = randomI(cityNum);
                while (x == y) y = randomI(cityNum);
                SO so(x, y);
                listV[i].push_back(so);
//                cout << so.x << "*" << so.y << ' ';
            }
//            cout <<endl;
        }
 
 
        getFitness();
        for (int i = 0; i < scale; i++)
        {
            vPd[i] = fitness[i];
            copyArray(Pd[i], oPop[i], cityNum);
        }
        bestNum = 0;
        vPgd = fitness[0];
        bestGen = 0;
        for (int i = 0; i < scale; i++) if (vPgd > fitness[i])
        {
            vPgd = fitness[i];
            bestNum = i;
        }
        copyArray(Pgd, oPop[bestNum], cityNum);
    }
 
    double getVal(int x)
    {
        double ret = 0;
        for (int i = 0; i < cityNum; i++)
        {
            int xx = oPop[x][i % cityNum];
            int yy = oPop[x][(i + 1) % cityNum];
            ret += dist[xx][yy];
        }
        return ret;
    }
 
    void getFitness()
    {
        for (int i = 0; i < scale; i++)
            fitness[i] = getVal(i);
    }
 
    void UpdateVal()
    {
        int j = 0;
        double vj = fitness[0];
        for (int i = 0; i < scale; i++)
        {
            if (vPd[i] > fitness[i])
            {
                vPd[i] = fitness[i];
                copyArray(Pd[i], oPop[i], cityNum);///???
            }
            if (vj > fitness[i])
            {
                vj = fitness[i];
                j = i;
            }
        }
        if (vj < vPgd)
        {
            bestGen = nowGen;///
            bestNum = j;///
            vPgd = vj;
            copyArray(Pgd, oPop[j], cityNum);
        }
    }
 
	void changeTo(int a[], vector<SO> v)///
	{
	    int vn = v.size();
	    for (int i = 0; i < vn; i++)
        {
            int x = v[i].x, y = v[i].y;
            swap(a[x], a[y]);
        }
	}
 
	vector<SO> minus(int a[], int b[])///
	{
	    int c[MAX_CITY], d[MAX_CITY];
	    for (int i = 0; i < cityNum; i++) d[i] = b[i];
	    for (int i = 0; i < cityNum; i++) c[a[i]] = i;
        vector<SO> v;
        SO s;
        for (int i = 0; i < cityNum; i++)
        {
            if (d[i] != a[i])
            {
                s.x = i, s.y = c[a[i]];
                swap(d[s.x], d[s.y]);
                v.push_back(s);
            }
        }
        return v;
	}
 
	void addTo(vector<SO> &v, vector<SO> a, int vn)
	{
        for (int i = 0; i < vn; i++)
            v.push_back(a[i]);
	}
 
    /// Vii=wVi+ra(Pid-Xid)+rb(Pgd-Xid)
    void evolution()
    {
        for (int ig = 0; ig < maxGen; ig++)
        {
 
            nowGen = ig + 1;///nowGen
            for (int is = 0; is < scale; is++)
            {
                if (is == bestNum) continue;
                vector<SO> v;
                v.clear();
 
                int lvn = w * listV[is].size();
                addTo(v, listV[is], lvn);
 
                vector<SO> a = minus(Pd[is], oPop[is]);
                int an = randomD() * a.size();
                addTo(v, a, an);
 
                vector<SO> b = minus(Pgd, oPop[is]);
                int bn = randomD() * b.size();
                addTo(v, b, bn);
 
                listV[is] = v;
                changeTo(oPop[is], listV[is]);
//                cout << listV[is].size() << endl;
            }
            getFitness();
            UpdateVal();
        }
    }
 
    void solve()
    {
        init();
 
        evolution();
 
        printf("answer %lf:\n", vPgd);
        printf("solution \n");
        for (int i = 0; i < cityNum; i++)
        {
            if (i) printf(" ");
            printf("%d\n", Pgd[i]);
        }
        cout << bestGen << ' ' << bestNum << endl;
        puts("");
    }
 
};
 
int cn;
vector<Point> pv;
double d[MAX_CITY][MAX_CITY];
void pre(vector<Point> pv)
{
    int cn = pv.size();
    for (int i = 0; i < cn; i++)
        for (int j = i + 1; j < cn; j++)
        {
            d[i][j] = d[j][i] = getDist(pv[i], pv[j]);
        }
}
int main ()
{
    srand((unsigned long)time(0));  ///设置时间种子
    while (cin >> cn)
    {
        pv.clear();
        for (int i = 0; i < cn; i++)
        {
            Point p;
            p.read();
            pv.push_back(p);
        }
        pre(pv);
        PSO solver(MAX_SCALE, cn, MAX_GEN, W_VAL, d);
        cout << "***************************************************" << endl;
        solver.solve();
        cout << "***************************************************" << endl;
    }
    return 0;
}

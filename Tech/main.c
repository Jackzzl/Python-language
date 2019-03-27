#include <stdio.h>
#include <stdlib.h>
#define MAX 10
#define bool int
#define true 1
#define false 0
typedef struct Fact//事实节点，即事实与标号的映射
{
    int number;//事实的编号
    char content[20];//事实的内容
    int isconclusion;//事实是否是结论
    struct Fact *next;//指向下一个节点
}NFact,*PFact;
typedef struct Rule//规则节点，由条件推得结论
{
    int number;//规则的编号
    int premise[MAX];//规则的所有前提
    int conclusion;//规则的结论
    struct Rule *next;//指向下一个节点
}NRule,*PRule;
PFact TheFact;//事实库（链表）
PRule TheRule;//规则库（链表）

void getFact()//读取事实文件，获取事实与标号的映射
{
    struct Fact *q=TheFact;
    FILE *fp;
    if((fp = fopen("E:\\zzl\\clion\\workplace\\Tech\\fact.txt","r"))  == NULL)//打开文件
    {
        printf("cannot open file fact\n");
        return;
    }
    while (!feof(fp))//还没有读到文件末尾
    {
        PFact p = (PFact)malloc(sizeof(NFact));
        fscanf(fp,"%d %s",&(p->number),p->content);
        p->isconclusion=0;
        p->next=q->next;
        q->next=p;
        q=p;
    }
    fclose(fp);//关闭文件
}

void changefact_is(int k)//根据规则更改事实节点的标志位
{
    PFact p=TheFact->next;
    while (p!=NULL)//遍历事实库（链表）
    {
        if(p->number==k)//找到需要更改标志的事实节点
        {
            p->isconclusion=1;break;
        }
        p=p->next;
    }
}

void getRule()//读取规则文件，获取规则库
{
    int i,k,no=0,base;
    struct Rule *q=TheRule;
    FILE *fp;
    if((fp = fopen("E:\\zzl\\clion\\workplace\\Tech\\rule.txt","r"))  == NULL)//打开文件
    {
        printf("cannot open file rule\n");
        return;
    }
    fscanf(fp,"%d",&base);
    while (!feof(fp))//还没读到文件末尾
    {
        i=0;
        PRule p = (PRule)malloc(sizeof(NRule));
        p->number=++no;
        fscanf(fp,"%d",&k);
        while (k!=-1)//读取一条完整的规则
        {
            p->premise[i++]=k;
            fscanf(fp,"%d",&k);
        }
        p->premise[i]=k;
        fscanf(fp,"%d",&k);
        p->conclusion=k;
        if(p->number>base)//如果是终节点，则将节点的标志位置1
            changefact_is(p->conclusion);
        p->next=NULL;
        q->next=p;
        q=p;
    }
    fclose(fp);//关闭文件
}

void printfact()//输出事实库
{
    int num=0;
    PFact p=TheFact->next;
    printf("动物条件如下：\n");
    while(p!=NULL)//遍历事实库
    {
        if(p->isconclusion==0)
        {
            num++;
            printf("%2d:%-12s",p->number,p->content);
            if(num%5==0)printf("\n");
        }
        p=p->next;
    }
    printf("\n");
}
void initial()//初始化操作，读取事实文件，规则文件，产生知识库
{
    TheFact = (PFact)malloc(sizeof(NFact));
    TheFact->next = NULL;
    TheRule = (PRule)malloc(sizeof(NRule));
    TheRule->next = NULL;
    getFact();
    getRule();
    printfact();
}
void printcontent(int Data[MAX])//输出用户选择的条件
{
    printf("你选择的条件是：\n");
    for (int i=0;Data[i]!=-1;i++)//遍历输入的条件
    {
        PFact p=TheFact->next;
        while(p!=NULL)//遍历事实库，如果用户输入的数字与事实库的标号相等，则输出相应的事实（条件）
        {
            if(p->number==Data[i])
            {
                printf("%s ",p->content);break;
            }
            p=p->next;
        }
    }
    printf("\n");
}
void getdata(int Data[MAX])//获取用户输入的条件
{
    int i=0,k;
    printf("请输入条件，并以-1结束：\n");//用户输入条件，以-1结尾，-1不存储
    do
    {
        scanf("%d",&k);
        Data[i++]=k;
    }while(k!=-1);
    printcontent(Data);//回显用户刚输入的条件
}

bool judgein(int k,int Data[MAX])//判断k是否在Data数组中
{
    for (int i=0;Data[i]!=-1;i++)//遍历Data数组
        if(k==Data[i])
            return true;
    return false;
}

void change(PRule p,int Data[MAX])//当搜索到中间节点，则将中间节点推出的结论置换输入的条件
{
    int i,j=0,current[MAX];
    current[j++]=p->conclusion;
    current[j]=-1;
    for ( i=0;Data[i]!=-1;i++)//遍历用户输入的条件
    {
        if(!judgein(Data[i],p->premise))//判断某一条件是否在规则库中
            if(!judgein(Data[i],current))//判断某一条件是否在current数组中，如果都不在，则复制到current数组中
            {
                current[j++]=Data[i];current[j]=-1;
            }
    }
    for ( i=0;i<=j;i++)//将current数组复制到data数组
        Data[i]=current[i];

}
bool AinB(int a[MAX],int b[MAX])//判断A数组是否为B数组的子集
{
    for (int i=0;a[i]!=-1;i++)
    {
        if (!judgein(a[i],b))
            return false;
    }
    return true;
}
int count(int Data[MAX])//返回数组中条件的个数，不包括-1
{
    int i;
    for (i=0;Data[i]!=-1;i++)
    {
    }
    return i;
}
void printresult(int k)//输出搜索结果
{
    PFact p=TheFact->next;
    while(p!=NULL)//遍历事实库，找到下标为k的规则
    {
        if(k==p->number)break;
        p=p->next;
    }
    if(p->isconclusion)//如果该事实节点为结论，则搜索成功，否则搜索失败
        printf("该动物为:%s\n",p->content);
    else
        printf("找不到该动物\n");
}
void search(int Data[MAX])//搜索函数
{
    int backup[MAX];
    int i;
    PRule p=TheRule->next;
    for (i=0;Data[i]!=-1;i++)//遍历用户输入的条件，然后备份到backup数组中
        backup[i]=Data[i];
    backup[i]=-1;
    while (p!=NULL)//遍历规则库
    {
        if(AinB(p->premise,Data))//如果规则库中的某一规则是用户输入条件的子集，即搜索到中间节点，则输出该规则
        {
            printf("使用了规则:%d\n",p->number);
            change(p,Data);
        }
        p=p->next;
    }
    if(count(Data)!=1)//输入条件是否匹配完，输入的条件只剩下一条时，则搜索结束
    {
        if(AinB(backup,Data))
        {
            if(AinB(Data,backup))//匹配失败
                printf("找不到该动物\n");
        }
        else
            search(Data);//递归搜索输入条件
    }
    else//搜索成功
        printresult(Data[0]);
}

int main()
{
    int Data[MAX];
    char c;
    initial();//读取事实文件和规则文件，产生知识库
    do
    {
        getdata(Data);//获取用户输入的条件
        search(Data);//搜索
        printf("按Y继续查找，按N退出程序：\n");
        c=getchar();//跳过搜索输入的回车
        c=getchar();//输入的字符
    }while (c!='N'&&c!='n');
    printf("程序运行结束\n");
    return 0;
}
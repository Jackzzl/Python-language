#include<stdio.h>
#include<stdlib.h>
#include<math.h>
// 八数码状态对应的节点结构体
struct Node{
    int s[3][3];// 保存八数码状态， 0 代表空格
    int f,g;// 启发函数中的f 和g 值
    struct Node * next;
    struct Node *previous;// 保存其父节点
};
int open_N=0; // 记录Open 列表中节点数目
// 八数码初始状态
int inital_s[3][3]={
        2,8,3,
        1,6,4,
        7,0,5
};
// 八数码目标状态
int final_s[3][3]={
        1,2,3,
        8,0,4,
        7,6,5
};
//------------------------------------------------------------------------
// 添加节点函数入口，方法：通过插入排序向指定表添加
//------------------------------------------------------------------------
void Add_Node( struct Node *head, struct Node *p)
{
    struct Node *q;
    if(head->next)// 考虑链表为空
    { q = head->next;
        if(p->f < head->next->f){// 考虑插入的节点值比链表的第一个节点值小
            p->next = head->next;
            head->next = p;
        }
        else {
            while(q->next)// 考虑插入节点x，形如a<= x <=b
            {
                if((q->f < p->f ||q->f == p->f) && (q->next->f > p->f ||
                                                    q->next->f == p->f)){
                    p->next = q->next;
                    q->next = p;
                    break;
                }
                q = q->next;
            }
            if(q->next == NULL) // 考虑插入的节点值比链表最后一个元素的值更大
                q->next = p;
        }
    }
    else head->next = p;
}
//------------------------------------------------------------------------
// 删除节点函数入口
//------------------------------------------------------------------------
void del_Node(struct Node * head, struct Node *p )
{
    struct Node *q;
    q = head;
    while(q->next)
    {
        if(q->next == p){
            q->next = p->next;
            p->next = NULL;
            if(q->next == NULL) return;
// free(p);
        }
        q = q->next;
    }
}
//------------------------------------------------------------------------
// 判断两个数组是否相等函数入口
//------------------------------------------------------------------------
int equal(int s1[3][3], int s2[3][3])
{
    int i,j,flag=0;
    for(i=0; i< 3 ; i++)
        for(j=0; j< 3 ;j++)
            if(s1[i][j] != s2[i][j]){flag = 1; break;}
    if(!flag)
        return 1;
    else return 0;
}
//------------------------------------------------------------------------
// 判断后继节点是否存在于Open或Closed表中函数入口
//------------------------------------------------------------------------
int exit_Node(struct Node * head,int s[3][3], struct Node *Old_Node)
{
    struct Node *q=head->next;
    int flag = 0;
    while(q)
        if(equal(q->s,s)) {
            flag=1;
            Old_Node->next = q;
            return 1;}
        else q = q->next;
    if(!flag) return 0;
}
//------------------------------------------------------------------------
// 计算p(n)的函数入口
// 其中p(n)为放错位的数码与其正确的位置之间距离之和
// 具体方法：放错位的数码与其正确的位置对应下标差的绝对值之和
//------------------------------------------------------------------------
int wrong_sum(int s[3][3])
{
    int i,j,fi,fj,sum=0;
    for(i=0 ; i<3; i++)
        for(j=0; j<3; j++)
        {
            for(fi=0; fi<3; fi++)
                for(fj=0; fj<3; fj++)
                    if((final_s[fi][fj] == s[i][j])){
                        sum += fabs(i - fi) + fabs(j - fj);
                        break;
                    }
        }
    return sum;
}
//------------------------------------------------------------------------
// 获取后继结点函数入口
// 检查空格每种移动的合法性，如果合法则移动空格得到后继结点
//------------------------------------------------------------------------
int get_successor(struct Node * BESTNODE,int direction,struct Node*Successor)//扩展BESTNODE，产生其后继结点SUCCESSOR
{
    int i,j,i_0,j_0,temp;
    for(i=0; i<3; i++)
        for(j=0; j<3; j++)
            Successor->s[i][j] = BESTNODE->s[i][j];
// 获取空格所在位置
    for(i=0; i<3; i++)
        for(j=0; j<3; j++)
            if(BESTNODE->s[i][j] == 0){i_0 = i; j_0 = j;break;}
    switch(direction)
    {
        case 0: if((i_0-1)>-1 ){
                temp = Successor->s[i_0][j_0];
                Successor->s[i_0][j_0] = Successor->s[i_0-1][j_0];
                Successor->s[i_0-1][j_0] = temp;
                return 1;
            }
            else return 0;
        case 1: if((j_0-1)>-1){
                temp = Successor->s[i_0][j_0];
                Successor->s[i_0][j_0] = Successor->s[i_0][j_0-1];
                Successor->s[i_0][j_0-1] = temp;
                return 1;
            }
            else return 0;
        case 2: if( (j_0+1)<3){
                temp = Successor->s[i_0][j_0];
                Successor->s[i_0][j_0] = Successor->s[i_0][j_0+1];
                Successor->s[i_0][j_0+1] = temp;
                return 1;
            }
            else return 0;
        case 3: if((i_0+1)<3 ){
                temp = Successor->s[i_0][j_0];
                Successor->s[i_0][j_0] = Successor->s[i_0+1][j_0];
                Successor->s[i_0+1][j_0] = temp;
                return 1;
            }
            else return 0;
    }
}
//------------------------------------------------------------------------
// 从OPen表获取最佳节点函数入口
//------------------------------------------------------------------------
struct Node * get_BESTNODE(struct Node *Open)
{
    return Open->next;
}
//------------------------------------------------------------------------
// 输出最佳路径函数入口
//------------------------------------------------------------------------
void print_Path(struct Node * head)
{
    struct Node *q, *q1,*p;
    int i,j,count=1;
    p = (struct Node *)malloc(sizeof(struct Node));
// 通过头插法变更节点输出次序
    p->previous = NULL;
    q = head;
    while(q)
    {
        q1 = q->previous;
        q->previous = p->previous;
        p->previous = q;
        q = q1;
    }
    q = p->previous;
    while(q)
    {
        if(q == p->previous)printf("八数码的初始状态： \n");
        else if(q->previous == NULL)printf("八数码的目标状态： \n");
        else printf("八数码的中间态%d\n",count++);
        for(i=0; i<3; i++)
            for(j=0; j<3; j++)
            {
                printf("%4d",q->s[i][j]);
                if(j == 2)printf("\n");
            }
        printf("f=%d, g=%d\n\n",q->f,q->g);
        q = q->previous;
    }
}
//------------------------------------------------------------------------
//A* 子算法入口:处理后继结点
//------------------------------------------------------------------------
void sub_A_algorithm(struct Node * Open, struct Node * BESTNODE,
                     struct Node * Closed,struct Node *Successor)
{
    struct Node * Old_Node = (struct Node *)malloc(sizeof(struct Node));
    Successor->previous = BESTNODE;// 建立从successor返回BESTNODE的指针
    Successor->g = BESTNODE->g++;// 后继结点的g值
// 检查后继结点是否已存在于Open 和Closed表中，如果存在：该节值和表中old_Node 节点
//g 值，前者小代表新的路径比老路径更好， 将Old_Node 的父节点改为BESTNODE，并修改其f， g 值，后者小则什么也不做。
// 即不存在Open 也不存在Closed表则将其加入OPen表，并计算其f值
    if( exit_Node(Open, Successor->s, Old_Node) ){
        if(Successor->g < Old_Node->g){
            Old_Node->next->previous = BESTNODE;// 将Old_Node 的父节点改为BESTNODE
            Old_Node->next->g = Successor->g;// 改g 值
            Old_Node->next->f = Old_Node->g +
                                wrong_sum(Old_Node->s);//修改f 值
// 排序~~~~~~~~~~~~~~~~~~
            del_Node(Open, Old_Node);
            Add_Node(Open, Old_Node);
        }

    }
    else if( exit_Node(Closed, Successor->s, Old_Node)){
        if(Successor->g < Old_Node->g){
            Old_Node->next->previous = BESTNODE;
            Old_Node->next->g = Successor->g;
            Old_Node->next->f = Old_Node->g + wrong_sum(Old_Node->s);
// 排序~~~~~~~~~~~~~~~~~~
            del_Node(Closed, Old_Node);
            Add_Node(Closed, Old_Node);
        }
    }
    else {
        Successor->f = Successor->g + wrong_sum(Successor->s);
        Add_Node(Open, Successor);
        open_N++;
    }
}
//------------------------------------------------------------------------
//A* 算法入口
// 八数码问题的启发函数为： f(n)=d(n)+p(n)
// 其中A* 算法中的g(n)根据具体情况设计为d(n)，意为n 节点的深度，而h(n)设计为p(n)，
// 意为放错的数码与正确的位置距离之和
//------------------------------------------------------------------------
void A_algorithm(struct Node * Open, struct Node * Closed) //A*算法
{
    int i,j;
    struct Node * BESTNODE, *inital, * Successor;
    inital = (struct Node * )malloc(sizeof(struct Node));
// 初始化起始节点
    for(i=0; i<3; i++)
        for(j=0; j<3; j++)
            inital->s[i][j] = inital_s[i][j];
    inital->f = wrong_sum(inital_s);
    inital->g = 0;
    inital->previous = NULL;
    inital->next = NULL;
    Add_Node(Open, inital);// 把初始节点放入OPEN表
    open_N++;
    while(1)
    {
        if(open_N == 0){printf("failure!"); return;}
        else {
            BESTNODE = get_BESTNODE(Open);//OPEN表获取f值最小的BESTNODE，将其从OPEN表删除并加入CLOSED表中
            del_Node(Open, BESTNODE);
            open_N--;
            Add_Node(Closed, BESTNODE);
            if(equal(BESTNODE->s, final_s)) {// 断BESTNODE是否为目标节点
                printf("success!\n");
                print_Path(BESTNODE);
                return;
            }
// 针对八数码问题，后继结点Successor的扩展方法：空格（二维数组中的0）上下左右移动，
// 判断每种移动的有效性， 有效则转向A*子算法处理后继节点，否则进行下一种移动
            else{
                Successor = (struct Node * )malloc(sizeof(struct Node));
                Successor->next = NULL;
                if(get_successor(BESTNODE, 0,
                                 Successor))sub_A_algorithm( Open, BESTNODE, Closed, Successor);
                Successor = (struct Node * )malloc(sizeof(struct Node));
                Successor->next = NULL;
                if(get_successor(BESTNODE, 1,
                                 Successor))sub_A_algorithm( Open, BESTNODE, Closed, Successor);
                Successor = (struct Node * )malloc(sizeof(struct Node));
                Successor->next = NULL;
                if(get_successor(BESTNODE, 2,
                                 Successor))sub_A_algorithm( Open, BESTNODE, Closed, Successor);
                Successor = (struct Node * )malloc(sizeof(struct Node));
                Successor->next = NULL;
                if(get_successor(BESTNODE, 3,
                                 Successor))sub_A_algorithm( Open, BESTNODE, Closed, Successor);
            }
        }
    }
}
//------------------------------------------------------------------------
//main() 函数入口
// 定义Open 和Closed列表。Open 列表： 保存待检查节点。Closed列表：保存不需要再检查的节点
//------------------------------------------------------------------------
int main()
{
    struct Node * Open = (struct Node * )malloc(sizeof(struct Node));
    struct Node * Closed = (struct Node * )malloc(sizeof(struct Node));
    Open->next = NULL ; Open->previous = NULL;
    Closed->next =NULL; Closed->previous = NULL;
    A_algorithm(Open, Closed);
    return 0;
}

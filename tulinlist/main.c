#include "stdio.h"
#include "string.h"
#include "stdlib.h"

#define MAX 50 // 最大顶点个数
#define QUEUESIZE 50
typedef struct node {
    int adjvex; // 顶点序号
    struct node *next;
} ArcNode, *PArcNode;

// 顶点头信息
typedef struct {
    ArcNode *head;
} VexNode;

typedef struct {
    VexNode lists[MAX];
    int vexes; // 顶点数
    int edges; // 边数
    int visited[MAX]; // 用于判断是否访问
} VGraph, *AdjList;

typedef struct {
    int items[QUEUESIZE];
    int front, rear;
    int count;
} SqQueue;

SqQueue sqQueue;

/** initialize the queue
 * to assist the solution of BSF
 * @param sqQueue
 * @return {@code 1} if the function works well
 */
int initQueue(SqQueue *sqQueue) {
    sqQueue->front = 0;
    sqQueue->rear = 0;
    sqQueue->count = 0;
    return 1;
}

/** judge whether the sqQueue is empty or not
 *
 * @param sqQueue
 * @return {@code 0} if SqQueue is not empty
 *   while {@code 1} if SqQueue is empty
 */
int isQueueEmpty(SqQueue sqQueue) {
    if (sqQueue.count == 0) {
        return 1;
    }
    return 0;
}

/** enqueue
 *
 * @param sqQueue
 * @param newItem
 * @return {@code 0} if enqueue operation fail
 *   while {@code 1} if enqueue operation success
 */
int enQueue(SqQueue *sqQueue, int newItem) {
    if (sqQueue->rear == sqQueue->front && sqQueue->count == QUEUESIZE) {
        printf("the queue is full");
        return 0;
    }
    sqQueue->items[sqQueue->rear] = newItem;
    sqQueue->rear = (sqQueue->rear + 1) % QUEUESIZE;
    sqQueue->count++;
    return 1;
}

/** deQueue
 *
 * @param sqQueue
 * @param deQueueItem
 * @return {@code 0} if delete operation fail
 *   while {@code 1} if delete operation success
 */
int deQueue(SqQueue *sqQueue) {
    if (sqQueue->count == 0) {
        printf("fail to deQueue because the queue is empty");
        return 0;
    }
    int deleteItem;
    deleteItem = sqQueue->items[sqQueue->front];
    sqQueue->front = (sqQueue->front + 1) % QUEUESIZE;
    sqQueue->count--;
    return deleteItem;
}

/**
 * 初始化邻接矩阵
 * @param adjMatrix
 */
void initGraph(VGraph *vGraph) {
    vGraph->vexes = 0;
    vGraph->edges = 0;
}

void createGraph(AdjList *adjList, int m[][MAX]) {
    PArcNode p;
    (*adjList)->edges = 0;
    for (int i = 0; i < (*adjList)->vexes; i++) {
        (*adjList)->lists[i].head = NULL;
        for (int j = (*adjList)->vexes - 1; j >= 0; j--)
            if (m[i][j] != 0) {
                p = (PArcNode) malloc(sizeof(ArcNode));
                p->adjvex = j;
                p->next = (*adjList)->lists[i].head;
                (*adjList)->lists[i].head = p;
                (*adjList)->edges++;
            }
    }
    memset((*adjList)->visited, 0, sizeof((*adjList)->visited));
}

/**
 * 深度优先遍历
 * @param adjMatrix
 * @param row
 */
void DFS(VGraph *vGraph, int row) {
    PArcNode node = vGraph->lists[row].head;
    if (vGraph->visited[row] == 0) {
        printf("%d", row);
        vGraph->visited[row] = 1;
    }
    while (node != NULL) {
        if (vGraph->visited[node->adjvex] == 0) {
            printf("%d", node->adjvex);
            vGraph->visited[node->adjvex] = 1;
            DFS(vGraph, node->adjvex);
        }
        node = node->next;
    }
}

void printtt(VGraph vGraph) {
    for (int i = 0; i < vGraph.vexes; ++i) {
        PArcNode node = vGraph.lists[i].head;
        while (node != NULL) {
            printf("%d", node->adjvex);
            node = node->next;
        }
        printf("\n");
    }
}

// 假设没有孤立的点，从第一行开始
void BFS(VGraph *vGraph) {
    enQueue(&sqQueue, 0);
    while (!isQueueEmpty(sqQueue)) {
        int index = deQueue(&sqQueue);
        printf("%d", index);
        vGraph->visited[index] = 1;
        PArcNode node = vGraph->lists[index].head;
        while (node != NULL) {
            if (vGraph->visited[node->adjvex] == 0) {
                enQueue(&sqQueue, node->adjvex);
                vGraph->visited[node->adjvex] = 1;
            }
            node = node->next;
        }
    }
}

void menu(VGraph *vGraph) {
    printf("欢迎光临 邻接表操作界面!\n");
    printf("您可以进行以下选择\n");
    while (1) {
        printf("\n");
        printf("1.创建邻接表 2.深度遍历 3.广度遍历 4.退出系统\n");
        printf("请选择：");
        int option; // 选项
        int num[MAX][MAX];
        // 当输入是字符或字符串时，会出现无限循环的现象，并未查明具体原因
        scanf("%d", &option); // NOLINT
        getchar();
        switch (option) {
            case 1:
                if (vGraph->vexes != 0) {
                    printf("已创建邻接矩阵");
                    break;
                }
                printf("请输入顶点数目: ");
                scanf("%d", &vGraph->vexes); // NOLINT
                printf("请输入矩阵(1为两点有连接,0为没有)：\n");
                for (int i = 0; i < vGraph->vexes; ++i) {
                    for (int j = 0; j < vGraph->vexes; ++j) {
                        scanf("%d", &num[i][j]); // NOLINT
                    }
                }
                createGraph(&vGraph, num);
                break;
            case 2:
                if (vGraph->vexes == 0) {
                    printf("请先创建邻接矩阵\n");
                    break;
                }
                // 从第一个开始深度遍历
                DFS(vGraph, 0);
                printf("\n");
                memset(vGraph->visited, 0, sizeof(vGraph->visited));
                break;
            case 3:
                if (vGraph->vexes == 0) {
                    printf("请先创建邻接矩阵\n");
                    break;
                }
                BFS(vGraph);
                printf("\n");
                memset(vGraph->visited, 0, sizeof(vGraph->visited));
                break;
            case 4:
                return;
            default:
                printf("请正确输入选项\n");
                break;
        }
    }
}

int main() {
    initQueue(&sqQueue);
    VGraph vGraph;
    initGraph(&vGraph);
    menu(&vGraph);
}
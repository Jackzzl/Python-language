package Test2;
/*
 * 赵卓良
 * @author
 * @version 2018 4-19
 * */

import java.util.Arrays;
import java.util.Scanner;

public class Test2 {
    public static void main(String[] args){
        int [] a= new int[100];
        for(int i=0;i<=99; i++){
            a[i]=i;
        }
        System.out.println("请输入要查看的数组序号：");

        Scanner ad = new Scanner(System.in);
        int b=ad.nextInt();
        System.out.println("结果为："+a[b]);/**/
        /*for(int element : a){
            System.out.println(element);
        }//输出的第二钟方式 for each 循环*/
        System.out.println(Arrays.toString(a));//输出一个String字符串

        //数组计数是从0开始
        //代码报错，访问a[]数组不可以使用a[ad]这种方式，为重新定义了数组长度，数组定义后无法改变长度，java.lang.ArrayIndexOutOfBoundsException: 100
        /*for(int i=0;i<a.length;i++){
            System.out.println(a[i]);
        }*/
    }
}

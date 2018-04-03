package SumFactorlai;

import java.util.Scanner;
/*
* zzl
* version 2018 4-3
* */
public class SumFactorial {
    public static int N;
    public static long factorial(int n){
        if (n==1)
            return 1L;
        else
            return n*factorial(n-1);
    }
    public static long sumFactorial(int n){
        long sum = 0;
        for(int i=1;i<=n;i++){
            sum+=factorial(i);
        }
        return sum;
    }
    public static void main(String[] args){
        try {
            Scanner scanner = new Scanner(System.in);
            System.out.println("输入想求和的阶乘值");
            N = scanner.nextInt();
            scanner.close();
        }catch(Exception e){
            System.out.println("输入数据有误");
            System.out.println("错误信息"+e.getMessage());
        }
        System.out.println("计算结果为"+sumFactorial(SumFactorial.N));

    }
}

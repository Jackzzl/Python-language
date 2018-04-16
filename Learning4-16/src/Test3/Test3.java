package Test3;
/*
* @version 2018 4-16
* @author zzl
* */
import java.math.*;
import java.util.*;
public class Test3 {
    public static void main(String[]args){
        Scanner in = new Scanner(System.in);

        System.out.println("How many number do you need to draw?");
        int k = in.nextInt();

        System.out.println("What is the highest number you can draw?");
        int n = in.nextInt();

        BigInteger lottoryOdds =BigInteger.valueOf(1);

        for(int i=1;i<=k;i++){
            lottoryOdds=lottoryOdds.multiply(BigInteger.valueOf(n-i+1)).divide(BigInteger.valueOf(i));

            System.out.println("You odds are 1 in "+lottoryOdds+".GoodLuck!");
        }
    }
}

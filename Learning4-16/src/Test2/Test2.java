package Test2;
/*
* @version 2018 4-16
* @author zzl
* */
import java.util.*;
public class Test2 {
    public static void main(String[] args){
        Scanner in = new Scanner(System.in);

        System.out .println("how many numbers do you need to draw?");
        int k = in.nextInt();

        System.out.println("what is the highest number you can draw?");
        int n = in.nextInt();

        int lotteryOdds =1;
        for(int i=1;i<k;i++){
            lotteryOdds= lotteryOdds*(n-i+1)/i;
            System.out.println("You odds are 1 in"+lotteryOdds+". Good Luck!");
        }
    }
}

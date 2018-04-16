package Test;
/*
* @vesrion 4-16
* @author zzl
* */
import java.util.*;
public class Test1 {
    public static void main(String[] args){
        //read input
        Scanner in = new Scanner(System.in);
        System.out.println("How much money do need t0 oretire?");
        double goal = in.nextDouble();

        System.out.println("how much money do you contribute every year?");
        double payment = in.nextDouble();

        System.out.println("Interest rate in %:");
        double interestRate = in.nextDouble();

        double balance =0;
        int years =0;

        //update account balance while goal isnot reach
        while(balance<goal){
            //add this year`s payment and interest
            balance+=payment;
            double interest = balance*interestRate/10;
            years++;
        }
        System.out.println("You are retire in"+years+"years.");
    }
}

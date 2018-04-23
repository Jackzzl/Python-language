package TestArray5;
import java.util.*;
/*
* @author zzl
* @version 2018 4-19
* */
public class TestArray {
    public static void main(String[] args){
        Scanner in = new Scanner(System.in);

        System.out.println("How much number do you need to draw");
        int k = in.nextInt();

        System.out.println("What is the highest number you can draw");
        int n = in.nextInt();
        //fill an array with the number 123

        int[] numbers=new int [n];
        for(int i =0;i<numbers.length;i++){
            numbers[i]=i+1;
        }
        int[] result = new int[k];
        for(int i=0;i<result.length;i++){
            //make a random indox between 0 and n-1
            int r= (int)(Math.random()*n);//强制类型转换

            result[i]= numbers[r];
            //move the last element into the random location
            numbers[r]=numbers[n-1];
            n--;
        }
        //print the sorted Array
        Arrays.sort(result);
        System.out.println("Bet the following combination. It`s make you rich!");
        for(int r:result)
            System.out.println(r);

    }
}

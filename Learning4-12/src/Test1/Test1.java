package Test1;
import java.util.*;
/*
* zzl
* version 2018 4-12
* Sting 练习
*
* */
public class Test1 {
    public static void main(String[] args){
        Scanner in = new Scanner(System.in);
        //get first name
        System.out.print("What is your name?");
        String name = in.nextLine();

        //get second imformation
        System.out.print("How old are you?");
        int age = in.nextInt();

        System.out.println("Hello,"+name+". Next year, you`ll be "+(age+1));
    }
}

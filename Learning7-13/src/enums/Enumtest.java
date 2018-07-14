package enums;
/*
* @author zzl
* @date 2018-7-13
* */
import java.util.*;
public class Enumtest {
    public static void main(String[] args){
        Scanner in =new Scanner(System.in);
        System.out.print("Enter a size: (SMALL, MEDIUM, LARGE, EXTRA_LARGE)");
        String input=in.next().toUpperCase();
        Size size=Enum.valueOf(Size.class, input);
        System.out.println("size="+size);
        System.out.println("abbreviatin="+size.getAbbreiation());
        if(size==Size.EXTRA_LARGE)
            System.out.println("Good job--you paid attention to the");
    }
}

enum Size{
    SMALL("S"), MEDIUM("M"), LARGE("L"), EXTRA_LARGE("XL");
    private Size(String abbreviation){this.abbreviation=abbreviation;}
    public String getAbbreiation(){
        return abbreviation;
    }
    private String abbreviation;
}

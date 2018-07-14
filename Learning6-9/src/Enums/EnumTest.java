package Enums;

import java.util.*;

/*
* @author zzl
* @version 2018 6-9
* @goal learn enum
* */
public class EnumTest {
    public static void main(String[] args){
        Scanner in= new Scanner(System.in);
        System.out.println("Enter a size:(Small, Medium,Lager,EXTRA_LARGE)");
        String input=in.next().toUpperCase();
        Size size=Enum.valueOf(Size.class,input);
        System.out.println("abbreviation="+size.getAbbreviation());
        if(size==size.EXTRA_LARGE)
            System.out.println("Good job-- you paid attention to the _.");

    }
}
enum Size{
    Small("S"),Medium("M"),Lager("L"),EXTRA_LARGE("Xl");
    private String abbreviation;
    private Size(String abbreviation){
        this.abbreviation=abbreviation;
    }
    public String getAbbreviation(){
        return abbreviation;
    }
    //private String abbreviation;
}

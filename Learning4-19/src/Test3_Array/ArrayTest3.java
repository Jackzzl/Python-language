package Test3_Array;
/*
* 赵卓良
* @author
* @version 2018 4-19
* */
import java.util.Arrays;

public class ArrayTest3 {//ArraycopyOf的复制(Array,Array.length)
    public static void main(String[] args) {
        int[] a = new int[100];
        for (int i = 0; i <= 99; i++) {
            a[i] = i;
        }
        int[] copied= Arrays.copyOf(a,a.length);
        for(int element:copied){
            System.out.println(element);
        }
    }
}

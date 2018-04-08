/**
 * zzl
 * version 2018 4-8
 * */
package Test4;
import java.util.Scanner;
public class Test4 {//对于三元操作符的应用 输出较小的数字
    public static void main(String[] args){
        float x=0;
        float y=0;
        Scanner scanner = new Scanner(System.in);
            try{System.out.println("请输入两个数字");
                x =scanner.nextFloat();
                System.out.println("请输入第二个数字");
                y=scanner.nextFloat();
            }catch(Exception e){
            System.out.println("输入数据错误");
            System.out.println("错误信息"+e.getMessage());

        }
        System.out.println(x<y?x:y);
    }
}

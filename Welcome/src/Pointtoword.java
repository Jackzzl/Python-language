import java.util.Scanner;
/*
version 2018 4-2
* zzl
* */
public class Pointtoword {
    public static String pointtoword(int grad){
        //输入分数转换为文字
        String result= null;
        switch(grad){
            case 10:
            case 9:
                result = "优";
                break;
            case 8:
                result = "良";
                break;
            case 7:
                result = "中";
                break;
            case 6:
                result = "及格";
                break;
            default:
                result= "不及格";

        }
        return result;
    }
    public static void main(String[] args){
        float point = 0;
        try{
            Scanner scanner= new Scanner(System.in);
            System.out.print("请输入分数(0-100)：");
            point = scanner.nextFloat();
            scanner.close();
        }catch(Exception e){
            System.out.println("输入信息有误");
            System.out.println("错误信息"+e.getMessage());
        }
        if(0<=point&&point<=100){
            System.out.println("成绩是："+pointtoword((int)point/10));
        }else{
            System.out.println("error"+point);
        }
    }
}

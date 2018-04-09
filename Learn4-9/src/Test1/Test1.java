package Test1;
//强制类型转换test
public class Test1 {
    public static void main(String[] args){
        double x = 9.8900;
        int nx = (int)x;
        int mx=(int)Math.round(x);
        System.out.println(nx);
        System.out.println(mx);
    }
}

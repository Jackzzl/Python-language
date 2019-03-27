package UDC;
import java.util.*;
public class Udc {
    public static int N;//编码个数

    public static String[] Code;//信源编码
    public static ArrayList<String> list= new ArrayList<String>();
    public static void main(String[] args){
        new Udc().start();
    }

    void start(){

        init();
        if(!singular(Code)){
            Sardings_Patterson(Code);
        }
    }

    private void init(){
        int k=0;
        String str="";
        Scanner sc=new Scanner(System.in);
        System.out.print("请输入信源编码个数:N= ");
        N=sc.nextInt();

        Code= new String[N];

        System.out.print("请输入信源编码 C:");
        while(k<N){
            str=sc.next();
            Code[k]=str;
            k++;
        }
    }
    private boolean singular(String[] code2){
        String str="";
        int s=-1;
        for(int i=0;i<code2.length;i++){
            str=code2[i];
            for(int j=0;j<code2.length-1;j++) {
                if (i != j) {
                    s = code2[j].compareTo(str);
                }
                if (s == 0) {
                    System.out.println("是奇异！！！")；
                    return true;
                }

            }
        }
        return false;
    }

}

package Test1;
import java.io.*;
import javax.swing.JOptionPane;
public class Testone {//逐个输入并计算10个学生的平均成绩和最好成绩
    public static void main(String[] args)throws IOException{
        int k;
        int count=10 ;//count为学生个数
        double score[] = new double [count];
        double doubleSum=0.0;
        double doubleAver = 0.0;
        double maxScore=0.0;//定于初始的值
        boolean contiGo=true;
        String str;
        BufferedReader buf = new BufferedReader(new InputStreamReader(System.in));
        for(k=0;k<count;k++){
            while(contiGo){
                System.out.print("请输入第"+(k+1)+"个同学的成绩");
                str = buf.readLine();
                try{//处理输入非数值数据或是输入为0；
                    score[k]=Double.parseDouble(str);
                    if(0>score[k]||100<score[k]){
                        JOptionPane.showMessageDialog(null,"成绩不应该为<0,重新输入。","提示信息",JOptionPane.QUESTION_MESSAGE);

                    }else
                        break;
                }catch(Exception ne){
                    JOptionPane.showMessageDialog(null,"输入的不是数据，不符合规矩，重新输入","提示信息",JOptionPane.QUESTION_MESSAGE);

                }
            }
            doubleSum+=score[k];
            if(score[k]>maxScore)maxScore=score[k];
        }
        doubleAver = doubleSum/count;
        System.out.println("这"+count+"个学生的平均成绩是："+doubleAver);
        System.out.println("这"+count+"个同学的最好成绩为："+maxScore);
    }
}

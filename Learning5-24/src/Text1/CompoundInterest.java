package Text1;
/*
* @author zzl
* @data 2018-5-24
* */
public class CompoundInterest {
    public static void main(String[] args){
        final double STARTRATE =10;
        final int NRATES =6;
        final int NYEARS =10;

        double interestRate [] =new double [NRATES];
        for(int j=0;j<interestRate.length;j++){
            interestRate[j]=(STARTRATE+j)/100.0;
        }

        double balance [][]=new double[NYEARS][NRATES];
        for(int j=0;j<balance[0].length;j++){
            balance[0][j]=10000;
        }
        for(int i=1;i<balance.length;i++){
            for(int j=0;j<balance[i].length;j++){
                double oldBalance =balance[i-1][j];
                double interest =oldBalance*interestRate[j];
                balance[i][j]=oldBalance+interest;
            }

        }
        for(int j=0;j<interestRate.length;j++){

            System.out.printf("%9.0f%%",100*interestRate[j]);
        }
        System.out.println();
        for(double[] row:balance){

            for(double b : row)
                System.out.printf("%10.2f",b);

            System.out.println();
        }
        /*double [][] a=new double [10][9];
        System.out.print(a.length);*/
    }
}

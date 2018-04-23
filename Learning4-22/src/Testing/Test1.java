package Testing;
/*
* @version 4-22
* @authorzzl
*多元数组的练习
* */
public class Test1 {
    public static void main(String[] args){
        final double STARTRATE=10;
        final int NRATES=6;
        final int NYEARS=10;

        //set interset rates to 10
        double[]interestRate= new double[NRATES];
        for(int j=0;j<interestRate.length;j++)
            interestRate[j]=(STARTRATE+j)/100.0;
        double[][]blances = new double[NYEARS][NRATES];

        //set initial balances to 10000
        for(int j=0;j<=blances[0].length;j++)
            blances[0][j]=10000;

        //compute interest for furture years
        for(int i=1;i<blances.length;i++)
            for(int j=0;j<blances[i].length;j++) {
                double oldBlance = blances[i - 1][j];

                double interest = oldBlance * interestRate[j];

                blances[i][j]=oldBlance+interest;
            }
            for(int j=0;j<interestRate.length;j++)
                System.out.printf("%9.0f%%",100*interestRate[j]);
        System.out.println();

        for(double[] row:blances){
            for(double b:row)
                System.out.printf("%10.2f",b);
        }
    }

}

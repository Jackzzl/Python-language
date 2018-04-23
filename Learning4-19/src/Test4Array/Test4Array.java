package Test4Array;
/*
* @author zzl
* @version 2018 4-19
*
* */
public class Test4Array {
    public static void main(String[] args){
        if(args.length==0||args[0].equals("-h"))
            System.out.print("Hello");
        else if(args[0].equals("-g"))
            System.out.print("Goodbye");
        else if(args[1].equals("cruel"))
            System.out.print(" cruel");
        else if(args[2].equals("world"))
            System.out.print(" world");
        for(int i=1;i<args.length;i++)
            System.out.print(""+args[i]);
        System.out.println("!");
    }
}

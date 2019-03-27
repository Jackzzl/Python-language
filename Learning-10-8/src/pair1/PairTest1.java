package pair1;
/*
* @author zzl
* @version 2018-10-8
*
* */
public class PairTest1 {
    public static void main(String[] args){
        String[] words={"Mary","had","a","little","lamb"};
        Pair<String> mm=ArrayAlg.minmax(words);
        System.out.println("min="+mm.getFirst());
        System.out.println("max="+mm.getSecond());
    }
}

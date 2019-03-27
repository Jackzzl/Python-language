package shuffle;

import java.util.*;

/*
* @author zzl
* @version 2018-10-28
* */
public class ShuffleTest {
    public static void main(String[] args){
        List<Integer> numbers=new ArrayList<>();
        for(int i=1;i<=49;i++)
            numbers.add(i);
        Collections.shuffle(numbers);
        List<Integer>winninCombination=numbers.subList(0,6);
        Collections.sort(winninCombination);
        System.out.println(winninCombination);

    }
}

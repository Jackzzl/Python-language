package priorityQueue;
/*
* @author zzl
* @version2018-10-18
*
* */
import java.util.*;
import java.time.*;
public class PriorityQueueTest {
    public static void main(String[] args){
        PriorityQueue<LocalDate> pq=new PriorityQueue<>();
        pq.add(LocalDate.of(1996,12,4));
        pq.add(LocalDate.of(1990,1,1));
        pq.add(LocalDate.of(1903,11,1));
        pq.add(LocalDate.of(1910,6,22));

        System.out.println("Iterating over elements...");
        for(LocalDate date:pq)
            System.out.println(date);
        System.out.println("Removing elements...");
        while(!pq.isEmpty())
            System.out.println(pq.remove());
    }
}

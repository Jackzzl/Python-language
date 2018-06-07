package Test3;
import java.util.*;
/*
* @author zzl
* @data 2018 5-26
* */
public class Constrates {
    public static void main(String agrs[]){
        Employee []staff=new Employee[3];

        staff[0]=new Employee("Harry",40000);
        staff[1]=new Employee(60000);
        staff[2]=new Employee();

        for(Employee e:staff)
            System.out.println("name="+e.getName()+",id="+e.getId()+",salary="+e.getSalary());

    }
}

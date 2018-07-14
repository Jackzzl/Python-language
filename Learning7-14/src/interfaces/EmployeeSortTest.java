package interfaces;
/*
* @author zzl
* @vision 2018 7-14
* */
import java.util.*;
public class EmployeeSortTest {
    public static void main(String[] args){
        Employee[] staff= new Employee[3];

        staff[0]=new Employee("H",3000);
        staff[1]=new Employee("D",4000);
        staff[2]=new Employee("F",5000);

        Arrays.sort(staff);

        for(Employee e:staff)
            System.out.println("name="+e.getName()+",salary" +e.getSalary());

    }
}

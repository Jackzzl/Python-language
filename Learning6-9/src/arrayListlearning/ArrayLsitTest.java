package arrayListlearning;
/*
* @author zzl
* @version 2018 6-9
* @goal learn ArrayList
* */
import java.util.*;
public class ArrayLsitTest {
    public static void main(String[] args){
        //fill the staff array list with three Employee objects
        ArrayList<Employee> staff=new ArrayList<>();

        staff.add(new Employee("Carl",75000,1987,10,12));
        staff.add(new Employee("Sam",45000,1978,12,25));
        staff.add(new Employee("Jeff",30000,1980,2,4));

        for(Employee e:staff)
            e.raiseSalary(5);

        //print out information about all Employee object
        for(Employee e:staff)
            System.out.println("name="+e.getName()+" salary="+e.getSalary()+" hiraday="+e.getHireDay());
    }
}

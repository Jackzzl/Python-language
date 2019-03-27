package map;
import java.util.*;
/*
* @author zzl
* @version2018-10-24
*
* */
public class MapTest {
    public static void main(String[] args){
        Map<String,Employee>staff=new HashMap<>();
        staff.put("144-25-5664",new Employee("Amy Lee"));
        staff.put("110-25-5664",new Employee("Amy Zhao"));
        staff.put("112-25-5664",new Employee("Amy May"));
        staff.put("123-25-5664",new Employee("Amy Lay"));

        System.out.println(staff);

        staff.remove("144-25-5664");

        staff.put("456-62-5527",new Employee("Shawn zhao"));

        System.out.println(staff.get("123-25-5664"));
        staff.forEach((k,v)->System.out.println("key="+k+",value="+v));
    }
}
class Employee{
    private String name;
    public Employee(String aname){
        name=aname;
    }
}

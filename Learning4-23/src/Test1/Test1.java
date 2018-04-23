package Test1;
import java.time.*;
/*
* @version2018 4-23
* @authorzzl
*
* */
public class Test1 {
    public static void main(String[] args){
        //fill the staff array with the three Employee object
        Employee[] staff = new Employee[3];

        staff[0]=new Employee("Carl",75000,1987,12,15);
        staff[1]=new Employee("Harry",50000,1989,10,1);
        staff[2]=new Employee("Tony",40000,1990,3,15);
        for(Employee e:staff)
            e.raiseSalary(5);
        for(Employee e:staff)
            System.out.println("name="+e.getName()+",salary="+e.getSalary()+",hireday="+e.getHireDay());
    }
}
//可以构建多个非公有类
class Employee {
    private String name;
    private double salary;
    private LocalDate hireDay;
    public Employee(String n, double s, int year, int month, int day){
        name =n;
        salary = s;
        hireDay = LocalDate.of(year,month,day);
    }

    public String getName(){
        return name;
    }
    public double getSalary(){
        return salary;
    }
    public LocalDate getHireDay(){
        return hireDay;
    }

    public void raiseSalary(double byPercent){
        double raise = salary*byPercent/100;
        salary+=raise;
    }
}
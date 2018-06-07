package Test3;

import java.time.LocalDate;

/**
 * @author zzl
 * @date 2018-5-24
 */

public class Test3 {
    public static void main(String args[]){
        Employee[] staff =new Employee[3];

        staff[0]=new Employee("Carl",75000,1987,12,15);
        staff[1]=new Employee("Harry",50000,1989,1,2);
        staff[2]=new Employee("Trear",40000,1990,3,4);


        for(Employee e:staff)
            e.raiseSalary(5);
        for (Employee e:staff)
            System.out.println("name="+e.getName()+", salary="+e.getSalary()+",hireday="+e.getHireday());
    }

}
class Employee{
    private String name;
    private double salary;
    private LocalDate hireday;

    public Employee(String n,double s,int year,int month,int day){
        name =n;
        salary=s;
        hireday=LocalDate.of(year,month,day);
    }
    public String getName(){
        return name;
    }

    public double getSalary() {
        return salary;
    }
    public LocalDate getHireday(){
        return hireday;
    }
    public void raiseSalary(double byPerent){
        double raise =salary*byPerent/100;
        salary+=raise;

    }
}

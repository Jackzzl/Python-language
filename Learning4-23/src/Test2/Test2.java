package Test2;
/**
 *@version20184-23
 *@author zzl
 */

public class Test2 {
    public static void main(String[] args){
        //fill the staff array with three Employee object
        Employee[] staff = new Employee[3];

        staff[0]=new Employee("tom",40000);
        staff[1]=new Employee("Dick",60000);
        staff[2]=new Employee("Harry",50000);

        for(Employee e:staff){
            e.setId();
            System.out.println("name="+e.getName()+",id="+e.getId()+",salary="+e.getSalary());
        }
        int n =Employee.getNextId();
        System.out.println("next available id" + n);
    }
}
class Employee{
    private static int nextId =1;

    private String name;
    private double salary;
    private int id;

    public Employee(String n,double s){
        name =n;
        salary =s;
        id =0;
    }
    public String getName(){
        return name;
    }

    public double getSalary() {
        return salary;
    }

    public int getId() {
        return id;
    }

    public void setId() {
        id =nextId;
        nextId++;
        // this.id = id;
    }
    public static int getNextId(){
        return nextId;
    }
    public static void main(String[] args){
        Employee e = new Employee("harry",50000);
        System.out.println(e.getName()+" "+e.getSalary());
    }

}

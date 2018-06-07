package Test2;
/*
* @author zzl
* @data 2018 5-26
* */
public class ParamTest {
    public static void main(String args[]) {
        //text 1
        System.out.println("Testing tripleValus:");
        double percent =10;
        System.out.println("Before:percent="+percent);
        tripleValue(percent);
        System.out.println("After:percent="+percent);

        //text2
        System.out.println("\nTexting trioleSalary:");
        Employee harry=new Employee("Harry",50000);
        System.out.println("Before:salary="+harry.getSalary());
        tripleSalary(harry);
        System.out.println("After:salary="+harry.getSalary());

        //text 3
        System.out.println("\nTexting swap:");
        Employee a= new Employee("Alice",70000);
        Employee b =new Employee("Bob",60000);
        System.out.println("Before: a="+a.getName());
        System.out.println("Before: b="+b.getName());
        swap(a,b);
        System.out.println("After: a="+a.getName());
        System.out.println("After: a="+b.getName());
    }
    public static void tripleValue(double x){
        //does not work;
        x=x*3;
        System.out.println("End of method :x="+x);
    }
    public static void tripleSalary(Employee x){
        x.raiseSalary(200);
        System.out.println("End of method: salary="+x.getSalary());

    }
    public static void swap(Employee x,Employee y){
        Employee temp =x;
        x=y;
        y=temp;
        System.out.println("End of Mothed: x="+x.getName());
        System.out.println("End of Mothed: y="+y.getName());
    }
}

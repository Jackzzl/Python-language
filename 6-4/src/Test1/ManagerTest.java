package Test1;

public class ManagerTest {
    public static void main(String []args){
        Manager boss=new Manager("Gay",80000,1967,7,03);
        boss.setBonus(5000);
        Employee[] staff=new Employee[3];

        staff[0]=boss;
        staff[1]=new Employee("Sam",50000,1989,9,27);
        staff[2]=new Employee("Tom",40000,1990,3,15);
        for(Employee e:staff)
            System.out.println("name"+e.getName()+" salary "+e.getSalary());
    }
}

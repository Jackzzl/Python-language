package Test3;

import Testone.Employ;

/*
* @author zzl
* @version 2018 6-7
* */
public class EqualsTest {
    public static void main(String[] args){
        Employee alice1=new Employee("Alice",75000,1987,12,15);
        Employee alice2=alice1;
        Employee alice3=new Employee("Alice",75000,1987,12,15);
        Employee bob=new Employee("Bob",50000,1998,10,1);

        System.out.println("alice1=aclie2:"+(alice1==alice2));
        System.out.println("alice1=aclie3:"+(alice1==alice3));
        System.out.println("alice1.equals(aclie3):"+alice1.equals(alice3));
        System.out.println("alice1.equals(bob):"+alice1.equals(bob));
        System.out.println("bob.toString():"+bob);
        Manager carl=new Manager("carl",80000,1967,11,15);
        Manager boss=new Manager("carl",80000,1967,11,15);
        boss.setBonus(5000);
        System.out.println("boss.toString()"+boss);
        System.out.println("carl.equals(boss)"+carl.equals(boss));
        System.out.println("alice1.hashCode()"+alice1.hashCode());
        System.out.println("alice3.hashCode()"+alice3.hashCode());
        System.out.println("bob.hashCode()"+bob.hashCode());
        System.out.println("carl.hashCode()"+carl.hashCode());
        Manager a=new Manager("k",9000,1876,2,3);

        System.out.println(a.getClass());




    }
}

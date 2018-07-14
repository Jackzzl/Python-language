package abstractClasses;
/*
* @author zzl
* @data 2018 7-11
* */
public class PersonTest {
    public static void main(String args[]){
        Person[] people = new Person[2];

        people[0]= new Employee("Harry",5000,1989,10,1);
        people[1]=new Student("Mary","computer science");

        for(Person p:people)
            System.out.println(p.getName()+","+p.getDescription());
    }
}

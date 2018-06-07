package Testone;
/*
* @author zzl
* @version 2018 6-7
* aim to test abstractclass
* abstract类无法进行初始化自己，可以建立子类对象 接口知识
* */
public class PersonTest {
    public static void main(String[] args){
        Person[] people=new Person[2];
        people[0]=new Employ("harry",50000,1998,07,27);
        people[1]=new Student("Morris","Computer");
        for(Person p:people)
            System.out.println(p.getName()+", "+p.getDescription());
    }
}

package Test3;

import java.util.Random;

public class Employee {
    private static int nextId;
    private int id;
    private String name="";
    private double salary;

    //static initialization block
    static{
        Random generator = new Random();
        nextId=generator.nextInt(10000);
    }
    //object initialization block
    {
        id = nextId;
        nextId++;
    }
    public Employee(String n,double s){
        n=name;
        s=salary;
    }
    public Employee(double s){//调用另一个构造器
        //calls the employee(String ,double)
        this("Employee #"+nextId,s);
    }//重载构造器
    public Employee(){
        //无参数构造器
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
}

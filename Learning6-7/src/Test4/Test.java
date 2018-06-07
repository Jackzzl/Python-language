package Test4;

public class Test{
    public void Test(){
        System.out.println("This is constructor of test!");
    }
    public static void main(String args[]){
        Test t = new Test();
        Person p = t.new Person();//新建一个内部类对象
        System.out.println(t.getClass().getCanonicalName());//获取权威的类名
        System.out.println(p.getClass().getCanonicalName());
    }
    //内部类
    class Person {
        public void play(String sportName) {
            System.out.println("I'am LittleLawson,I like play" + sportName);
        }
    }
}

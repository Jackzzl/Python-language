package timer;
/*
* @author zzl
* @visition 2018 7-14
* */
import java.awt.*;
import java.awt.event.*;
import java.util.*;
import javax.swing.Timer;
import javax.swing.*;

public class TimerTest {
    public static void main(String[] args){
        ActionListener listener= new TimePrinter();
        Timer t= new Timer(10000,listener);//构造定时器，每隔时间通告listener一声
        t.start();
        JOptionPane.showConfirmDialog(null,"Quit program?");
        System.exit(0);
    }
}
class TimePrinter implements ActionListener{
    public void actionPerformed(ActionEvent event){
        System.out.println("At the tone, the time is "+ new Date());
        Toolkit.getDefaultToolkit().beep();//获取默认工具箱，发出铃声
    }
}

package noteHelloWorld;
import javax.swing.*;
import java.awt.*;
/*
* @author zzl
* @version 2018-11-27
*
* */
public class NoteHelloWorld{
    public static void main(String [] args){
        EventQueue.invokeLater(()->{
            JFrame frame =new NoteHelloWorldFrame();
            frame.setTitle("NoteHelloWorld");
            frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
            frame.setVisible(true);
        });
    }
}
class NoteHelloWorldFrame extends JFrame {
    public NoteHelloWorldFrame(){
        add(new NoteHelloWorldComponent());
        pack();
    }
}
class NoteHelloWorldComponent extends JComponent{
    public static final int MESSAGE_X=75;
    public static final int MESSAGE_Y=100;

    private static final int DEFAULT_WIDTH=300;
    private static final int DEFAULT_HEIGHT=200;

    public void paintComponent(Graphics g){
        g.drawString("Not a hello, world porgram",MESSAGE_X,MESSAGE_Y);
    }
    public Dimension getPreferredSize(){
        return new Dimension(DEFAULT_WIDTH,DEFAULT_HEIGHT);
    }
}

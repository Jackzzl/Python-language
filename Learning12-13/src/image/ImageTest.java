package image;
/*
* @author zzl
* @version 2018-12-13
*
*
* */

import java.awt.*;
import javax.swing.*;
public class ImageTest {
    public static void main(String[] agrs){
        EventQueue.invokeLater(()->{
            JFrame frame=new ImageFrame();
            frame.setTitle("ImageTest");
            frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
            frame.setVisible(true);
        });
    }
}

class ImageFrame extends JFrame{
    public ImageFrame(){
        add(new ImageComponent());
        pack();
    }

}

class ImageComponent extends JComponent{
    private static final int WIDTH=300;
    private static final int HEIGHT=200;

    private Image image;

    public ImageComponent(){
        image=new ImageIcon("Blue-ball.gif").getImage();
    }

    public void painComponent(Graphics g){
        if(image==null)return;

        int imageWidth=image.getWidth(this);
        int imageHeight=image.getHeight(this);

        g.drawImage(image,0,0,null);

        for(int i=0;i*imageWidth<=getWidth();i++)
            for(int j=0;j*imageHeight<=getHeight();j++)
                if(i+j>0)
                    g.copyArea(0,0,imageWidth,imageHeight,i*imageWidth,j*imageHeight);
    }

    public Dimension getPreferredSize(){
        return new Dimension(WIDTH,HEIGHT);
    }
}

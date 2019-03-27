package button;
import java.awt.*;
import javax.swing.*;
import java.awt.event.*;

public class ButtonFrame extends JFrame {
    private JPanel buttonPanel;
    private static final int WIDTH=300;
    private static final int HEIGHT=200;
    public ButtonFrame(){
        setSize(WIDTH,HEIGHT);

        JButton yellowButton = new JButton("Yellow");
        JButton blueButton = new JButton("Blue");
        JButton redButton = new JButton("Red");

        buttonPanel =new JPanel();

        buttonPanel.add(yellowButton);
        buttonPanel.add(blueButton);
        buttonPanel.add(redButton);

        add(buttonPanel);

        ColorAction yellowAction =new ColorAction(Color.YELLOW);
        ColorAction blueAction = new ColorAction(Color.BLUE);
        ColorAction redAction= new ColorAction(Color.red);

        yellowButton.addActionListener(yellowAction);
        blueButton.addActionListener(blueAction);
        redButton.addActionListener(redAction);
    }

    private class ColorAction implements ActionListener{
        private Color backgroundColor;

        public ColorAction(Color c){
            backgroundColor=c;
        }
        public void actionPerformed(ActionEvent event){
            buttonPanel.setBackground(backgroundColor);
        }
    }


}

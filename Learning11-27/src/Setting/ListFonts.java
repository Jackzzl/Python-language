package Setting;
import java.awt.*;
/*
* @author zzl
* @version 2018-11-27
* */
public class ListFonts {
    public static void main(String[] args){
        String[] fontNames=GraphicsEnvironment.getLocalGraphicsEnvironment().getAvailableFontFamilyNames();
        for(String fontName : fontNames)
            System.out.println(fontName);
    }
}

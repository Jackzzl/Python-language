package view.menu;

import java.awt.BorderLayout;
import java.awt.CardLayout;
import java.awt.Dimension;
import java.awt.FlowLayout;
import java.awt.GridLayout;
import java.awt.Toolkit;
import java.awt.event.MouseEvent;
import java.awt.event.MouseListener;
import java.util.ArrayList;

import javax.swing.BorderFactory;
import javax.swing.DefaultListModel;
import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JList;
import javax.swing.JOptionPane;
import javax.swing.JPanel;
import javax.swing.JScrollPane;
import javax.swing.JTextArea;
import javax.swing.JTextField;

import data.DataDealer;
import data.Result;
import style.font.FontClass;

public class MenuFrame extends JFrame implements MouseListener{
	/**
	 * 
	 */
	private static final long serialVersionUID = 1L;
	private static final int DEFAULT_WIDTH = 800;
	private static final int DEFAULT_HEIGHT = 600;
	private JButton jb_rule_save,jb_face,jb_data,jb_input_sub,jb_feature_sub,jb_rule_add,jb_rule_delete,jb_rule_update;
	private JPanel jp_header,jp_body,jp_face,jp_input,jp_output
	,jp_data,jp_data_input;
	private JScrollPane jsp_list,jsp_rule, jsp_truth;
	private JLabel jlb_num,jlb_feature,jlb_output;
	private JTextField jtf_num, jtf_feature;
	private JList<String> jlst_feature, jlst_rule;
	private CardLayout card;
	private int feature_num,cur_feature = 0;
	private DefaultListModel<String> dlm_feature, dlm_rule;
	private static DataDealer dd;
	private static JTextArea jta_result, jta_truth;
	public MenuFrame(){
		FontClass.loadIndyFont();
		setSize(DEFAULT_WIDTH, DEFAULT_HEIGHT);//长宽
		appearCenter();//居中显示
		setTitle("实验一：");
		setResizable(false);
		setLayout(new BorderLayout());
		feature_num = 0;
		jb_face = new JButton("首页");
		jb_face.addMouseListener(this);
		jb_face.setEnabled(false);
		jb_data = new JButton("数据库");
		jb_data.addMouseListener(this);
		jp_header = new JPanel();//头部
		jp_body = new JPanel();//身体
//		JLabel test = new JLabel("test");
//		jp_header.add(test);
		jp_header.add(jb_face);
		jp_header.add(jb_data);
		card = new CardLayout();
		jp_body.setLayout(card);
		jp_face = new JPanel();//第一页卡片
		jp_face.setLayout(new BorderLayout());
		jp_input = new JPanel();//输入容器
		jp_input.setLayout(new GridLayout(2, 3));
		jp_output = new JPanel();//输出容器
		jp_data = new JPanel();//第二页卡片
		jtf_num = new JTextField(10);
		//输入约束条件的数目
		jlb_num = new JLabel("请输入动物特征的数目：");
		jb_input_sub = new JButton("提交");
		jb_input_sub.addMouseListener(this);
		//输入并显示相应的特征
		dlm_feature = new DefaultListModel<String>();
		dlm_rule = new DefaultListModel<String>();
		jlst_feature = new JList<String>(dlm_feature);
		jlst_rule = new JList<String>(dlm_rule);
		jlst_feature.setBorder(BorderFactory.createTitledBorder("包含以下特征"));
		jtf_feature = new JTextField(10);
		jtf_feature.setEditable(false);
		jlb_feature = new JLabel("请输入特征：");
		jb_feature_sub = new JButton("提交");
		jb_feature_sub.addMouseListener(this);
		jp_input.add(jlb_num);
		jp_input.add(jtf_num);
		jp_input.add(jb_input_sub);
		jp_input.add(jlb_feature);
		jp_input.add(jtf_feature);
		jp_input.add(jb_feature_sub);
		jb_feature_sub.setEnabled(false);
		//添加jlist
		jsp_list = new JScrollPane();
		jsp_list.setViewportView(jlst_feature);
		//制作输出Panel
		jlb_output = new JLabel("结果及过程：");
		jta_result = new JTextArea();
		jta_result.setPreferredSize(new Dimension(800, 300));
		jta_result.setEditable(false);
		jp_output.setLayout(new FlowLayout(FlowLayout.LEFT));
		jp_output.add(jlb_output);
		jp_output.add(jta_result);
		jp_face.add(jp_input,BorderLayout.NORTH);
		jp_face.add(jsp_list,BorderLayout.CENTER);
		jp_face.add(jp_output,BorderLayout.SOUTH);
		//数据库页面
		jp_data.setLayout(new BorderLayout());
		jta_truth = new JTextArea();
		jsp_rule = new JScrollPane();
		jsp_truth = new JScrollPane();
		jsp_truth.setViewportView(jta_truth);
		jsp_rule.setPreferredSize(new Dimension(0,230));
		jta_truth.setEditable(false);
		jlst_rule.setBorder(BorderFactory.createTitledBorder("规则数据库"));
		jsp_rule.setViewportView(jlst_rule);
		jta_truth.setBorder(BorderFactory.createTitledBorder("综合数据库"));
		jp_data_input = new JPanel();
		//对规则数据库的增删改
		jb_rule_add = new JButton("增加规则");
		jb_rule_delete = new JButton("删除规则");
		jb_rule_update = new JButton("修改规则");
		jb_rule_save = new JButton("保存规则");
		jb_rule_add.addMouseListener(this);
		jb_rule_delete.addMouseListener(this);
		jb_rule_update.addMouseListener(this);
		jb_rule_save.addMouseListener(this);
		jp_data_input.add(jb_rule_add);
		jp_data_input.add(jb_rule_delete);
		jp_data_input.add(jb_rule_update);
		jp_data_input.add(jb_rule_save);
		jp_data.add(jp_data_input,BorderLayout.NORTH);
		jp_data.add(jsp_truth,BorderLayout.CENTER);
		jp_data.add(jsp_rule,BorderLayout.SOUTH);
		jp_body.add(jp_face);
		jp_body.add(jp_data);
		dd = new DataDealer();
		this.add(jp_header,BorderLayout.NORTH);
		this.add(jp_body,BorderLayout.CENTER);
		flush();
	}
	private void appearCenter() {
		// TODO Auto-generated method stub
		int windowWidth = this.getWidth();                    //获得窗口宽
        int windowHeight = this.getHeight();                  //获得窗口高
        Toolkit kit = Toolkit.getDefaultToolkit();             //定义工具包
        Dimension screenSize = kit.getScreenSize();            //获取屏幕的尺寸
        int screenWidth = screenSize.width;                    //获取屏幕的宽
        int screenHeight = screenSize.height;                  //获取屏幕的高
        this.setLocation(screenWidth/2-windowWidth/2, 
        		screenHeight/2-windowHeight/2);//设置窗口居中显示
	}
	public static void writeResult(String s){
		jta_result.setText(jta_result.getText()+s+"\n");
	}
	public static void flush_truth(){
		jta_truth.setText("");
		for(int i = 0; i < dd.db.truth.size(); i++){
			jta_truth.setText(jta_truth.getText()+dd.db.truth.get(i).result
					+"\n");
		}
	}
	@Override
	public void mouseClicked(MouseEvent e) {
		// TODO Auto-generated method stub
		if(e.getSource()==jb_face && jb_face.isEnabled()){
			jb_face.setEnabled(false);
			jb_data.setEnabled(true);
			//显示第一张card
			card.first(jp_body);
		}else if(e.getSource()==jb_data && jb_data.isEnabled()){
			jb_data.setEnabled(false);
			jb_face.setEnabled(true);
			//显示第二张卡片
			flush_truth();
			card.last(jp_body);
		}else if(e.getSource()==jb_input_sub&&jb_input_sub.isEnabled()){
			String cont = jtf_num.getText();
			try{
				feature_num = Integer.parseInt(cont);
			}catch(Exception e1){
				JOptionPane.showMessageDialog(null, "请输入数字！");
				jtf_num.selectAll();
				return;
			}
			if(feature_num<=0){
				JOptionPane.showMessageDialog(null, "请输入合法数字！");
				return;
			}
			jtf_num.setEditable(false);
			jb_input_sub.setEnabled(false);
			jtf_feature.setEditable(true);
			jb_feature_sub.setEnabled(true);
		}else if(e.getSource()==jb_feature_sub && jb_feature_sub.isEnabled()){
			if(jtf_feature.getText().equals("")&&cur_feature<feature_num){
				JOptionPane.showMessageDialog(null, "输入不可为空！");
				jtf_feature.requestFocus();
				return;
			}
			cur_feature++;
			if(cur_feature>feature_num){
				jb_feature_sub.setEnabled(false);
				//然后开始进行运算
				ArrayList<String> arr = new ArrayList<String>();
				for(int i = 0; i < feature_num; i++){
					dd.addRule(dlm_feature.getElementAt(i).split("\\.")[1]);
					arr.add(dlm_feature.getElementAt(i).split("\\.")[1]);
				}
				//只在这里循环，直到求出最终解或者失败退出
				while(true){
					Result r = dd.run(arr);
					if(r==null){//要求用户补充事实
						int opt = JOptionPane.showConfirmDialog(null, "还可以补充事实吗？", "现有事实不足！",JOptionPane.YES_NO_OPTION);
						if(opt==0){//还能添加
							int t = Integer.parseInt(JOptionPane.showInputDialog("新增加的特征数目为？"));
							for(int i = 0; i < t; i++){
								String tmp = JOptionPane.showInputDialog("请输入第"+(i+1)+"条新增特征");
								writeResult("新增特征："+tmp);
								dd.addRule(tmp);
								arr.add(tmp);
							}
						}else{
							JOptionPane.showMessageDialog(null, "失败退出！");
							break;
						}
					}else{//找到答案
						JOptionPane.showMessageDialog(null, "我day到了！"+r.result);
						break;
					}
				}
			}else{
				dlm_feature.addElement("#"+cur_feature+"."+jtf_feature.getText());
				jtf_feature.setText("");
				jtf_feature.requestFocus();
			}
			if(cur_feature==feature_num){
				jb_feature_sub.setText("开始推理");
				jtf_feature.setEditable(false);
			}
		}else if(e.getSource()==jb_rule_add){//默认输入符合规范
			String[] pre = JOptionPane.showInputDialog("请输入新增规则的前件，用空格隔开").split(" ");
			String res = JOptionPane.showInputDialog("请输入新增规则的结论");
			Result r = new Result(res);
			for(int i = 0; i < pre.length; i++){
				r.pre.add(pre[i]);
			}
			dd.addRule(r);
			flush();
		}else if(e.getSource()==jb_rule_save){
			dd.save();
		}else if(e.getSource()==jb_rule_delete&&jlst_rule.getSelectedIndex()!=-1){
			int idx = jlst_rule.getSelectedIndex();
			JOptionPane.showMessageDialog(null, "删除成功！");
			dd.db.rb.removeRule(idx);
			flush();
		}else if(e.getSource()==jb_rule_update&&jlst_rule.getSelectedIndex()!=-1){
			int idx = jlst_rule.getSelectedIndex();
			String tmp_pre="";
			for(int i = 0; i < dd.db.rb.rule.get(idx).pre.size(); i++){
				tmp_pre += dd.db.rb.rule.get(idx).pre.get(i)+" ";
			}
			String[] pre = JOptionPane.showInputDialog("请输入修改规则的前件，用空格隔开",tmp_pre).split(" ");
			String res = JOptionPane.showInputDialog("请输入修改规则的结论",dd.db.rb.rule.get(idx).result);
			Result r = new Result(res);
			for(int i = 0; i < pre.length; i++){
				r.pre.add(pre[i]);
			}
			dd.db.rb.removeRule(idx);
			dd.db.rb.addRule(r);
			flush();
		}
	}
	private void flush() {
		// TODO Auto-generated method stub
		dlm_rule.removeAllElements();
		for(Result r:dd.db.rb.rule){
			StringBuilder tmp=new StringBuilder("IF:");
			tmp.append(r.pre.get(0));
			for(int i = 1; i < r.pre.size(); i++){
				tmp.append(" AND "+r.pre.get(i));
			}
			tmp.append(" THEN:"+r.result);
			dlm_rule.addElement(tmp.toString());
		}
	}
	@Override
	public void mousePressed(MouseEvent e) {
		// TODO Auto-generated method stub
		
	}
	@Override
	public void mouseReleased(MouseEvent e) {
		// TODO Auto-generated method stub
		
	}
	@Override
	public void mouseEntered(MouseEvent e) {
		// TODO Auto-generated method stub
		
	}
	@Override
	public void mouseExited(MouseEvent e) {
		// TODO Auto-generated method stub
		
	}
}

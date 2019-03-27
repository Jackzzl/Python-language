package data;

import java.io.Serializable;
import java.util.ArrayList;

import view.menu.MenuFrame;

public class DataBase implements Serializable{

	/**
	 * 
	 */
	private static final long serialVersionUID = 1L;
	public ArrayList<Result> truth;//事实
	public RuleBase rb;
	public DataBase(){
		truth = new ArrayList<Result>();
		rb = new RuleBase();
	}
	//增加新的事实
	public void addElement(Result r){
		truth.add(r);
	}
	//删除事实
	public void removeElement(int index){
		truth.remove(index);
	}
	//获取所有事实（用于显示）
	public ArrayList<String> getElements(){
		ArrayList<String> tmp = new ArrayList<String>();
		for(Result r:truth){
			tmp.add(r.result);
		}
		return tmp;
	}
	/**
	 * 从知识库中获取新的知识
	 */
	public boolean search(){
		boolean flag = false;
		if(rb.isEmpty()){
			return false;//知识库为空
		}
		ArrayList<Result> tmp = rb.getNewResult(truth);//默认这些都是定义良好的result
		for(Result r:tmp){
			if(!truth.contains(r)){
				Result rr = null;
				for(Result rrr:rb.rule)
					if(rrr.equals(r))
						rr = rrr;
				String pre = rr.pre.get(0);
				for(int i = 1; i < rr.pre.size(); i++){
					pre+="、"+rr.pre.get(i);
				}
				MenuFrame.writeResult("由前提："+pre+"，从而新增事实："+rr.result);
				truth.add(r);
				flag = true;
			}
		}
		return flag;
	}
	public Result match(ArrayList<String> question){
		for(Result r:truth){
			if(r.isAnswer(question)){
				return r;
			}
		}
		return null;
	}
}

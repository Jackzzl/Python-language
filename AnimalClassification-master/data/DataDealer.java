package data;

import java.util.ArrayList;

import view.menu.MenuFrame;

public class DataDealer {
	ArrayList<String> init;
	public DataBase db;
	public DataDealer(){
		load();
	}
	public Result run(ArrayList<String> init){
		while(true){
			Result r = db.match(init);//是要求匹配所有特征！所以不能出现错的特征！
			if(r!=null){
				MenuFrame.writeResult("找到结果了！结论为："+r.result);
				return r;
			}else{
				MenuFrame.writeResult("综合数据库中尚没有解，调用知识数据库...");
				if(!db.search()){
					MenuFrame.writeResult("知识库中没有可用知识！");
					return null;
				}
			}
		}
	}
	public void addRule(String s){
		Result r = new Result(s);
		db.addElement(r);
	}
	/**
	 * 这个addRule是用来增加到rulebase的
	 * @param r
	 */
	public void addRule(Result r){
		db.rb.addRule(r);
	}
	public void save() {
		// TODO Auto-generated method stub
		try{
			RuleBase.save(db.rb);
		}catch(Exception e){
			e.printStackTrace();
		}
	}
	private void load() {
		// TODO Auto-generated method stub
		db = new DataBase();
		try{
			db.rb = RuleBase.load();//尝试性的读取一下
		}catch(Exception e){
			db = new DataBase();
			e.printStackTrace();
		}
	}
	
}

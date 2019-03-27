package data;

import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.ObjectInputStream;
import java.io.ObjectOutputStream;
import java.io.Serializable;
import java.util.ArrayList;

public class RuleBase implements Serializable{

	/**
	 * 
	 */
	private static final long serialVersionUID = 1L;
	public ArrayList<Result> rule;
	private int cnt;
	public RuleBase(){
		rule = new ArrayList<Result>();
	}
	public void addRule(Result r){
		rule.add(r);
		cnt++;
	}
	public void removeRule(int index){
		rule.remove(index);
		cnt--;
	}
	public ArrayList<Result> getNewResult(ArrayList<Result> truth){
		ArrayList<Result> tmp = new ArrayList<Result>();
		for(Result r: rule){
			boolean flag = true;
			for(String s:r.pre){
//				for(Result rr:truth){
//					if(rr.result.equals(anObject))
//				}
				if(!truth.contains(new Result(s))){
					flag = false;
					break;
				}
			}
			if(flag){
				tmp.add(trans(truth,r));
			}
		}
//		for(Result r:truth){
//			ArrayList<Result> tt = match(r);
//			cnt-=tt.size();
//			if(tt.size()>0){
//				for(Result rr:tt){
//					tmp.add(trans(r,rr));
//				}
//			}
//		}
		return tmp;
	}
	/**
	 * 将前件的所有前件都添加至中间结论的前件中去
	 * @param pre
	 * @param res
	 * @return
	 */
	private Result trans(ArrayList<Result> truth, Result res) {
		// TODO Auto-generated method stub
		Result re = new Result(res.result);
		for(int i = 0; i < res.pre.size(); i++){
			re.pre.add(res.pre.get(i));
		}
		for(Result r:truth){
			if(re.pre.contains(r.result)){
				for(String s:r.pre){//把前件的所有前件都加入到res的前件中去
					if(!re.pre.contains(s))
						re.pre.add(s);
				}
			}
		}
		return re;
	}
	/**
	 * 判断rule数组中是否包含可以匹配pre的条件，若有则返回该result
	 * @param r
	 * @return
	 */
//	private ArrayList<Result> match(Result pre) {
//		// TODO Auto-generated method stub
//		ArrayList<Result> tmp = new ArrayList<Result>();
//		for(Result r:rule){
//			boolean flag = true;
//			for(String s:r.pre){
//				if(!(pre.pre.contains(s)||pre.result.equals(s))){
//					flag = false;//当前r的前件不满足break;
//				}
//			}
//			if(flag){
//				tmp.add(r);
//			}
//		}
//		return tmp;
//	}
	public boolean isEmpty(){
		return cnt<=0;
	}
	/**
	 * 必须先存档才能读档，不然会报错
	 * @param db
	 * @throws IOException
	 */
	public static void save(RuleBase db) throws IOException{
		System.out.println("Saving as serializable in RuleBase.txt...");
		FileOutputStream foo = new FileOutputStream("RuleBase.txt");
		ObjectOutputStream oos = new ObjectOutputStream(foo);
		oos.writeObject(db);
		oos.flush();
		oos.close();
		System.out.println("Successfully saving!");
	}
	public static RuleBase load() throws IOException, ClassNotFoundException{
		FileInputStream fin = new FileInputStream("RuleBase.txt");
		ObjectInputStream oin = new ObjectInputStream(fin);
		RuleBase tmp = (RuleBase)oin.readObject();
		oin.close();
		return tmp;
	}
}

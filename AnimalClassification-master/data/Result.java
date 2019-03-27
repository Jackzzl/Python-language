package data;

import java.io.Serializable;
import java.util.ArrayList;

public class Result implements Serializable{//封装性差就差了，随便来
	/**
	 * 
	 */
	private static final long serialVersionUID = 1L;
	public ArrayList<String> pre;
	public String result;
	public Result(String r){
		pre = new ArrayList<String>();
		result = r;
	}
	public boolean isAnswer(ArrayList<String> question){
		if(pre.size()==0)
			return false;
		for(String s:question){
			if(!pre.contains(s))
				return false;
		}
		return true;
	}
	@Override
	public boolean equals(Object o){
		Result tmp = (Result)o;
		return this.result.equals(tmp.result);
	}
}

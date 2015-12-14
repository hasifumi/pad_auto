package com.hahahassy.android;

import java.util.StringTokenizer;

import com.android.uiautomator.testrunner.UiAutomatorTestCase;

import android.graphics.Point;
import android.os.Bundle;

public class UiAutomator extends UiAutomatorTestCase {
	public void swipe(){
	    Bundle args = this.getParams();
	    String x_str = args.getString("x");
	    String y_str = args.getString("y");
	    String t_str = args.getString("t");
	    int t = Integer.parseInt(t_str);
	    StringTokenizer x = new StringTokenizer(x_str, ",");
	    StringTokenizer y = new StringTokenizer(y_str, ",");
	    assertTrue(x.countTokens() == y.countTokens());
	    Point[] point = new Point[x.countTokens()];
	    int i = 0;
	    while(x.hasMoreTokens()){
	        point[i] = new Point(
	            Integer.parseInt(x.nextToken()), Integer.parseInt(y.nextToken()));
	        i++;
	    }
	    getUiDevice().swipe(point, t);
	}

}

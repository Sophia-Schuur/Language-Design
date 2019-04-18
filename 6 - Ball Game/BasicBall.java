/******************************************************************************
 *  Compilation:  javac ColoredBall.java
 *  Execution:    java ColoredBall
 *  Dependencies: StdDraw.java
 *
 *  Implementation of a 2-d ball moving in square with coordinates
 *  between -1 and +1.
 *  
 *
 ******************************************************************************/

import java.awt.Color;

public class BasicBall { 
    protected double rx, ry;     // position
    protected double vx, vy;     // velocity
    protected double radius;        
    protected Color color;          
    public boolean isOut;
    public String type;
    protected int score;
    

    // Constructor
    public BasicBall(double r) {
        rx = 0.0;
        ry = 0.0;
        vx = StdRandom.uniform(-0.01, 0.01);
        vy = StdRandom.uniform(-0.01, 0.01);
        radius = r;
        color = Color.RED;
        isOut = false;
        type = "BasicBall";
        score = 25;
    }
   
    public String GetType() { return this.type; }
    public int GetScore() { return this.score; }
    public double GetRadius() { return this.radius; }
   
    // Move the ball one step
    public void Move() {
        rx = rx + vx;
        ry = ry + vy;
        if ((Math.abs(rx) > 1.0) || (Math.abs(ry) > 1.0)) 
        	isOut = true;
    }

    // Draw the ball   
    public void Draw() { 
        // There is no need to recheck this when you already check in Move(). 
        // It also breaks BounceBall because we Draw() AFTER we Move(). 
    	// if ((Math.abs(rx) <= 1.0) && (Math.abs(ry) <= 1.0)) {
    		StdDraw.setPenColor(color);
    		StdDraw.filledCircle(rx, ry, radius);
    	// } else
    	// 	isOut = true;
    	
    }

    // Position ball back to center and randomize velocity
    public int Reset() {
        rx = 0.0;
        ry = 0.0;  	
        vx = StdRandom.uniform(-0.01, 0.01);
        vy = StdRandom.uniform(-0.01, 0.01);
        return 1;
    }
    
    // Check if ball is clicked on
    public boolean IsHit(double x, double y) {
    	if ((Math.abs(rx-x)<=radius) && (Math.abs(ry-y)<=radius))
			return true;
		else return false; 

    }
}

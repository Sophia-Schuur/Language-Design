/******************************************************************************
 *  SplitBallwill split into 2 unique balls every time the ball is hit. The 
    2 split-balls will always appear at the center of the game window and they 
    will have the same radius as the original ball. Their initial speeds will 
    be randomly assigned. 

    Each ball generated in a split is itself a split-ball and can be split 
    further when hit with a mouse click. 

    A hit to a split ball will increase the player’s score by 10 points
 *  
 *
 ******************************************************************************/

import java.awt.Color;

public class SplitBall extends BasicBall 
{ 
    private int bounces;

    // Constructor
    public SplitBall(double r) {
        super(r);
        rx = 0.0;
        ry = 0.0;
        vx = StdRandom.uniform(-0.01, 0.01);
        vy = StdRandom.uniform(-0.01, 0.01);
        bounces = 0;
        radius = r;
        color = Color.BLUE;
        isOut = false;
        type = "SplitBall";
        score = 10;
    }
    
    // Return 2 instead of 1. Will reset as normal and BallGame.java will span a new SplitBall.
    @Override
    public int Reset() {
        rx = 0.0;
        ry = 0.0;   
        vx = StdRandom.uniform(-0.01, 0.01);
        vy = StdRandom.uniform(-0.01, 0.01);
        return 2;
    }
}
    


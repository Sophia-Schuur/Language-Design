/******************************************************************************
 *  This is a larger ball which gets smaller by 33% (i.e., 2/3 of the original size) 
    each time the player hits it. Similar to BasicBall, after each hit, the ball 
    will be moved to its initial location and it will be assigned a random speed. 

    When the ball size is less than or equal to 25% of the initial size the ball, 
    the ball will be reset to its original size and it will start from the middle of the 
    screen with a random initial speed. 

    A hit to a shrink ball will increase the player’s score by 20 points.
 *  
 *
 ******************************************************************************/

import java.awt.Color;

public class ShrinkBall extends BasicBall 
{ 
    private double originalRadius;

    // Constructor
    public ShrinkBall(double r) {
        super(r);
        rx = 0.0;
        ry = 0.0;
        vx = StdRandom.uniform(-0.01, 0.01);
        vy = StdRandom.uniform(-0.01, 0.01);
        originalRadius = r;
        radius = r;
        color = Color.MAGENTA;
        isOut = false;
        type = "ShrinkBall";
        score = 20;
    }

    @Override
    public int Reset()
    {   // When radius is halved, the ball is 25% its original size.
        if(radius <= 0.5*originalRadius) // So use .5 NOT .25
        {
            radius = originalRadius; 
        }
        // Otherwise, the ball becomes 33% smaller (multiplied by 5/6)
        else
        {
            radius = radius * 0.8333; 
        }
        return super.Reset();
    }
}

/******************************************************************************
 *  BounceBall will bounce on the borders of the scene but it will be out 
    after it bounces for a certain number of times. (The bounce count will be 3 
    for all bounce balls.) The ball should maintain the magnitude of its speed 
    in each bounce. 

    The direction (sign) of the speed will change due to the bounce. The other 
    ball types won’t bounce on borders. After bouncing 3 times, the bounce ball 
    will disappear out of the game window.

    Similar to other balls, after each hit, the ball will be moved to its initial 
    location and it willbe assigned a random speed.

    A hit to a bounce ball will increase the player’s score by 15 points.
 *  
 *
 ******************************************************************************/

import java.awt.Color;

public class BounceBall extends BasicBall 
{ 
    private int bounces;

    // Constructor
    public BounceBall(double r) {
        super(r);
        rx = 0.0;
        ry = 0.0;
        vx = StdRandom.uniform(-0.01, 0.01);
        vy = StdRandom.uniform(-0.01, 0.01);
        bounces = 0;
        radius = r;
        color = Color.YELLOW;
        isOut = false;
        type = "BounceBall";
        score = 15;
    }

    @Override
    public void Move() {
        rx = rx + vx;
        ry = ry + vy;
        if ((Math.abs(rx) > 1.0) || (Math.abs(ry) > 1.0)) // Radius outside the screen?
        {
            if (bounces < 3) // Over 3 bounces?
            {
                if (Math.abs(rx) > 1.0) // Too far left or right?
                {
                    vx = vx * -1.0;
                }
                else if (Math.abs(ry) > 1.0)   // Too far top or bottom?
                {
                    vy = vy * -1.0;
                }
                bounces++;  
            }
            else // Out of bounces and outside the screen? Ball be gone!
            {
                isOut = true;
            }
        }
    }
    
}

/******************************************************************************
 *  Sophia Schuur
 *  4/18/2019
 *  Windows intended

 *  Simple java game. Click on balls to earn points before they leave the screen.
 *  Arguments passed through command line. 
 *  For example: (java BallGame) 4 basic 0.10 bounce 0.05 shrink 0.13 split 0.05


 *  Compilation:  javac BallGame.java
 *  Execution:    java BallGame n
 *  Dependencies: BasicBall.java StdDraw.java
 *
 *  Part of the animation code is adapted from Computer Science: An Interdisciplinary Approach Book
 *
 *******************************************************************************/
import java.awt.Color;
import java.awt.Font;
import java.util.*;

public class BallGame { 

    public static void main(String[] args) {
        
        // Get inputs from user (command line)
    	int numBalls = Integer.parseInt(args[0]);
    	String ballTypes[] = new String[numBalls];
    	double ballSizes[] = new double[numBalls];
    	
    	//retrieve ball types
    	int index =1;
    	for (int i=0; i<numBalls; i++) {
    		ballTypes[i] = args[index];
    		index = index+2;
    	}
    	//retrieve ball sizes
    	index = 2;
    	for (int i=0; i<numBalls; i++) {
    		ballSizes[i] = Double.parseDouble(args[index]);
    		index = index+2;
    	}
       
        Player player = new Player();

        // Dictionary for tracking most hit balls
    	HashMap<String, Integer> mostHit = new HashMap<String, Integer>();
        mostHit.put("BasicBall", 0);
        mostHit.put("ShrinkBall", 0);
        mostHit.put("BounceBall", 0);
        mostHit.put("SplitBall", 0);

    	int numBallsinGame = 0;
        BallFactory factory = new BallFactory();
        ArrayList<BasicBall> balls = new ArrayList<BasicBall>(numBalls);

        StdDraw.enableDoubleBuffering();
        StdDraw.setCanvasSize(800, 800);
        // set boundary to box with coordinates between -1 and +1
        StdDraw.setXscale(-1.0, +1.0);
        StdDraw.setYscale(-1.0, +1.0);  
        StdDraw.enableDoubleBuffering();      

        for (int i = 0; i < numBalls; i++)
        {
            balls.add(factory.GetBall(ballTypes[i], ballSizes[i]));
            numBallsinGame++;
        }
        
        while (numBallsinGame > 0) {

            // Move each ball across screen
            for (var ball : balls)
            {
                ball.Move(); 
            }

            // Check if mouse is clicked
            if (StdDraw.isMousePressed()) {
                double x = StdDraw.mouseX();
                double y = StdDraw.mouseY();

                // Check whether a ball is hit OUCH
                for (int i = 0; i < balls.size(); i++)
                {
                    if (balls.get(i).IsHit(x,y)) {

                            // Splitball? -> Need to add to our list of sweet balls
                        	int resetFlag = balls.get(i).Reset();
                            if (resetFlag == 2)
                            {
                                balls.add(new SplitBall(balls.get(i).GetRadius()));
                            }
                            player.AddTotalHits();
                            player.UpdateScore(balls.get(i).GetScore());
                            
                            // +1 to corresponding ball type <string, int>
                            mostHit.put(balls.get(i).GetType(), mostHit.get(balls.get(i).GetType()) + 1);
                            int mostHits = Collections.max(mostHit.values());

                            // Check for max type hit and set it
                            for (var item : mostHit.entrySet())
                            {
                                if (item.getValue() == mostHits)
                                { 
                                    player.SetMostHitBall(item.getKey()); 
                                    break;
                                }
                            }
                    }
                }
            }
            
            numBallsinGame = 0;
    
            // Draw sum background or whatnot
            StdDraw.clear(StdDraw.BLACK);
            StdDraw.setPenColor(StdDraw.WHITE); // what does this even do
              
            for (var ball : balls)
            {
                if (ball.isOut == false) { 
                    ball.Draw();
                    numBallsinGame++;
                }
            }
            // Print the game progress
            StdDraw.setPenColor(StdDraw.YELLOW);
            Font font = new Font("Arial", Font.BOLD, 20);
            StdDraw.setFont(font);
            
            // Print player stats
            StdDraw.text(-0.65, 0.90, "Total balls: "+ String.valueOf(numBallsinGame));           
            StdDraw.text(-0.65, 0.80, "Total Hits: "+ String.valueOf(player.GetHits()));
            StdDraw.text(-0.65, 0.70, "Score: "+ String.valueOf(player.GetScore()));
            StdDraw.text(-0.65, 0.60, "Most Hit Ball: "+ player.GetMostHitBall());
            
            StdDraw.show();
            StdDraw.pause(20);
        }
        
        // End game
        StdDraw.clear();
        StdDraw.clear(StdDraw.GRAY);
        StdDraw.setPenColor(StdDraw.BLACK);
        while (true) {
            StdDraw.setPenColor(StdDraw.BLACK);
            Font font = new Font("Arial", Font.BOLD, 60);
            StdDraw.setFont(font);
            StdDraw.text(0, .4, "YA RAN OUTTA BALLZ");

            //StdDraw.text(0, .15, "Total ballZ: "+ String.valueOf(numBallsinGame));           
            StdDraw.text(0, 0, "Total Hits: "+ String.valueOf(player.GetHits()));
            StdDraw.text(0, -.15, "Score: "+ String.valueOf(player.GetScore()));
            if (player.GetMostHitBall().equals(""))
                StdDraw.text(0, -.3, "You didn't even get one.");          
            else
                StdDraw.text(0, -.3, "Most Hit Ball: "+ player.GetMostHitBall());
            
            StdDraw.show();
            StdDraw.pause(10);           
        }
        	
        
    }
}

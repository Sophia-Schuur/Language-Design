
import java.awt.Color;

public class BallFactory { 
    
    //public BallFactory() {}

    // Return balltype based on input string
    public BasicBall GetBall(String ballType, double r)
    {
        if (ballType.equals("basic"))
        {
            return new BasicBall(r);
        }
        else if (ballType.equals("shrink"))
        {
            return new ShrinkBall(r);
        }
        else if (ballType.equals("bounce"))
        {
            return new BounceBall(r);
        }
        else if (ballType.equals("split"))
        {
            return new SplitBall(r);
        }
        return null;
    }
}

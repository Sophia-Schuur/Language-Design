public class Player { 
    
    //Points: basic →25; shrink→20; bounce →15; split →10).
    private int totalHits;
    private int score;
    private String mostHitBall;

    //Constructor
    public Player() 
    {
        totalHits = 0;
        score = 0;
        mostHitBall = "";
    }

    //getters n setters
    public int GetHits() { return this.totalHits; }
    public void SetHits(int totalHits) { this.totalHits = totalHits; }

    public int GetScore() { return this.score; }
    public void SetScore(int score) { this.score = score; }

    public String GetMostHitBall() { return this.mostHitBall; }
    public void SetMostHitBall(String mostHitBall) { this.mostHitBall = mostHitBall; }

    //public methods
    public void UpdateScore(int score)
    {
        this.score = this.score + score;
    }

    public void AddTotalHits()
    {
        totalHits++;
    }

    
    
}

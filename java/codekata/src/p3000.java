import java.util.HashMap;
import java.util.Scanner;

class Point {
    int x,y;
    Point(int x, int y) {
        this.x = x;
        this.y = y;
    }
}

class TriangleCounter {
    private final Point[] points;
    private final HashMap<Integer, Integer> cntX= new HashMap<>();
    private final HashMap<Integer, Integer> cntY= new HashMap<>();

    public TriangleCounter(Point[] points) {
        this.points=points;
        for (Point p : points){
            cntX.put(p.x, cntX.getOrDefault(p.x,0)+1);
            cntY.put(p.y, cntY.getOrDefault(p.y,0)+1);
        }
    }

    public long count(){
        long r = 0;
        for (Point p : points) {
            r += (long)(cntX.get(p.x)-1)*(long)(cntY.get(p.y)-1);
        }
        return r;
    }
}

public class p3000 {
    public static void main(String[] args) {
        Point[] points;
        try (Scanner scanner = new Scanner(System.in)) {
            int n = scanner.nextInt();
            points = new Point[n];
            for (int i=0;i<n;i++){
                int x=scanner.nextInt();
                int y=scanner.nextInt();
                points[i] = new Point(x,y);
            }
        }

        TriangleCounter tcounter = new TriangleCounter(points);
        System.out.println(tcounter.count());
    }
}
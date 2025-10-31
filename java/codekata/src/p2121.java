
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;
import java.util.Objects;
import java.util.StringTokenizer;

class Point {
    int x,y;
    Point(int x, int y){
        this.x = x;
        this.y = y;
    }

    @Override
    public boolean equals(Object o){
        if (this == o) return true;
        if (!(o instanceof Point)) return false;
        Point p = (Point) o;
        return x == p.x && y == p.y;
    }

    @Override
    public int hashCode(){
        return Objects.hash(x,y);
    }
}

public class p2121 {
    public static void main() throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());
        st = new StringTokenizer(br.readLine());
        int a = Integer.parseInt(st.nextToken()), b = Integer.parseInt(st.nextToken());
        HashSet<Point> points = new HashSet<>();
        List<Point> pointList = new ArrayList<>();
        for (int i=0;i<n;i++){
            st = new StringTokenizer(br.readLine());
            Point p = new Point(Integer.parseInt(st.nextToken()),Integer.parseInt(st.nextToken()));
            points.add(p);
            pointList.add(p);
        }

        int cnt = 0;
        for (Point p : pointList){
            Point right = new Point(p.x+a, p.y);
            Point top = new Point(p.x, p.y+b);
            Point diag = new Point(p.x+a, p.y+b);
            if (points.contains(right)&&points.contains(top)&&points.contains(diag)) cnt++;
        }
        System.out.println(cnt);
    }
}

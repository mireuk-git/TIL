
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

class Point{
    int x;
    int y;
    Point(int x, int y){
        this.x = x;
        this.y = y;
    }
}

public class p15923 {
    public static void main(String[] args)throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n=Integer.parseInt(br.readLine());
        Point[] point = new Point[n];
        for (int i=0;i<n;i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int x = Integer.parseInt(st.nextToken());
            int y = Integer.parseInt(st.nextToken());
            point[i] = new Point(x,y);
        }
        int l = 0;
        for (int i=0;i<n-1;i++){
            if (point[i].x == point[i+1].x) l+=Math.abs(point[i].y-point[i+1].y);
            else if (point[i].y == point[i+1].y) l+=Math.abs(point[i].x-point[i+1].x);
        }
        if (point[0].x == point[n-1].x) l+=Math.abs(point[0].y-point[n-1].y);
        else if (point[0].y == point[n-1].y) l+=Math.abs(point[0].x-point[n-1].x);
        System.out.println(l);
    }
}

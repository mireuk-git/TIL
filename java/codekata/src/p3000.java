import java.util.HashMap;
import java.util.Scanner;

public class p3000 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        int[][] points = new int[n][2];
        HashMap<Integer, Integer> cnt_x =6 new HashMap<>();
        HashMap<Integer, Integer> cnt_y = new HashMap<>();
        for (int i=0;i<n;i++){
            String[] point = scanner.next().split(" ");
            int x=Integer.parseInt(point[0]);
            System.out.println(point[0]);
            int y=Integer.parseInt(point[1]);
            System.out.println("y");
            points[i][0]=x;
            System.out.println("points.x");
            points[i][1]=y;

            cnt_x.put(x,cnt_x.getOrDefault(x,0)+1);
            System.out.println("cnt_x");
            cnt_y.put(y,cnt_y.getOrDefault(y,0)+1);
        }
        scanner.close();
        System.out.println("input finished");

        long count=0;
        for (int i=0;i<n;i++){
            int x = points[i][0];
            int y = points[i][1];
            count+=(cnt_x.get(x)-1)*(cnt_y.get(y)-1);
        }
        System.out.println(count);

    }
}
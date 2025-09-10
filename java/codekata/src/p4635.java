import java.util.Scanner;

public class p4635 {
    public static void main(String[] args) {
        try (Scanner scanner = new Scanner(System.in)) {
            int n = scanner.nextInt();
            while (n!=-1) {
                int prevT=0;
                int distance=0;
                for (int i=0;i<n;i++){
                    int s = scanner.nextInt();
                    int t = scanner.nextInt();
                    distance=distance+s*(t-prevT);
                    prevT=t;
                }
                System.out.println(distance+" miles");
                n=scanner.nextInt();
            }
        }
    }
}

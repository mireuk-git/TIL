import java.util.Scanner;

public class App {
    public static int minCost(int[] r){
        int n = r.length;
        int[][] dp = new int[n][2];
        dp[0][0]=0;
        dp[0][1]=r[0];

        for (int i=1;i<n;i++){
            dp[i][0]=dp[i-1][1];
            dp[i][1]=Math.min(dp[i-1][0],dp[i-1][1])+r[i];
        }
        return Math.min(dp[n-1][0],dp[n-1][1]);
    }
    public static void main(String[] args) throws Exception {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        int[] r = new int[n];
        for (int i=0;i<n;i++){ r[i] = scanner.nextInt(); }
        scanner.close();

        System.out.println(minCost(r));
        
    }
}

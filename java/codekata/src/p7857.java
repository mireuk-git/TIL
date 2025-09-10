import java.util.Scanner;
public class p7857 {
    public static void main(String[] args) {
        int b;
        try (Scanner scanner = new Scanner(System.in)) {
            int n = Integer.parseInt(scanner.nextLine());
            String[] a = new String[n];
            a[0]=scanner.nextLine();
            b = a[0].length();
            for (int i=1;i<n;i++){
                a[i]=scanner.nextLine();
                int min;
                if (a[i].length()<a[i-1].length()) { min=a[i].length(); }
                else { min = a[i-1].length(); }
                
                int j=0;
                while (j<min && a[i].charAt(j)==a[i-1].charAt(j)) { j++; }
                b+=a[i].length()-j+1;
            }
        }
        System.out.println(b);
    }
}

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class p2765 {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int trip = 0;
        while(true){
            StringTokenizer st = new StringTokenizer(br.readLine());
            double diameter = Double.parseDouble(st.nextToken());
            int revol = Integer.parseInt(st.nextToken());
            double time = Double.parseDouble(st.nextToken());
            if (revol == 0) break;

            double pi = 3.1415927;
            double distance = diameter*revol*pi/12/5280;
            double mph = distance/time*3600;

            System.out.println(String.format("Trip #%d %.2f %.2f",++trip,distance,mph));
        }
    }
}

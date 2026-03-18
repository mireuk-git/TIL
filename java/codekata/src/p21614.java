
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class p21614 {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String instruction = br.readLine();
        String direction="";
        while (!instruction.equals("99999")){
            int d_code = Integer.parseInt(instruction.substring(0,1))+Integer.parseInt(instruction.substring(1,2));
            int steps = Integer.parseInt(instruction.substring(2,5));
            if (d_code%2==1) direction = "left";
            else if (d_code>0) direction = "right";
            System.out.println(direction+" "+steps);
            instruction = br.readLine();
        }
    }
}

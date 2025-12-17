
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class p13567 {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int m = Integer.parseInt(st.nextToken());
        int n = Integer.parseInt(st.nextToken());
        int x=0, y=0;
        int dx=1, dy=0;
        boolean valid = true;

        for (int i=0;i<n;i++){
            st = new StringTokenizer(br.readLine());
            String command = st.nextToken();
            int d = Integer.parseInt(st.nextToken());
            if (valid) {
                if (command.equals("TURN")) {
                    if (d==0) {
                        if (dx==1) { dx=0; dy=1; }
                        else if (dy==1) { dx=-1; dy=0; }
                        else if (dx==-1) { dx=0; dy=-1; }
                        else if (dy==-1) { dx=1; dy=0; }
                    }
                    else if (d==1) {
                        if (dx==1) { dx=0; dy=-1; }
                        else if (dy==-1) { dx=-1; dy=0; }
                        else if (dx==-1) { dx=0; dy=1; }
                        else if (dy==1) { dx=1; dy=0; }
                    }
                }
                else if (command.equals("MOVE")){
                    if (0<=x+dx*d && x+dx*d<=m && 0<=y+dy*d && y+dy*d<=m){
                        x+=dx*d;
                        y+=dy*d;
                    }
                    else valid = false;
                }
            }
        }
        if (!valid) System.out.println(-1);
        else System.out.println(x+" "+y);
    }
}

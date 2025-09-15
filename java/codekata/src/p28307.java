import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;
public class p28307{
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int c = Integer.parseInt(st.nextToken());
        int[][] tiles = new int[2][c];
        for (int x=0;x<2;x++){
            st=new StringTokenizer(br.readLine());
            for (int y=0;y<c;y++){
                tiles[x][y]=Integer.parseInt(st.nextToken());
            }
        }

        int meters=0;
        for (int x=0;x<2;x++){
            for (int y=0;y<c;y++){
                if (tiles[x][y]==1){
                    meters+=3;
                    if ((x+y)%2==0 && x<1 && tiles[x+1][y]==1){
                        meters-=1;
                    }
                    if ((x+y)%2==1 && x>0 && tiles[x-1][y]==1){
                        meters-=1;
                    }
                    if (y<c-1 && tiles[x][y+1]==1){
                        meters-=1;
                    }
                    if (y>0 && tiles[x][y-1]==1){
                        meters-=1;
                    }
                }
            }
        }
        System.out.println(meters);
    }
}
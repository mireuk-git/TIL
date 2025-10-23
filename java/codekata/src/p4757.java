
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class p4757 {
    public static void main(String[] args)throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        
        int n = Integer.parseInt(st.nextToken());
        String winner="";
        int winnerSolved=0 , winnerPenalty=0;
        for (int i=0;i<n;i++){
            st = new StringTokenizer(br.readLine());
            String name = st.nextToken();
            int solved=0, penalty=0;
            for (int j=0;j<4;j++){
                int tries = Integer.parseInt(st.nextToken());
                int time = Integer.parseInt(st.nextToken());
                if (time>0) {
                    solved++;
                    penalty+=time+(tries-1)*20;
                }
            }
            if (winnerSolved < solved || (winnerSolved == solved && winnerPenalty > penalty)){
                winner = name;
                winnerSolved = solved;
                winnerPenalty = penalty;
            }
        }
        System.out.println(winner+" "+winnerSolved+" "+winnerPenalty);
    }
}

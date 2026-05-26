
import java.util.ArrayDeque;
import java.util.Queue;

class Solution{
    public int solution(int[] players, int m, int k){
        int count=0;
        Queue<Integer> servers = new ArrayDeque<>();
        for (int t=0;t<24;t++){
            while (!servers.isEmpty() && servers.peek()<=t) servers.poll();
            while (players[t]>=(servers.size()+1)*m) {
                count++;
                servers.offer(t+k);
            }
        }
        return count;
    }
}

public class p389479 {
    
}

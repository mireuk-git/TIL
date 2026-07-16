
import java.util.HashMap;

class Solution{
    long solution(int[] weights){
        HashMap<Integer,Integer> counter = new HashMap<>();
        for (int w: weights){
            counter.put(w, counter.getOrDefault(w, 0)+1);
        }
        int[][] ratio = {{1,2},{2,3},{3,4}};

        long answer = 0;
        for (int k: counter.keySet()){
            for (int[] r: ratio){
                if (k%r[0]!=0) continue;
                int target = k*r[1]/r[0];
                answer+=(long)counter.get(k)*counter.getOrDefault(target,0);
            }
            answer+=(long)counter.get(k)*(counter.get(k)-1)/2;
        }
        return answer;
    }
}
public class p152996{
    public static void main(String[] args) {
        Solution s = new Solution();
        int[] weights = {100,180,360,100,270};
        System.out.println(s.solution(weights));
    }
}
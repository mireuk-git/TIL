
import java.util.ArrayList;
import java.util.List;

class Solution{
    public int[] solution(int[] progresses, int[] speeds){
        int iter = 0;
        List<Integer> result = new ArrayList<>();
        while (iter<progresses.length){
            int days = Math.ceilDiv((100-progresses[iter]),speeds[iter]);
            int count = 1;
            iter++;
            while (iter<progresses.length && progresses[iter]+speeds[iter]*days>=100){
                count++;
                iter++;
            }
            result.add(count);
        }
        int[] answer = new int[result.size()];
        for (int i=0;i<result.size();i++) answer[i] = result.get(i);
        return answer;
    }
}
public class p42586 {
    
}

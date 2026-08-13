
import java.util.ArrayList;
import java.util.Collections;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

class Solution{
    public int solution(int k, int[] tangerine){
        int answer=0;
        Map<Integer,Integer> counter = new HashMap<>();
        for (int i: tangerine){
            counter.put(i, counter.getOrDefault(i, 0)+1);
        }

        List<Integer> values = new ArrayList<>(counter.values());
        Collections.sort(values,Collections.reverseOrder());
        while(k>0){
            k-=values.get(answer);
            answer++;
        }
        return answer;
    }
}

public class p138476{
    public static void main(String[] args) {
        int[] tangerine = {1, 3, 2, 5, 4, 5, 2, 3};
        Solution s = new Solution();
        System.out.println(s.solution(4, tangerine));
    }
}

import java.util.ArrayList;
import java.util.List;

class Solution{
    public int solution(int[][] targets){
        List<int[]> l = new ArrayList<>();
        for (int[] t: targets) l.add(t);
        l.sort((a,b)->Integer.compare(a[1],b[1]));
        
        int end = 0;
        int count = 0;
        for (int[] t: l){
            if (t[0]>=end){
                count++;
                end = t[1];
            }
        }
        return count;
    }
}

public class p181188 {
    
}

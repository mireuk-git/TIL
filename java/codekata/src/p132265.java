
import java.util.HashMap;
import java.util.HashSet;
import java.util.Map;
import java.util.Set;

class Solution{
    public int solution(int[] topping){
        Map<Integer,Integer> left = new HashMap<>();
        Set<Integer> right = new HashSet<>();
        int result = 0;
        for (int t: topping) left.put(t,left.getOrDefault(t,0)+1);
        for (int t: topping){
            right.add(t);
            left.put(t, left.get(t)-1);
            if (left.get(t)==0) left.remove(t);

            if (left.keySet().size() == right.size()) result++;
        }
        return result;
    }
}

public class p132265 {
    
}

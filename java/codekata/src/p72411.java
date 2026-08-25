
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

class Solution{
    public String[] solution(String[] orders, int[] course){
        List<String> l = new ArrayList<>();
        for (int c: course){
            Map<String,Integer> counter = new HashMap<>();
            for (String o: orders){
                char[] chars = o.toCharArray();
                Arrays.sort(chars);
                combination(chars,0,c,"",counter);
            }

            System.out.println("counter contains:");
            for (String s: counter.keySet()) System.out.println(s+" "+counter.get(s));

            int max = 0;
            List<String> tmp = new ArrayList<>();
            for (String s: counter.keySet()){
                if (counter.get(s)>max){
                    max = counter.get(s);
                    tmp = new ArrayList<>();
                    tmp.add(s);
                }
                else if (counter.get(s)==max){
                    tmp.add(s);
                }
            }

            System.out.println("max indicated: value "+max);
            for (String s:tmp) System.out.println(s);

            if (max>=2){
                for (String s: tmp) {
                    if (!l.contains(s)) l.add(s);
                }
            }
        }
        Collections.sort(l);
        String[] r = new String[l.size()];
        for (int i=0;i<l.size();i++) r[i] = l.get(i);
        return r;
    }
    private void combination(char[] arr, int start, int r, String result, Map<String,Integer> counter){
        if (r==0){
            counter.put(result,counter.getOrDefault(result,0)+1);
            return;
        }
        for (int i=start;i<arr.length;i++){
            combination(arr,i+1,r-1,result+arr[i],counter);
        }
    }
}

public class p72411 {
    public static void main(String[] args) {
        Solution s = new Solution();
        String[] orders = {"ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"};
        int[] course = {2,3,4};
        String[] str = s.solution(orders, course);
        for(String c: str) System.out.println(c);
    }
}

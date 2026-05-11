import java.util.ArrayList;
import java.util.List;

class Solution{
    class Pair{
        String s;
        char c;
        Pair(String s, int n){
            this.s = s;
            this.c = s.charAt(n);
        }
    }
    public String[] solution(String[] strings, int n){
        List<Pair> list = new ArrayList<>();
        for (String s: strings){
            list.add(new Pair(s,n));
        }
        
        list.sort((p1,p2)->{
            if (p1.c != p2.c) return Character.compare(p1.c,p2.c);
            return p1.s.compareTo(p2.s);
        });
        String[] answer = new String[strings.length];
        for (int i=0;i<strings.length;i++) answer[i] = list.get(i).s;
        return answer;
    }
}

public class p12915 {
    public static void main(String[] args){
        String[] strings = {"sun", "bed", "car"};
        int n = 1;
        Solution s = new Solution();
        String[] answer = s.solution(strings,n);
        for (String c: answer) System.out.print(c+" ");
    }
}

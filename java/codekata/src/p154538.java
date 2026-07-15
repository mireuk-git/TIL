import java.util.ArrayDeque;
import java.util.Deque;

class Tuple{
    int y;
    int s;
    Tuple(int y, int s){
        this.y = y;
        this.s = s;
    }
}

class Solution{
    int solution(int x, int y, int n){
        Deque<Tuple> queue = new ArrayDeque<>();
        queue.add(new Tuple(y,0));

        while (!queue.isEmpty()){
            Tuple t = queue.pop();
            int ty = t.y;
            int s = t.s;
            if (x==ty) return s;
            if (x>ty) continue;

            if (ty%3==0) queue.add(new Tuple(ty/3,s+1));
            if (ty%2==0) queue.add(new Tuple(ty/2,s+1));
            queue.add(new Tuple(ty-n,s+1));
        }
        return -1;
    }
}

public class p154538 {
    public static void main(String[] args) {
        Solution s = new Solution();
        System.out.println(s.solution(10,40,5));
    }
}

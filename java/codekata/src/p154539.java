import java.util.ArrayDeque;
import java.util.Deque;

class Solution{
    int[] solution(int[] numbers){
        Deque<Integer> stack = new ArrayDeque<>();
        int n = numbers.length;
        int[] answer = new int[n];
        for (int i=0;i<n;i++) answer[i]=-1;

        for (int i=0;i<n;i++){
            while (!stack.isEmpty() && numbers[stack.peek()]<numbers[i]){
                answer[stack.pop()] = numbers[i];
            }
            stack.push(i);
        }
        return answer;
    }
}

public class p154539{
    public static void main(String[] args) {
        int[] numbers = {2,3,3,5};
        Solution s = new Solution();
        int[] answer = s.solution(numbers);
        for (int i: answer) System.out.print(i+" ");
        System.out.println();
    }
}
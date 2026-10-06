
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

class Solution{
    private int gcd(int a, int b){
        while (b>0){
            int tmp = a;
            a = b;
            b = tmp%b;
        }
        return a;
    }
    public int solution(int[] arrayA, int[] arrayB){
        int a = arrayA[0];
        for (int i: arrayA)
            a = gcd(i,a);
        List<Integer> a_divisor = new ArrayList<>();
        for (int i=1;i<=Math.sqrt(a);i++){
            if (a%i==0){
                a_divisor.add(i);
                a_divisor.add(a/i);
            }
        }
        Collections.sort(a_divisor,Collections.reverseOrder());

        int b = arrayB[0];
        for (int i: arrayB)
            b = gcd(i,b);
        List<Integer> b_divisor = new ArrayList<>();
        for (int i=1;i<=Math.sqrt(b);i++){
            if (b%i==0){
                b_divisor.add(i);
                b_divisor.add(b/i);
            }
        }
        Collections.sort(b_divisor,Collections.reverseOrder());

        int a_pointer=0, b_pointer=0;
        while (true){
            if (a_divisor.get(a_pointer)==1 && b_divisor.get(b_pointer)==1)
                return 0;
            boolean divided = false;
            if (a_divisor.get(a_pointer)>b_divisor.get(b_pointer)){
                for (int i: arrayB){
                    if (i%a_divisor.get(a_pointer)==0){
                        divided = true;
                        break;
                    }
                }
                if (!divided) return a_divisor.get(a_pointer);
                a_pointer++;
            }
            else{
                for (int i:arrayA){
                    if (i%b_divisor.get(b_pointer)==0){
                        divided = true;
                        break;
                    }
                }
                if (!divided) return b_divisor.get(b_pointer);
                b_pointer++;
            }
        }
    }
}

public class p135807 {
    public static void main(String[] args) {
        Solution s = new Solution();
        int[] arrayA = {10,20};
        int[] arrayB = {5,17};
        System.out.println(s.solution(arrayA, arrayB));
    }
}

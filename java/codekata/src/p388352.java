
import java.util.ArrayList;
import java.util.List;

class Solution{
    void combination(int start, int n, int r, int[] selected, int depth, List<int[]> result){
        if (depth==r){
            result.add(selected.clone());
            return;
        }
        for (int i=start;i<=n;i++){
            selected[depth]=i;
            combination(i+1,n,r,selected,depth+1,result);
        }
    }
    

    public int solution(int n, int[][] q, int[] ans){
        List<int[]> candidates = new ArrayList<>();
        combination(1,n,5,new int[5],0,candidates);
        for (int i=0;i<q.length;i++){
            List<int[]> newCandidates = new ArrayList<>();
            for (int[] c: candidates){
                int count=0;
                for (int e: q[i]){
                    for (int num:c){
                        if (e==num){
                            count++;
                            break;
                        }
                    }
                }
                if (count==ans[i]) newCandidates.add(c);
            }
            candidates = newCandidates;
        }
        return candidates.size();
    }
}


public class p388352 {
    public static void main(String[] args) {
        int n=10;
        int[][] q = {{1, 2, 3, 4, 5}, {6, 7, 8, 9, 10}, {3, 7, 8, 9, 10}, {2, 5, 7, 9, 10}, {3, 4, 5, 6, 7}};
        int[] ans = {2, 3, 4, 3, 3};
    }
}

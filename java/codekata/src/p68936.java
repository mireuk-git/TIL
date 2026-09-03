class Solution{
    int[] answer = {0,0};
    int[][] arr;
    void quad(int x, int y, int n){
        int cur = arr[x][y];
        boolean reduce = true;
        for (int i=x;i<x+n;i++){
            for (int j=y;j<y+n;j++) {
                if (cur!=arr[i][j]){
                    reduce = false;
                    break;
                }
            }
            if (!reduce) break;
        }
        if (reduce) answer[cur]++;
        else{
            int half = n/2;
            quad(x,y,half);
            quad(x+half,y,half);
            quad(x+half,y+half,half);
            quad(x,y+half,half);
        }
    }
    public int[] solution(int[][] arr){
        this.arr = arr;
        quad(0,0,arr.length);
        return answer;
    }
}

public class p68936 {
    public static void main(String[] args) {
        Solution s = new Solution();
        int[][] arr = {{1,1,1,1,1,1,1,1},{0,1,1,1,1,1,1,1},{0,0,0,0,1,1,1,1},{0,1,0,0,1,1,1,1},{0,0,0,0,0,0,1,1},{0,0,0,0,0,0,0,1},{0,0,0,0,1,0,0,1},{0,0,0,0,1,1,1,1}};
        int[] ans = s.solution(arr);
        System.out.println(ans[0]+" "+ans[1]);
    }
}

class Solution{
    public int solution(String[][]board, int h, int w){
        int n = board.length;
        int count=0;
        int[] dh={0,1,-1,0}, dw={1,0,0,-1};
        for(int i=0;i<4;i++){
            int hCh=h+dh[i], wCh=w+dw[i];
            if (0<=hCh && hCh<n && 0<=wCh && wCh<n)
            if (board[h][w].equals(board[hCh][wCh])) count++;
        }
        return count;
    }
}

public class p250125 {
    
}

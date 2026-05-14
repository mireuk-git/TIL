
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

class Solution{
    public int solution(int[] mats, String[][] park){
        List<Integer> ms = new ArrayList<>();
        for (int i: mats) ms.add(i);
        ms.sort(Collections.reverseOrder());
        for (int m: ms){
            for (int x=0;x<=park.length-m;x++){
                for (int y=0;y<=park[x].length-m;y++){
                    if (park[x][y].equals("-1")){
                        boolean success = true;
                        for (int i=0;i<m;i++){
                            for (int j=0;j<m;j++){
                                if (!park[x+i][y+j].equals("-1")){
                                    success = false;
                                    break;
                                }
                            }
                            if (!success) break;
                        }
                        if (success) return m;
                    }
                }
            }
        }
        return -1;
    }
}

public class p340198{
    public static void main(String[] args){

    }
}
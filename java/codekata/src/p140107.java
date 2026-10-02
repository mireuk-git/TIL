class Solution{
    public long solution(int k, int d){
        long count = 0;
        long ld = d;
        for (long y=0;y<=d;y+=k){
            count += (long)Math.sqrt(ld*ld-y*y)/k+1;
        }
        return count;
    }
}

public class p140107{

}

class Solution{
    long countCircle(int r, boolean edge){
        long x = 0;
        long y = r;
        long count = 0;
        while (y>0){
            while (x*x+y*y>(long)r*r) y-=1;
            if (!edge && x*x+y*y==(long)r*r) y-=1;
            if (y>0) count+=y;
            x++;
        }
        return count;
    }
    long solution(int r1, int r2){
        long d1 = countCircle(r1, false);
        long d2 = countCircle(r2, true);
        return (d2-d1)*4;
    }
}

public class p181187 {
    public static void main(String[] args){

    }
}
10^12
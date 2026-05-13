class Solution{
    int[] swap(int[] l){
        int tmp=l[0];
        l[0]=l[1];
        l[1]=tmp;
        return l;
    }
    public int solution(int[] wallet, int[] bill){
        if (wallet[0]>wallet[1]) swap(wallet);
        if (bill[0]>bill[1]) swap(bill);
        int answer=0;
        while (wallet[0]<bill[0] || wallet[1]<bill[1]){
            bill[1]/=2;
            answer++;
            if (bill[0]>bill[1]) swap(bill);
        }
        return answer;
    }
}

public class p340199 {
    
}

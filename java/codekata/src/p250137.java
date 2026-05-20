class Solution{
    public int solution(int[] bandage, int health, int[][]attacks){
        int hp=health;
        int t=0;
        for (int[] a: attacks){
            if (hp<health) hp+=Math.min(health-hp, bandage[1]*(a[0]-t-1)+(a[0]-t-1)/(bandage[0])*bandage[2]);
            hp-=a[1];
            if (hp<=0) return -1;
            t=a[0];
        }
        return hp;
    }
}

public class p250137 {
    public static void main(String[] args) {
        int[] bandage={3,2,7};
        int health = 20;
        int[][] attacks={{1,15},{5,16},{8,6}};
        Solution s = new Solution();
        int r = s.solution(bandage,health,attacks);
        System.out.println(r);
    }
}

class Solution{
    public int[] solution(String[] name, int[] yearning,String[][] photo){
        int[] result= new int[photo.length];
        for (int i=0;i<photo.length;i++){
            for (String s: photo[i]){
                for (int j=0;j<name.length;j++){
                    if (s.equals(name[j])) result[i]+=yearning[j];
                }
            }
        }
        return result;
    }
}

public class p176963 {
    public static void main(String[] args) {
        String[] name = {"may", "kein", "kain", "radi"};
        int[] yearning = {5, 10, 1, 3};
        String[][] photo = {{"may", "kein", "kain", "radi"},{"may", "kein", "brin", "deny"}, {"kon", "kain", "may", "coni"}};
        Solution s = new Solution();
        int[] result = s.solution(name,yearning,photo);
        for (int i:result) System.out.print(i+" ");
    }
}

class Solution{
    public int[] solution(String s){
        int[] count = {0,0};
        String str = s;
        while (!str.equals("1")){
            count[0]++;
            int zero = 0;
            for (int j=0;j<str.length();j++){
                if (str.charAt(j)=='0') zero++;
            }
            count[1]+=zero;
            int l = str.length()-zero;
            String b = "";
            while (l>0){
                b = (l%2)+b;
                l/=2;
            }
            str = b;
        }
        return count;
    }
}

public class p70129 {
    public static void main(String[] args) {
        Solution s = new Solution();
        int[] result = s.solution("110010101001");
        System.out.println("result - count[0]: "+result[0]+" count[1]: "+result[1]);
    }
}

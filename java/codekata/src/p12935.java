class Solution{
    public int[] solution(int[] arr){
        if (arr.length<=1) {
            int[] answer = {-1};
            return answer;
        }
        int min=arr[0], t=0;
        for (int i=1;i<arr.length;i++){
            if (arr[i]<min) {min=arr[i]; t=i;}
        }
        int[] answer = new int[arr.length-1];
        for (int i=0;i<t;i++) answer[i]=arr[i];
        for (int i=t;i<arr.length-1;i++) answer[i]=arr[i+1];
        return answer;
    }
}

public class p12935 {
    public static void main(String[] args) {
        int[] arr={1,5,9,10};
        Solution s = new Solution();
        int[] answer=s.solution(arr);
        for (int i=0;i<answer.length;i++) System.out.println(answer[i]);
    }
}

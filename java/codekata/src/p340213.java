class Solution{
    int toSec(String s){
        int sec=Integer.parseInt(s.substring(0,2))*60+Integer.parseInt(s.substring(3,5));
        return sec;
    }

    public String solution(String video_len, String pos, String op_start, String op_end, String[] commands){
        int len=toSec(video_len);
        int p=toSec(pos);
        int os=toSec(op_start);
        int oe=toSec(op_end);

        if (os<=p && p<oe) p=oe;
        for (String c: commands){
            if (c.equals("prev")){
                p-=10;
                if (p<0) p=0;
            }
            else if (c.equals("next")){
                p+=10;
                if (p>len) p=len;
            }
            if (os<=p && p<oe) p=oe;
        }
        System.out.println(p);

        String answer=String.format("%02d:%02d",p/60,p%60);
        return answer;
    }
}

public class p340213 {
    public static void main(String[] args) {
        String video_len="34:33";
        String pos = "13:00";
        String op_start = "00:55";
        String op_end="02:55";
        String[] commands={"next","prev"};
        Solution s = new Solution();
        String answer=s.solution(video_len, pos, op_start, op_end, commands);
        System.out.println(answer);
    }
}

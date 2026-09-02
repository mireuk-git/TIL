class Solution{
    public int solution(String skill, String[] skill_trees){
        int count = 0;
        for (String s: skill_trees){
            int lv = 0;
            boolean avail = true;
            for (char c: s.toCharArray()){
                for (int i=0;i<skill.length();i++){
                    if (c == skill.charAt(i)){
                        if (c==skill.charAt(lv)) lv++;
                        else{
                            avail = false;
                            break;
                        }
                    }
                }
                if (!avail) break;
            }
            if (avail) count+=1;
        }
        return count;
    }
}

public class p49993{
    public static void main(String[] args) {
        String skill = "CBD";
        String[] skill_trees = {"BACDE", "CBADF", "AECB", "BDA"};
        Solution s = new Solution();
        System.out.println(s.solution(skill, skill_trees));
    }
}
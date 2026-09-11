
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

class Solution{
    public String[] solution(String[] record){
        Map<String,String> user = new HashMap<>();
        String[][] newRecord = new String[record.length][3];
        for (int i=0;i<record.length;i++){
            newRecord[i] = record[i].split(" ");
            if (newRecord[i][0].equals("Enter") || newRecord[i][0].equals("Change")) {
                    user.put(newRecord[i][1],newRecord[i][2]);
            }
        }

        List<String> result = new ArrayList<>();
        for (String[] r: newRecord){
            if (r[0].equals("Enter")){
                String s = user.get(r[1])+"님이 들어왔습니다.";
                result.add(s);
            }
            else if (r[0].equals("Leave")){
                String s = user.get(r[1])+"님이 나갔습니다.";
                result.add(s);
            }
        }
        String[] answer = new String[result.size()];
        for (int i=0;i<result.size();i++) answer[i] = result.get(i); 
        return answer;
    }
}

public class p42888 {
    public static void main(){

    }
}

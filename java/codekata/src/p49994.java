
import java.util.HashSet;
import java.util.Set;

class Solution{
    public int solution(String dirs){
        Set<String> routes = new HashSet<>();
        int[] pos = {0,0};

        for (char d: dirs.toCharArray()){
            int x = pos[0];
            int y = pos[1];
            switch (d) {
                case 'R' -> {
                    if (pos[0]==5) continue;
                    pos[0]++;
                }
                case 'L' -> {
                    if (pos[0]==-5) continue;
                    pos[0]--;
                }
                case 'U' -> {
                    if (pos[1]==5) continue;
                    pos[1]++;
                }
                case 'D' -> {
                    if (pos[1]==-5) continue;
                    pos[1]--;
                }
            }

            String route;
            if (x<pos[0]||(x==pos[0]&&y<pos[1])){
                route=x+""+y+""+pos[0]+""+pos[1];
            }
            else{
                route=pos[0]+""+pos[1]+""+x+""+y;
            }
            routes.add(route);
        }
        return routes.size();
    }
}

public class p49994 {
    
}


import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;

class Solution{
    class Robot{
        int[][] points;
        int n;
        int[] pos;
        int progress;

        Robot(int[][] points){
            this.points = points;
            this.progress = 0;
            this.n = points.length-1;
            this.pos = points[0];
        }

        boolean active(){
            return this.progress < this.n;
        }

        void move(){
            //완료 로봇 비활성화
            if (!this.active()) return;
            //위치변경
            int r = this.pos[0];
            int c = this.pos[1];
            int r_t = this.points[progress+1][0];
            int c_t = this.points[progress+1][1];

            if (r<r_t) this.pos[0]+=1;
            else if (r_t<r) this.pos[0]-=1;
            else if (c<c_t) this.pos[1]+=1;
            else if (c_t<c) this.pos[1]-=1;
            //진행도 갱신
            if (this.pos[0]==r_t && this.pos[1]==c_t) {
                this.progress++;
            }
        }
    }
    public int solution(int[][] points, int[][] routes){
        int count = 0;
        int l = routes[0].length;
        List<Robot> robots = new ArrayList<>();
        //routes를 point의 좌표로 전환, robots 초기화
        for (int[] route: routes){
            int[][] p = new int[route.length][2];
            for (int j=0;j<l;j++){
                p[j][0] = points[route[j]-1][0];
                p[j][1] = points[route[j]-1][1];
            }
            robots.add(new Robot(p));
        }

        while (!robots.isEmpty()){
            // 충돌확인
            HashMap<String,Integer> c = new HashMap<>();
            for (Robot r: robots){
                String pos = r.pos[0]+","+r.pos[1];
                c.put(pos,c.getOrDefault(pos,0)+1);
            }
            for (String k: c.keySet()){
                if (c.get(k)>1) count++;
            }
            // robot 비활성화
            List<Robot> newRobots = new ArrayList<>();
            for (Robot r: robots) if (r.active()) newRobots.add(r);
            robots = newRobots;
            // move
            for (Robot r: robots) r.move();
        }
        return count;
    }
}

public class p340211{
    public static void main(String[] args){
        int[][] points = {{3,2},{6,4},{4,7},{1,4}};
        int[][] routes = {{4,2},{1,3},{2,4}};
        Solution s = new Solution();
        System.out.println(s.solution(points, routes));
    }
}
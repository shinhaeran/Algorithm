import java.util.*;
class Solution {
    public String solution(String[] participant, String[] completion) {
        String answer = "";
        // List p1 = new ArrayList<String>();
        
        // for(String s : participant)
        //     p1.add(s);
        // List<String> c1 = Arrays.asList(completion);
        // for(String s :participant){
        //     // p1.remove(s);
        //     if( !c1.contains(s)){
        //         answer = s; break;
        //     }
        // }
        Arrays.sort(participant);
        Arrays.sort(completion);
        for(int i=0; i<completion.length; i++){
            if(!participant[i].equals(completion[i])){
                return participant[i];
            }
        }
        answer = participant[participant.length-1];
        return answer;
    }
}
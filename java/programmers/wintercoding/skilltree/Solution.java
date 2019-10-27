package wintercoding.skilltree;

class Solution {
    public int solution(String skill, String[] skill_trees) {
        int answer = 0;

        int skillLength = skill.length();

        for(int i=0; i< skill_trees.length; i++){
            String checkSkillTree = skill_trees[i];
            boolean wrongSkillTree = false;
            int checkSkillIndex = 0;

            //검사 시작
            for(int j = 0; j<checkSkillTree.length(); j++){
                if(checkSkillIndex < skillLength-1){
                    for(int k=checkSkillIndex+1; k<skillLength; k++){
                        if(checkSkillTree.charAt(j) == skill.charAt(k)){
                            wrongSkillTree = true;
                            break;
                        }
                    }
                }
                if(checkSkillTree.charAt(j) == skill.charAt(checkSkillIndex)){
                    checkSkillIndex+=1;
                    if(checkSkillIndex == skillLength) break;
                }
            }

            if(!wrongSkillTree){
                answer+=1;
            }
        }
        return answer;
    }
}

//
// Created by Jeongho on 2019-10-30.
//

#include <vector>
#include <queue>
#include <iostream>

using namespace std;

int deploy(queue<pair<int,int>> &work,int deploy_count);

int main(){

    vector<int> progresses;
    vector<int> speeds;
//
    progresses.push_back(93);
    progresses.push_back(30);
    progresses.push_back(55);

    speeds.push_back(1);
    speeds.push_back(30);
    speeds.push_back(5);

    vector<int> answer;

    queue<pair<int,int>> work;

    for (auto it = progresses.begin(); it != progresses.end(); it++) {
        int index = distance(progresses.begin(),it);
        work.push(make_pair(*it,index));
    }

    do{
        int deploy_count = 0;
        //work progress
        for(unsigned int i=0; i<work.size();i++){
            auto temp = work.front();
            if(temp.first<100)
                temp.first+=speeds[temp.second];
            work.pop();
            work.push(temp);
        }

        //deploy
        deploy_count = deploy(work,deploy_count);
        if(deploy_count>0){
            answer.emplace_back(deploy_count);
        }

    }while (!work.empty());

    for(auto i : answer){
        cout<<i;
    }

    return 0;
}

int deploy(queue<pair<int,int>> &work,int deploy_count){
    if(work.front().first >= 100){
        work.pop();
        deploy_count+=1;
        if(!work.empty()){
            return deploy(work,deploy_count);
        } else return deploy_count;
    }else{
        return deploy_count;
    }
}

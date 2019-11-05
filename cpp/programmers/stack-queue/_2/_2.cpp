//
// Created by Jeongho on 2019-10-31.
//

#include <string>
#include <vector>
#include <queue>
#include <iostream>
#include <algorithm>


using namespace std;

int main(){
    vector<int> priorities;
    for(auto i : {1,1,9,1,1,1}){
        priorities.push_back(i);
    }
//
//    for(auto i : {2,1,3,2}){
//        priorities.push_back(i);
//    }

    int location = 0;

    /// -----------------
    priority_queue<int> pq;
    queue<pair<int,int>> print_q;
    queue<pair<int,int>> final_print_q;

    for(auto i : priorities){
        pq.push(i);
    }

    for (auto it = priorities.begin(); it != priorities.end(); it++) {
        int index = distance(priorities.begin(),it);
        // (우선순위, 인덱스)
        print_q.push(make_pair(*it,index));
    }

    do{
        auto temp = print_q.front();
            // 우선순위 높은게 있으면
        if(temp.first<pq.top()){
            print_q.pop();
            print_q.push(temp);
        }else{
            final_print_q.push(temp);
            pq.pop();
            print_q.pop();
        }
        //print
//        final_print_q.push()
    }while (!print_q.empty());


    int answer;
    for (int i = 0; !final_print_q.empty(); i++) {
        if(final_print_q.front().second==location){
            answer = i+1;
            break;
        }
        final_print_q.pop();
    }
    cout<<answer+1;
    //번째 +1

}
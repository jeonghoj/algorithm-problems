//
// Created by Jeongho on 2019-11-01.
//

#include <vector>
#include <queue>
#include <iostream>

using namespace std;

int main(){
    vector<int> nums;
    for(auto i : {5,1,1,1,1,1}){
        nums.push_back(i);
    }

    priority_queue<pair<int,int>,vector<pair<int,int>>,greater<>> pq;

    for (int i = 0; i < nums.size(); i++) {
        pq.push(make_pair(nums[i],i));
    }

    int size = pq.size();
    for (int i = 0; i < size; i++) {
        auto temp = pq.top();
        cout<<temp.first<<":"<<temp.second<<endl;
        pq.pop();
    }

    return 0;

}


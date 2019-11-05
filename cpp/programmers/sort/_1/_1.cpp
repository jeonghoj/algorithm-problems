//
// Created by Jeongho on 2019-11-03.
//

#include <string>
#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;

int main(){
    vector<int> array;
    vector<vector<int>> commands;

    for(auto i : {1, 5, 2, 6, 3, 7, 4}){
        array.push_back(i);
    }

    commands.push_back({2, 5, 3});
    commands.push_back({4, 4, 1});
    commands.push_back({1, 7, 3});

    // ----

    vector<int> answer;

    for (auto command : commands) {
        vector<int> temp_arr;
        int from = command[0];
        int to = command[1];
        int index = command[2];

        for (auto it = array.begin()-1 + from; it != array.begin() + to; it++) {
            temp_arr.push_back(*it);
        }
        sort(temp_arr.begin(),temp_arr.end());
        answer.push_back(temp_arr[index-1]);
        temp_arr.clear();
    }

    for(auto i : answer){
        cout<<i;
    }

}
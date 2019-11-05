//
// Created by Jeongho on 2019-11-01.
//

#include <string>
#include <vector>
#include <iostream>

using namespace std;

int main(){
    int n = 5;
    vector<int> lost;
    vector<int> reserve;

    // -- 초기값 --
    for(auto i : {2,4}){
        lost.push_back(i);
    }
    for(auto i : {3}){
        reserve.push_back(i);
    }

    // -- 본문 --

    int answer = 0;

    for(auto r_it = reserve.begin(); r_it != reserve.end();){
        bool found = false;
        for (auto l_it = lost.begin(); l_it != lost.end();) {
            if(*r_it == *l_it){
                lost.erase(l_it);
                reserve.erase(r_it);
                found = true;
                break;
            } else {
                l_it++;
            }
        }
        if(!found){
            r_it++;
        }

    }


    for (auto r_it = reserve.begin(); r_it != reserve.end();) {
        bool found = false;
        if (!lost.empty()) {
            for (auto l_it = lost.begin(); l_it != lost.end();) {
                if (*l_it == *r_it - 1) {
                    lost.erase(l_it);
                    reserve.erase(r_it);
                    found = true;
                    break;
                } else if (*l_it == *r_it + 1) {
                    lost.erase(l_it);
                    reserve.erase(r_it);
                    found = true;
                    break;
                } else {
                    l_it++;
                }
            }
        }
        if (!found) {
            r_it++;
        }
    }

    answer = n - lost.size();

    cout<<answer;


}

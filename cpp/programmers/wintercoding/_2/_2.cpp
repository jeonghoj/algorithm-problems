//
// Created by Jeongho on 2019-10-31.
//

#include <iostream>
#include <cmath>
#include <vector>

using namespace std;

void solution(vector<int> &sol,int n);

int main(){

    int n = 4;
    vector<int> answer;

    solution(answer,n);

    for (int & it : answer) {
        cout<<it;
    }

}

void solution(vector<int> &sol,int n){
    if(n==1) {
        sol.push_back(0);
    }else{
        solution(sol,--n);
        vector<int> temp;
//        int center_index = (int)pow(2,n)-1;
        int temp_center_index = (int)pow(2,n-1)-1;
        temp = sol;
//        sol.insert(sol.begin(),temp.begin(),temp.end());
        temp[temp_center_index] = 1 - temp[temp_center_index];
        sol.push_back(0);
        sol.insert(sol.end(),temp.begin(),temp.end());
    }



}

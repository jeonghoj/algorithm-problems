//
// Created by Jeongho on 2019-11-04.
//

#include <string>
#include <vector>
#include <algorithm>
#include <cmath>
#include <iostream>

using namespace std;

bool cmp(const int &a ,const int &b);

int main(){
    vector<int> numbers;
    for(auto i : {6, 10, 2}) numbers.push_back(i);

    string answer;

    vector<int> temp = numbers;
    sort(temp.begin(),temp.end());

    if(temp.back() == 0){
        answer = "0";
    }else{
        sort(numbers.begin(),numbers.end(),cmp);
        for(auto i : numbers){
            answer += to_string(i);
        }
    }

    cout<<answer;
}

// 첫번째 인자가 작을 경우 true 리턴
bool cmp(const int &a ,const int &b){

    if(log10(a)+1 == log10(b)+1){
        return a<b;
    }else{
        string s_a = to_string(a);
        string s_b = to_string(b);
        return s_b + s_a < s_a + s_b;
    }

}


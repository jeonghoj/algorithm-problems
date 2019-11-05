//
// Created by Jeongho on 2019-11-03.
//

#include <string>
#include <vector>
#include <algorithm>
#include <iostream>

using namespace std;

int main() {
    vector<int> scoville;
    int K;

    for(auto i : {1, 2, 3, 9, 10, 12}){
        scoville.push_back(i);
    }
    K=7;

    // 힙 만들기
    // size 검사 뒤에 값 2개 빼기 -> 섞기 -> 넣기
    // 경계 조건
    // size가 1일때 값 하나가 K보다 큰지 작은지
    // size가 2이상일 때 가장 작은 값이 K보다 큰지 작은지

    int answer = 0;


    make_heap(scoville.begin(),scoville.end(),greater<int>());

    int count = 0;
    while(scoville.size()>1){
        // 젤 작은 값 뒤로 보내기
        pop_heap(scoville.begin(),scoville.end(),greater<int>());
        int min_first = scoville.back();
        scoville.pop_back();
        pop_heap(scoville.begin(),scoville.end(),greater<int>());
        int min_second = scoville.back();
        scoville.pop_back();
        int mixed_cook = min_first + (min_second*2);
        scoville.push_back(mixed_cook);
        push_heap(scoville.begin(),scoville.end(),greater<int>());
        count++;
        if(scoville.front()>=K){
            break;
        }
    }
    answer = count;
    if(scoville.front() < K){
        answer = -1;
    }


    cout<<answer;

//    return answer;
}
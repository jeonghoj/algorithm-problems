//
// Created by Jeongho on 2019-10-28.
//

#include <iostream>
#include <queue>

using namespace std;

// container 는 그 자체로 포인터. 그 포인터 주소를 넘기고싶으면 변수앞에 &붙인다
void q_para(queue<int> &q);

int main(){
    queue<int> q;
    cout<<"q size"<<q.size()<<endl;
    q.push(1);
    cout<<"q size"<<q.size()<<endl;
    q.push(2);
    q.push(3);
    q.push(4);

    q.pop();


    cout<<q.front();

    cout<<q.back();

    cout<<q.size();

    cout<<q.empty() ? "yes" : "no";

}

void q_para(queue<int> q){
    cout<<endl;
    cout<<"func start";
    cout<<q.front();
    q.pop();
    cout<<q.front();
    cout<<"func end";
    cout<<endl;
}
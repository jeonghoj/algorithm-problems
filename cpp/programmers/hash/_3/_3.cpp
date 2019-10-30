//
// Created by Jeongho on 2019-10-27.
//

#include <iostream>
#include <string>
#include <vector>
#include <set>
#include <map>

using namespace std;

int main(){
    vector<vector<string>> clothes;
    vector<string> temp_cloth;
    temp_cloth.emplace_back("yellow_hat");
    temp_cloth.emplace_back("headgear");
    clothes.push_back(temp_cloth);
    temp_cloth.clear();
    temp_cloth.emplace_back("blue_sunglasses");
    temp_cloth.emplace_back("eyewear");
    clothes.push_back(temp_cloth);
    temp_cloth.clear();
    temp_cloth.emplace_back("green_turban");
    temp_cloth.emplace_back("headgear");
    clothes.push_back(temp_cloth);
    temp_cloth.clear();

    unsigned int result=1;
    set<string> cl;
    multimap<string,string> mp;
    for(auto i:clothes){
        cl.insert(i.back());
        mp.insert(make_pair(i.back(),i.front()));
    }
    cout<<"a count :" << mp.count("headgear")<<endl;

    multimap<string,string>::iterator map_it;
    for(map_it = mp.begin(); map_it!=mp.end();map_it++){
        cout<<map_it->first<<":"<<map_it->second<<endl;
    }

    set<string>::iterator set_it;
    for(set_it = cl.begin(); set_it != cl.end(); set_it++){
        result*=(mp.count(*set_it))+1;
    }

    cout<<result-1;







    set<string> s1;
    set<vector<string>> s2;
    s1.insert("str");
    s1.insert("a1");
    s1.insert("a2");
    vector<string> temp;
    temp.push_back("a1");
    temp.push_back("a2");
    s2.insert(temp);
    vector<string> temp2;
    temp2.push_back("a1");
    temp2.push_back("a2");
    s2.insert(temp2);

    for(auto i : s2){
        cout<<s2.size()<<" ";
    }

    return 0;
}

int solution(vector<vector<string>> clothes) {

    int answer = 0;

    return answer;
}
//
// Created by Jeongho on 2019-10-29.
//

#include <string>
#include <vector>
#include <map>

#include <iostream>

using namespace std;

int main(){

    vector<string> genres;
    genres.emplace_back("classic");
    genres.emplace_back("pop");
    genres.emplace_back("classic");
    genres.emplace_back("pop");
    genres.emplace_back("classic");
    genres.emplace_back("classic");
    vector<int> plays;
    plays.push_back(500);
    plays.push_back(600);
    plays.push_back(150);
    plays.push_back(5500);
    plays.push_back(500);
    plays.push_back(500);

    // first 장르별 sort
    // second 장르별 play가 많은 순으로 sort

    vector<int> answer;

    map<string,int> genre_plays; // classic 1450

    multimap<string,multimap<int,int>> genre_index; // classic 800:3

    for(auto g_iter = genres.begin(); g_iter != genres.end(); g_iter++){
        int index = distance(genres.begin(), g_iter);
        // 장르별 노래 인덱스
        if(genre_plays.find(*g_iter) == genre_plays.end()){
            // 장르를 못찾는다 -> 처음 넣는 값이다
            multimap<int,int> temp;
            temp.clear();
            temp.insert(make_pair(plays[index],index));
            genre_index.insert(make_pair(*g_iter, temp));

            genre_plays.insert(make_pair(*g_iter, plays[index]));

        }else{
            // 존재하는 값이다
            genre_index.find(*g_iter)->second.insert(make_pair(plays[index], index));
            genre_plays[*g_iter]+=plays[index];
        }
    }

    // 장르별로 많은 순서대로 정렬
    map<int,string> g_best_count; // 1450 classic
    for(const auto& i : genre_plays){
        g_best_count.insert(make_pair(i.second, i.first));
    }

    for (auto iter = g_best_count.rbegin(); iter != g_best_count.rend(); iter++) {
        //classic pop
        auto music = genre_index.find(iter->second)->second.rbegin();

        if(genre_index.find(iter->second)->second.size()<2){
            answer.push_back(music->second);
        } else{
            if(genre_index.find(iter->second)->second.count(music->first)>1){
                pair<map<int,int>::iterator,map<int,int>::iterator> ret;
                ret = genre_index.find(iter->second)->second.equal_range(music->first);
                auto iter = ret.first;
                answer.push_back(iter++->second);
                answer.push_back(iter->second);
            }else{
                answer.push_back(music++->second);
                answer.push_back(music->second);
            }

        }
    }

    for(auto i : answer){
        cout<<i;
    }

//    for(const auto& i:genre_index){
//        cout<<i.first<<"->"<<endl;
//        for(auto j : i.second){
//            cout<<j.first<<" :"<<j.second<<endl;
//        }
//    }

//    for(const auto& i : g_best_count){
//        cout<<i.first<<" "<<i.second<<endl;
//    }



}

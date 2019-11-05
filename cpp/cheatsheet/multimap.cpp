//
// Created by Jeongho on 2019-10-29.
//

#include <map>
#include <iostream>
#include <string>

using namespace std;

int main(){
    multimap<int,string> test;
    test.insert(make_pair(1,"one"));
    test.insert(make_pair(3,"three3"));
    test.insert(make_pair(1,"two"));
    test.insert(make_pair(2,"two2"));
    test.insert(make_pair(1,"three"));

    for (auto i:test) {
        cout<<i.second<<endl;
    }
    cout<<endl;

    for (auto it = test.find(2); it != test.end(); it++) {
        cout<<it->second<<endl;
    }
    cout<<test.count(2);
    cout<<test.count(1);

    cout << "test contains:\n";
    for (int i=0; i<4; i++)
    {
        pair <multimap<int,string>::iterator, multimap<int,string>::iterator> ret;
        ret = test.equal_range(i);
        cout << i << " =>";
        for (auto it=ret.first; it!=ret.second; ++it)
            cout << ' ' << it->second;
        cout << '\n';
    }
}

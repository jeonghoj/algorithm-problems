```cpp
#include <string>
#include <vector>
#include <set>
#include <map>

using namespace std;

int solution(vector<vector<string>> clothes) {
    
    int result=1;
    set<string> cloth_type;
    multimap<string,string> mp;
    
    for(auto i:clothes){
        cloth_type.insert(i.back());
        mp.insert(make_pair(i.back(),i.front()));
    }

    set<string>::iterator it;
    for(it = cloth_type.begin(); it != cloth_type.end(); it++){
        result*=(mp.count(*it))+1;
    }

    int answer = result-1;
    return answer;
}
```

set을 이용하여 중복없이 의류의 종류를 담았고,

map을 이용하여 의류마다 몇가지의 옷이 있는지 뽑아내었다.

종류가 3가지 A B C 라고 했을때

(A+1)(B+1)(C+1)-1

공식이 성립한다.

이유는 각 종류마다 입지 않았을때의 경우의 수 +1

그리고 문제 조건대로 아무것도 입지않았을때의 경우의 수 1개를 뺀것이다.

---
REVIEW

A B C 에서 경우의 수를 뽑으라고 했을때, 나열하여 공식을 찾아보도록하자.

A B C AB AC BC ABC -> (A+1)(B+1)(C+1)-1 의 공식이 나온다.
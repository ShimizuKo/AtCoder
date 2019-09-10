#include <bits/stdc++.h>
using namespace std;
#define ll long long

ll MOD = 1000000007;
vector<ll> fact(100005, 0);

ll pow_MOD(ll x, ll n){
  x %= MOD;
  if(n == 0) return 1;
  if(n % 2 == 0) return pow_MOD((x * x) % MOD, n / 2);
  else return (x * pow_MOD((x * x) % MOD, (n - 1) / 2)) % MOD;
}

ll P(ll n, ll k){
  if(n < k) return 0;
  if(k == 0) return 1;
  return (fact.at(n) * pow_MOD(fact.at(n - k), MOD - 2)) % MOD;
}

int main(){
  int N, K;
  cin >> N >> K;

  fact.at(0) = 1;
  for(int i = 1; i <= K + 1; i++){
    fact.at(i) = (fact.at(i - 1) * i) % MOD;
  }

  vector<vector<int>> g(100005);
  for(int i = 0; i < N - 1; i++){
    int a, b;
    cin >> a >> b;
    a--; b--;
    g.at(a).push_back(b);
    g.at(b).push_back(a);
  }

  int s = 0;
  vector<int> Q = {s};
  ll ans = 1;
  vector<bool> serched(N, false);
  serched[0] = true;

  while(Q.size() != 0){
    int v = Q.at(0);
    Q.erase(Q.begin());
    int nk = K - 2;
    int c = g.at(v).size() - 1;
    if(v == s){
      nk = K;
      c += 2;
    }
    ans *= P(nk, c) % MOD;
    for(int i : g.at(v)){
      if(serched.at(i)) continue;
      serched.at(i) = true;
      Q.push_back(i);
    }
  }
  ans %= MOD;
  cout << ans << endl;

  return 0;
}

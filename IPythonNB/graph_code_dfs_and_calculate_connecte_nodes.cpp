#include <bits/stdc++.h>
#include <algorithm>
#include <iterator>
#include <stack>
#include <sys/types.h>
 
using namespace std;
 
#define x first
#define y second
typedef long long ll;
typedef long double ld;
typedef pair<int, int> pii;
typedef unsigned long long ull;
typedef pair<ll, ll> pll;
 
#define INF 1000000000000LL

vector <ll> v[200001];
bool vis[200001];
ll a[200001];
//ll b[200001];
ll cnt1[200001];
ll h = 0;
ll cnt = 0;

void nofnodes(ll x, ll y){
    cnt1[x] = 1;
    for(ll i = 0; i < ll(v[x].size()); i++){
        ll z = v[x][i];
        if(z == y)
        continue;
        nofnodes(z, x);
        cnt1[x] += cnt1[z];
    }
}

void dfs(ll r){
    ll l = 0;
    for(ll i = 0; i < ll(v[r].size()); i++){
        ll z = v[r][i];
        if(!vis[z]){
            l = 1;
            vis[z] = 1;
            cnt += 1;
            dfs(z);
        }
    }
    if(l == 0){
        a[r] = cnt;
        cnt--;
    }else{
        a[r] = cnt;
        cnt--;
    }
}

int main(){
    ll n, k;
    cin>>n>>k;
    for(ll i = 0; i < n - 1; i++){
        ll x, y;
        cin>>x>>y;
        v[x].push_back(y);
        v[y].push_back(x);
    }
    vis[1] = true;
    dfs(1);
    nofnodes(1, 0);
    for(ll i = 1; i <= n; i++){
        a[i] = a[i] - cnt1[i] + 1;
    }
    sort(a+1, a+n+1);
    ll sum = 0;
    for(ll i = n; i > n - k; i--){
        sum += a[i];
    }
    cout<<sum<<endl;
    return 0;
}

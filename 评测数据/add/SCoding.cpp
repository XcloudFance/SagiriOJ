//SagiriOpenJudge的对拍coding标程不能出现任何的差错，出现WA,RE的话将崩溃 
#include<bits/stdc++.h>
using namespace std;
int main()
{
	freopen("sCoding.in","r",stdin);
	freopen("sCoding.out","w",stdout);
	int a,b,res;cin>>a>>b>>res;
	if(res==a+b)cout<<1;//注意这里要输出 
	else cout<<0; 
} 

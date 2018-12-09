#include<iostream>
using namespace std;
long long n,r[1000];
int main()
{
	freopen("domino.in","r",stdin);
	freopen("domino.out","w",stdout);
	cin>>n;
	r[1]=1;
	r[2]=2;
	for(int i=3;i<=n;i++)
	{
		r[i]=r[i-1]+r[i-2];
	}
	cout<<r[n];
}

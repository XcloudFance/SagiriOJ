#include<bits/stdc++.h>
#include<cstdlib>
#include<windows.h> 
int f[10001][10001];
int a[100001],s[100001];
int n;
using namespace std;
int main()
{
	freopen("unite.in","r",stdin);
	freopen("unite.out","w",stdout);
	cin>>n;
	for (int i=1;i<=n;i++) cin>>a[i];
	for (int i=1;i<=n;i++) s[i]=s[i-1]+a[i];
	memset(f,0x3f,sizeof(f));
	for (int i=1;i<=n;i++) f[i][i]=0;
	for (int i=n;i>=1;i--)
	for (int j=i+1;j<=n;j++)
	for (int k=i;k<=j-1;k++) f[i][j]=min(f[i][j],f[i][k]+f[k+1][j]+s[j]-s[i-1]);
	cout<<f[1][n];

}


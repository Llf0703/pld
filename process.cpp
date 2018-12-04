#include<bits/stdc++.h>

using namespace std;

int main()
{
    freopen("Claris.txt","r",stdin);
    freopen("pro.txt","w",stdout);
    string s;
    while (getline(cin,s))
    {
        string offi="https://www.lydsy.com/JudgeOnline/problem.php?id="+s;
        string bzojch="https://bzoj.llf0703.com/p/"+s+".html";
        string dbzoj="https://darkbzoj.cf/problem/"+s;
        cout<<"<tr>\n";
        cout<<"<td>"<<s<<"</td>\n";
        cout<<"<td><a target=\"_blank\" style=\"color:black;\" href=\""<<offi<<"\">链接</a></td>\n";
        cout<<"<td><a target=\"_blank\" style=\"color:black;\" href=\""<<bzojch<<"\">链接</a></td>\n";
        cout<<"<td><a target=\"_blank\" style=\"color:black;\" href=\""<<dbzoj<<"\">链接</a></td>\n";
        cout<<"</tr>\n";
    }
    return 0;
}
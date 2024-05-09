#include<bits/stdc++.h>
#include<iostream>
using namespace std;
int main()
{
    int n,i,j,k,mincost = 0 ,min,row,col;
    cout<<"Enter no of vertices : ";
    cin>>n;
    int visit[n];
    int cost[n][n];
    for(i = 0 ;i<n;i++)
    {
        visit[i] = 0;
    }
    for(i = 0;i<n;i++)
    {
        for(j = 0;j<n;j++)
        {
            cost[i][j] = -1;
        }
    }
    char ch;
    for(i = 0;i<n;i++)
    {
        for(j = i+1;j<n;j++)
        {
            cout<<"Do you want edge between "<<i+1<<" and "<<j+1<<endl;
            cin>>ch;
            if(ch == 'y' || ch == 'Y')
            {
                cout<<"Enter the weight : ";
                cin>>cost[i][j];
                cost[j][i] = cost[i][j];  
            }  
        }
    }
    visit[0] = 1;
    for(k = 0;k<n-1;k++)
    {
        min = 999;
        for(i = 0;i<n;i++)
        {
            for(j=0;j<n;j++)
            {
                if(visit[i] == 1 && visit[j] == 0)
                {
                    if(cost[i][j] != -1 && cost[i][j] < min)
                    {
                        min = cost[i][j];
                        row = i;
                        col = j;
                    }
                }
            }
        }
        mincost += min;
        visit[col] = 1;
        cost[row][col] = cost[col][row] = -1;
        cout<<row+1<<" -> "<<col+1<<endl;

    }
    cout<<"MIN.COST : "<<mincost<<endl;
    return 0 ;


}
#include<iostream>
#include<unordered_map>
#include<vector>
#include <string>
using namespace std;
int main() 
{
	unordered_map<string, int>graph;
	unordered_map<int, int>freq;
	int number_nodes;
	int number_edges;
	cin >> number_nodes;
	cin >> number_edges;
	for (int i = 0; i < number_edges; i++)
	{
		int u, v, w;
		cin >> u >> v >> w;
		string my_key = "";
		my_key = to_string(u) + "," + to_string(v) + "," + to_string(w);
		if (graph.count(my_key)==0)
		{
			graph[my_key] = 1;

		}
		if (freq.count(u) > 0)
		{
			freq[u]+=1;
		}
		else
			freq[u] = 1;
		if (freq.count(v) > 0)
		{
			freq[v]+=1;
		}
		else
			freq[v] = 1;
	}
	for (int i = 0; i < number_nodes; i++)
	{
		if (freq.count(i) != 0)
			cout << freq[i] << "\n";
		else
			cout << 0 << "\n";

	}
	int x;
	cin >> x;
}
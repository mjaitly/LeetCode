#include<iostream>
#include<queue>
#include<map>
#include<cassert>
#include<cstring>
#include<climits>
using namespace std;
 
int W, H, N;
 
int dx[] = {1, -1, 0, 0};
int dy[] = {0, 0, -1, 1};
 
int calc(int i, int j) {
	if(W <= H)
		return  i + W * j;
	return H * i + j;
}
 
bool get(int bitmask, int i, int j) {
	return (bitmask&(1<<calc(i,j)));
}
 
int bfs(int bitmask) {
	int dist[W][H];
	memset(dist, -1, sizeof dist);
 
	int maxDist = 0;
	queue<pair<int,int>> Q;
 
	for(int i = 0; i < W; i++)
		for(int j = 0; j < H; j++)
			if(get(bitmask, i, j)) {
				dist[i][j] = 0;
				Q.push({i, j});
			}
 	assert(Q.size() == N);
 
	while(!Q.empty()) {
		int x = Q.front().first;
		int y = Q.front().second;
		maxDist = max(maxDist, dist[x][y]);
		Q.pop();
 
		for(int d = 0; d < 4; d++) {
			int newx = x + dx[d];
			int newy = y + dy[d];
 
			if(newx >= W || newy >= H || newx < 0 || newy < 0)
				continue;
			if(dist[newx][newy] == -1) {
				dist[newx][newy] = dist[x][y] + 1;
				Q.push({newx, newy});
			}
		}
	}
 
/*	
	for(int i = 0; i < W; i++) {
		for(int j = 0; j < H; j++)
			cout << get(bitmask, i, j) << ' ';
		cout << '\n';
	}
	cerr << "^ VAL IS = " << maxDist << "\n\n";
*/
	return maxDist;
}
 
map<pair<int,int>, int> dp;
 
int solve(int bitmask, int left) {
	if(left == 0) {
		return bfs(bitmask);
	}
	if(dp.find({bitmask, left}) != dp.end()) {
		return dp[{bitmask, left}];
	}
	int minDistance = INT_MAX;
	for(int i = 0; i < W; i++)
		for(int j = 0; j < H; j++)
			if(!get(bitmask, i, j)) {
				int val = solve((bitmask|(1<<calc(i, j))), left-1);
				minDistance = min(minDistance, val);
			}
	return dp[{bitmask, left}] = minDistance;
}
 
int main() {
	while(cin >> W >> H >> N) {
		dp.clear();
		cout << solve(0, N) << '\n';
	}
}

/* 
Input
4 4 3
2 3 2
5 1 1
28 1 5
14 2 5
4 7 5
*/
/*
Output
2
1
2
3
2
2
*/
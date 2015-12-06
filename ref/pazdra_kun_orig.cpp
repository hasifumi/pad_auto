//pazdra_kun

#include <vector>
#include <cstdio>
#include <cstring>
#include <ctime>
#include <cstdlib>
#include <cmath>
#include <string>
#include <iostream>
#include <cstdint>
#include <algorithm>
#include <cassert>
#include <random>
#include <queue>
#include <list>
#include <climits>

using namespace std;

#define ROW 5
#define COL 6
#define DEPTH 7

//important param

#define PLAY 300000
#define MAX_CHAIN 900000
#define MAX_TURN 20
#define PLAYNUM 5000

const double similarity_rate = 0.8;

unsigned int rnd(int mini, int maxi);
double d_rnd(double mini, double maxi);
void init();
void fall();
void chain(int now_row, int now_col, int d, int count);
void monte_carlo();
void hill_climb();
int evalute();
int sum_evalute();
int sum_e();
int check();
void set();
void solve(int num);
void operation();
void dfs(int now_row, int now_col, int depth);
void Nbeam();
int check2(int play);
void solve2(int num);

int max_count;

int start[2];//start point
int movei[MAX_TURN][2];//move point
int goal[2];//end point

//if(index==0){y point}
int ans_start[2];//solution start point
int ans[MAX_TURN][2];//solution move point
int ans_goal[2];//solution end point
int g_turn;//solution end turn

int field[ROW][COL];
int chainflag[ROW][COL];
int t_erase[ROW][COL];
int dummy[ROW][COL];
int f_field[ROW][COL];
int fff = 0;
double save;

int max_score;

struct member{
	int start[2];//start point
	int movei[MAX_TURN][2];//move point
	int goal[2];//end point
	int score;
	int nowC;
	int nowR;
}player[3], temp, node[PLAYNUM], dum[PLAYNUM];



int main(){

	srand((unsigned)time(NULL));

	solve(5);
	//solve2(5);

	return 0;
}

// int main(int argc, char *argv[]){
//
// 	srand((unsigned)time(NULL));
//
// 	solve((int)argv[1]);
// 	//solve2(5);
//
// 	return 0;
// }
//
void solve2(int num){
	double sum = 0;
	for (int t = 0; t < num; t++){

		init();
		memcpy(f_field, field, sizeof(field));

		max_score = 0;
		dfs(0, 0, 0);

		start[0] = ans_start[0];
		start[1] = ans_start[1];
		memcpy(movei, ans, sizeof(ans));
		goal[0] = ans_goal[0];
		goal[1] = ans_goal[1];

		int rep = 0;
		save = (double)max_score;
		for (int m = 0; m < MAX_TURN; m++){
			if (movei[m][0] == -1){ rep = m; break; }
		}
		g_turn = rep;

		hill_climb();


		start[0] = ans_start[0];
		start[1] = ans_start[1];
		memcpy(movei, ans, sizeof(ans));
		goal[0] = ans_goal[0];
		goal[1] = ans_goal[1];

		memcpy(field, f_field, sizeof(f_field));

		printf("t=%d\n", t + 1);
		printf("input=\n");
		for (int row = 0; row < ROW; row++){
			for (int col = 0; col < COL; col++){
				printf("%d", field[row][col]);
			}
			printf("\n");
		}
		printf("\n");

		printf("x=%d,y=%d\n", start[1], start[0]);

		for (int i = 0; i < MAX_TURN; i++){
			if (movei[i][0] == -1 || movei[i][1] == -1){ break; }
			else{
				printf("x=%d,y=%d\n", movei[i][1], movei[i][0]);
			}
		}
		printf("x=%d,y=%d\n", goal[1], goal[0]);
		printf("\n");

		fff = 1;
		operation();
		fff = 0;
		int x = sum_evalute();
		printf("sum_evalute=%d\n", x);
		printf("\n");

		sum += (double)x;
	}

	printf("Average Combo = %lf\n", sum / (double)num);

}
void solve(int num){
	double sum = 0;
	for (int t = 0; t < num; t++){

		init();
		memcpy(f_field, field, sizeof(field));
		//monte_carlo();

		Nbeam();

		int best = 0;
		int index;
		for (int i = 0; i<PLAYNUM; i++){
			if (best<node[i].score){
				best = node[i].score;
				index = i;
			}
		}
		ans_start[0] = node[index].start[0];
		ans_start[1] = node[index].start[1];
		memcpy(ans, node[index].movei, sizeof(ans));
		ans_goal[0] = node[index].goal[0];
		ans_goal[1] = node[index].goal[1];
		start[0] = node[index].start[0];
		start[1] = node[index].start[1];
		memcpy(movei, node[index].movei, sizeof(ans));
		goal[0] = node[index].goal[0];
		goal[1] = node[index].goal[1];

		int rep = 0;
		save = (double)node[index].score;
		for (int m = 0; m < MAX_TURN; m++){
			if (movei[m][0] == -1){ rep = m; break; }
		}
		g_turn = rep;
		//hill_climb();

		start[0] = ans_start[0];
		start[1] = ans_start[1];
		memcpy(movei, ans, sizeof(ans));
		goal[0] = ans_goal[0];
		goal[1] = ans_goal[1];

		memcpy(field, f_field, sizeof(f_field));

		printf("t=%d\n", t + 1);
		printf("input=\n");
		for (int row = 0; row < ROW; row++){
			for (int col = 0; col < COL; col++){
				printf("%d", field[row][col]);
			}
			printf("\n");
		}
		printf("\n");

		printf("x=%d,y=%d\n", start[1], start[0]);

		for (int i = 0; i < MAX_TURN; i++){
			if (movei[i][0] == -1 || movei[i][1] == -1){ break; }
			else{
				printf("x=%d,y=%d\n", movei[i][1], movei[i][0]);
			}
		}
		printf("x=%d,y=%d\n", goal[1], goal[0]);
		printf("\n");

		fff = 1;
		operation();
		fff = 0;
		int x = sum_evalute();
		printf("sum_evalute=%d\n", x);
		printf("\n");

		sum += (double)x;
	}

	printf("Average Combo = %lf\n", sum / (double)num);

}

void init(){

	for (int row = 0; row < ROW; row++){
		for (int col = 0; col < COL; col++){
			field[row][col] = rnd(1, 6);
		}
	}

}

void set(){

	for (int row = 0; row < ROW; row++){
		for (int col = 0; col < COL; col++){
			if (field[row][col] == 0){ field[row][col] = rnd(1, 6); }
		}
	}

}
void fall(){
	for (int row = ROW - 1; row >= 0; row--){
		for (int col = 0; col < COL; col++){
			int check = row;
			while (1){
				if (check == ROW - 1){ break; }
				if (field[check + 1][col] == 0){
					field[check + 1][col] = field[check][col];
					field[check][col] = 0;
				}
				check++;
			}
		}
	}
}
void chain(int now_row, int now_col, int d, int count){

	if (now_row == -1 || now_row == ROW || now_col == -1 || now_col == COL){ return; }

	if (field[now_row][now_col] == d && chainflag[now_row][now_col] == 0){

		chainflag[now_row][now_col] = -1;
		if (max_count < count){ max_count = count; }
		dummy[now_row][now_col] = -1;

		chain(now_row - 1, now_col, d, count + 1);
		chain(now_row + 1, now_col, d, count + 1);
		chain(now_row, now_col - 1, d, count + 1);
		chain(now_row, now_col + 1, d, count + 1);
	}

}
int evalute(){

	int value = 0;

	memset(chainflag, 0, sizeof(chainflag));

	for (int row = 0; row < ROW; row++){
		for (int col = 0; col < COL; col++){
			if (chainflag[row][col] == 0 && field[row][col] != 0){
				max_count = 0;
				memset(dummy, 0, sizeof(dummy));
				chain(row, col, field[row][col], 1);
				if (max_count >= 3){
					if (check() == 1){ value++; }
				}
			}
		}
	}

	return value;
}
int sum_evalute(){//real_ver

	int a;
	int sum = 0;

	while (1){

		memset(t_erase, 0, sizeof(t_erase));
		a = evalute();

		if (a == 0){ break; }

		for (int row = 0; row < ROW; row++){
			for (int col = 0; col < COL; col++){
				if (t_erase[row][col] == -1){ field[row][col] = 0; }
			}
		}

		fall();
		set();

		sum += a;

	}
	return sum;

}
int sum_e(){//evalute_ver

	int a;
	int sum = 0;

	while (1){

		memset(t_erase, 0, sizeof(t_erase));
		a = evalute();

		if (a == 0){ break; }

		for (int row = 0; row < ROW; row++){
			for (int col = 0; col < COL; col++){
				if (t_erase[row][col] == -1){ field[row][col] = 0; }
			}
		}

		fall();
		sum += a;

	}
	return sum;

}


int check(){

	int v = 0;
	for (int row = 0; row < ROW; row++){
		for (int col = 0; col < COL - 2; col++){
			if (dummy[row][col] == -1 && dummy[row][col + 1] == -1 &&
				dummy[row][col + 2] == -1 && field[row][col] == field[row][col + 1] &&
				field[row][col] == field[row][col + 2]){
				t_erase[row][col] = -1;
				t_erase[row][col + 1] = -1;
				t_erase[row][col + 2] = -1;
				v = 1;
			}

		}

	}
	for (int col = 0; col < COL; col++){
		for (int row = 0; row < ROW - 2; row++){
			if (dummy[row][col] == -1 && dummy[row + 1][col] == -1 &&
				dummy[row + 2][col] == -1 && field[row][col] == field[row + 1][col] &&
				field[row][col] == field[row + 2][col]){
				t_erase[row][col] = -1;
				t_erase[row + 1][col] = -1;
				t_erase[row + 2][col] = -1;
				v = 1;
			}

		}

	}

	return v;
}

void operation(){

	int now_row = start[0], now_col = start[1];

	for (int i = 0; i < MAX_TURN; i++){
		if (movei[i][0] == -1 || movei[i][1] == -1){ break; }
		else{
			swap(field[now_row][now_col], field[movei[i][0]][movei[i][1]]);
			now_row = movei[i][0];
			now_col = movei[i][1];
		}
	}

	swap(field[now_row][now_col], field[goal[0]][goal[1]]);

	if (fff == 1){

		printf("output=\n");
		for (int row = 0; row < ROW; row++){
			for (int col = 0; col < COL; col++){
				printf("%d", field[row][col]);
			}
			printf("\n");
		}
		printf("\n");
	}


}
void monte_carlo(){

	int dx[8] = { -1, 0, 1, -1, 1, -1, 0, 1 };
	int dy[8] = { -1, -1, -1, 0, 0, 1, 1, 1 };

	int turn, ran;
	int now_row, now_col;

	double before, after, r;

	for (int i = 0; i < PLAY; i++){
		memcpy(field, f_field, sizeof(f_field));
		start[0] = rnd(0, ROW - 1);
		start[1] = rnd(0, COL - 1);
		turn = rnd(0, MAX_TURN);
		memset(movei, -1, sizeof(movei));
		now_row = start[0];
		now_col = start[1];
		for (int j = 0; j <= turn; j++){
			while (1){
				ran = rnd(0, 7);
				if (0 <= now_row + dy[ran] && now_row + dy[ran] <ROW &&
					0 <= now_col + dx[ran] && now_col + dx[ran] <COL
					){
					break;
				}

			}
			if (j < turn){
				movei[j][0] = now_row + dy[ran];
				movei[j][1] = now_col + dx[ran];
				now_row += dy[ran];
				now_col += dx[ran];
			}
			else{
				goal[0] = now_row + dy[ran];
				goal[1] = now_col + dx[ran];
			}
		}
		operation();
		if (i == 0){
			before = (double)sum_e();
		}
		else{
			after = (double)sum_e();
			r = after / before;
			if (1.0 < r){
				ans_start[0] = start[0];
				ans_start[1] = start[1];
				memcpy(ans, movei, sizeof(movei));
				ans_goal[0] = goal[0];
				ans_goal[1] = goal[1];
				g_turn = turn;
				before = after;
				save = after;
			}
		}
	}
}
void hill_climb(){

	int dx[8] = { -1, 0, 1, -1, 1, -1, 0, 1 };
	int dy[8] = { -1, -1, -1, 0, 0, 1, 1, 1 };

	int turn, ran;
	int now_row, now_col;

	double before, after, r;

	before = save;


	for (int i = 0; i < MAX_CHAIN; i++){
		memcpy(field, f_field, sizeof(f_field));
		start[0] = ans_start[0];
		start[1] = ans_start[1];
		memcpy(movei, ans, sizeof(ans));
		int st = (int)floor((double)g_turn*similarity_rate);
		turn = rnd(st, g_turn);
		now_row = ans[st - 1][0];
		now_col = ans[st - 1][1];
		for (int j = st; j <= turn; j++){
			while (1){
				ran = rnd(0, 7);
				if (0 <= now_row + dy[ran] && now_row + dy[ran] < ROW &&
					0 <= now_col + dx[ran] && now_col + dx[ran] < COL
					){
					break;
				}

			}
			if (j < turn){
				movei[j][0] = now_row + dy[ran];
				movei[j][1] = now_col + dx[ran];
				now_row += dy[ran];
				now_col += dx[ran];
			}
			else{
				goal[0] = now_row + dy[ran];
				goal[1] = now_col + dx[ran];
			}
		}
		for (int j = turn; j < MAX_TURN; j++){
			movei[j][0] = -1;
			movei[j][1] = -1;
		}
		operation();
		after = (double)sum_e();
		r = after / before;
		if (1.0 < r){
			ans_start[0] = start[0];
			ans_start[1] = start[1];
			memcpy(ans, movei, sizeof(movei));
			ans_goal[0] = goal[0];
			ans_goal[1] = goal[1];
			before = after;
		}
	}
}

void dfs(int now_row, int now_col, int depth){

	if (depth == DEPTH){

		goal[0] = now_row;
		goal[1] = now_col;

		operation();

		int score = sum_e();

		if (max_score < score){
			ans_start[0] = start[0];
			ans_start[1] = start[1];
			memcpy(ans, movei, sizeof(movei));
			ans_goal[0] = goal[0];
			ans_goal[1] = goal[1];
			max_score = score;
		}
		memcpy(field, f_field, sizeof(f_field));

		return;

	}
	else if (depth == 0){
		memset(movei, -1, sizeof(movei));
		for (int row = 0; row < ROW; row++){
			for (int col = 0; col < COL; col++){
				start[0] = row;
				start[1] = col;
				dfs(row, col, depth + 1);
			}
		}
		return;
	}
	else{

		int dx[8] = { -1, 0, 1, -1, 1, -1, 0, 1 };
		int dy[8] = { -1, -1, -1, 0, 0, 1, 1, 1 };

		movei[depth - 1][0] = now_row;
		movei[depth - 1][1] = now_col;


		for (int i = 0; i < 8; i++){
			if (0 <= now_row + dy[i] && now_row + dy[i] < ROW &&
				0 <= now_col + dx[i] && now_col + dx[i] < COL
				){
				dfs(now_row + dy[i], now_col + dx[i], depth + 1);
			}
		}
		return;
	}

}
unsigned int rnd(int mini, int maxi){
	static unsigned int x = rand() % INT_MAX;
	static unsigned int y = rand() % INT_MAX;
	static unsigned int z = rand() % INT_MAX;
	static unsigned int w = rand() % INT_MAX;
	unsigned int t;

	t = x ^ (x << 11);
	x = y; y = z; z = w;
	w = (w ^ (w >> 19)) ^ (t ^ (t >> 8));

	return (w / (UINT_MAX / ((maxi - mini) + 1))) + mini;

}
double d_rnd(double mini, double maxi){
	static unsigned int x = rand() % INT_MAX;
	static unsigned int y = rand() % INT_MAX;
	static unsigned int z = rand() % INT_MAX;
	static unsigned int w = rand() % INT_MAX;
	unsigned int t;

	t = x ^ (x << 11);
	x = y; y = z; z = w;
	w = (w ^ (w >> 19)) ^ (t ^ (t >> 8));

	return (((double)w / ((double)UINT_MAX + 1)) * (maxi - mini)) + mini;

}
void Nbeam(){

	for (int i = 0; i<PLAYNUM; i++){
		node[i].score = 0;
		for (int j = 0; j < MAX_TURN; j++){
			node[i].movei[j][0] = -1;
			node[i].movei[j][1] = -1;
		}
	}
	int size = ROW*COL;
	int cnt = 0;
	for (int i = 0; i < ROW; i++){
		for (int j = 0; j < COL; j++){
			node[cnt].start[1] = j;
			node[cnt].start[0] = i;
			node[cnt].nowC = j;
			node[cnt].nowR = i;
			cnt++;
		}
	}
	int rank;
	int dumsize;

	int dx[8] = { -1, 0, 1, -1, 1, -1, 0, 1 };
	int dy[8] = { -1, -1, -1, 0, 0, 1, 1, 1 };

	for (int i = 0; i <= MAX_TURN; i++){
		dumsize = 0;
		for (int k = 0; k < size; k++){
			for (int j = 0; j < 8; j++){
				temp = node[k];
				memcpy(field, f_field, sizeof(f_field));
				if (0 <= temp.nowC + dx[j] && temp.nowC + dx[j]<COL && 0 <= temp.nowR + dy[j] && temp.nowR + dy[j]<ROW){
					start[0] = temp.start[0];
					start[1] = temp.start[1];
					memcpy(movei, temp.movei, sizeof(movei));
					temp.nowC += dx[j];
					temp.nowR += dy[j];
					goal[0] = temp.nowR;
					goal[1] = temp.nowC;
					if (i == MAX_TURN){
						temp.goal[0] = temp.nowR;
						temp.goal[1] = temp.nowC;
					}
					else{
						temp.movei[i][0] = temp.nowR;
						temp.movei[i][1] = temp.nowC;
					}
					operation();
					temp.score = sum_e();
					if (dumsize < PLAYNUM){
						dum[dumsize] = temp;
						dumsize++;
					}
					else if (dumsize == PLAYNUM){
						rank = check2(PLAYNUM);
						if (temp.score > dum[rank].score){
							dum[rank] = temp;
						}
					}
				}
			}
		}
		for (int x = 0; x<dumsize; x++){
			node[x] = dum[x];
		}
		size = dumsize;
	}

}
int check2(int play){

	int worst = 10000;
	int index;
	for (int i = 0; i<play; i++){
		if (worst>dum[i].score){
			worst = dum[i].score;
			index = i;
		}
	}
	return index;
}

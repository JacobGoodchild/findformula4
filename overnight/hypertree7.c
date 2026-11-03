// Count labelled 2-dimensional Q-acyclic "hypertrees" (bases of the triangle matroid of K_n) with exact |H_1| histogram.
// usage: ./hypertree7 N WORKER NWORKERS   (resumable: per-prefix results appended to out_N_W.txt)
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdint.h>
typedef long long ll; typedef unsigned long long ull; typedef __int128 i128;
#define P 2147483647ULL
static int N, R, NT, K;                 // vertices, rows, triangles, target rank
static int M[64][64];                    // M[t][r]
static int tri[64][3];
static ull Bm[32][32]; static int piv[32];
static ull cnt_total; static ull hist[2048];
static int PREFIXLEN=7, W, NW; static char done[1<<12];
static FILE *fo;
static ull mulmod(ull a, ull b){ return (a*b)%P; }
static ull powmod(ull a, ull e){ ull r=1; while(e){ if(e&1) r=mulmod(r,a); a=mulmod(a,a); e>>=1;} return r; }
static int sel[32];
static ll bareiss_abs_det(int *cols){
    ll A[32][32]; int n=K;
    for(int i=0;i<n;i++) for(int j=0;j<n;j++) A[i][j]=M[cols[j]][i];
    ll prev=1; int sign=1;
    for(int k=0;k<n-1;k++){
        if(A[k][k]==0){ int s=-1; for(int i=k+1;i<n;i++) if(A[i][k]!=0){s=i;break;} if(s<0) return 0;
            for(int j=0;j<n;j++){ ll t=A[k][j];A[k][j]=A[s][j];A[s][j]=t;} sign=-sign; }
        for(int i=k+1;i<n;i++) for(int j=k+1;j<n;j++){ i128 v=(i128)A[i][j]*A[k][k]-(i128)A[i][k]*A[k][j]; A[i][j]=(ll)(v/prev); }
        prev=A[k][k];
    }
    ll d=A[n-1][n-1]; return d<0?-d:d;
}
static ull cur_prefix_id; static int cur_active;
static ull local_cnt; static ull local_hist[2048];
static void dfs(int i,int k,ull pid){
    if(k==K){ local_cnt++; ll d=bareiss_abs_det(sel); if(d>2047) d=2047; local_hist[d]++; return; }
    if(i==NT) return;
    if(NT-i < K-k) return;
    if(i==PREFIXLEN){                      // entering the free part: handle prefix scheduling once per prefix
        if(!cur_active){
            if((pid%NW)!=(ull)W || done[pid]) return;
            cur_active=1; cur_prefix_id=pid; local_cnt=0; memset(local_hist,0,sizeof local_hist);
            dfs(i,k,pid);
            fprintf(fo,"%llu %llu",pid,local_cnt); for(int h=0;h<2048;h++) if(local_hist[h]) fprintf(fo," %d:%llu",h,local_hist[h]); fprintf(fo,"\n"); fflush(fo);
            cur_active=0; return;
        }
    }
    // include column i if independent
    ull v[32]; for(int r=0;r<R;r++){ ll x=M[i][r]; v[r]=(x%(ll)P+P)%P; }
    for(int j=0;j<k;j++){ ull c=v[piv[j]]; if(c){ ull m=P-c; for(int r=0;r<R;r++) if(Bm[j][r]) v[r]=(v[r]+mulmod(m,Bm[j][r]))%P; } }
    int p=-1; for(int r=0;r<R;r++) if(v[r]){p=r;break;}
    if(p>=0){
        ull inv=powmod(v[p],P-2); for(int r=0;r<R;r++) v[r]=mulmod(v[r],inv);
        memcpy(Bm[k],v,sizeof(ull)*R); piv[k]=p; sel[k]=i;
        dfs(i+1,k+1,i<PREFIXLEN? (pid|(1ULL<<i)):pid);
    }
    dfs(i+1,k,pid);
}
int main(int argc,char**argv){
    N=atoi(argv[1]); W=atoi(argv[2]); NW=atoi(argv[3]);
    // rows: edges among vertices 1..N-1 ; triangles: all 3-subsets of 0..N-1
    int eid[16][16]; R=0; for(int a=1;a<N;a++) for(int b=a+1;b<N;b++) eid[a][b]=R++;
    NT=0; for(int a=0;a<N;a++) for(int b=a+1;b<N;b++) for(int c=b+1;c<N;c++){ tri[NT][0]=a;tri[NT][1]=b;tri[NT][2]=c;
        memset(M[NT],0,sizeof M[NT]);
        if(b>=1) M[NT][eid[b][c]]+= 1;      // edge (b,c) coeff +1
        if(a>=1) { M[NT][eid[a][c]]+=-1; M[NT][eid[a][b]]+=1; }
        NT++; }
    K=R;
    if(PREFIXLEN>NT) PREFIXLEN=NT;
    char fn[64]; sprintf(fn,"out_%d_%d.txt",N,W);
    FILE*fi=fopen(fn,"r"); if(fi){ char line[1<<14]; while(fgets(line,sizeof line,fi)){ ull pid; if(sscanf(line,"%llu",&pid)==1) done[pid]=1; } fclose(fi); }
    fo=fopen(fn,"a");
    cur_active=0; dfs(0,0,0);
    fprintf(fo,"FINISHED\n"); fclose(fo); return 0;
}

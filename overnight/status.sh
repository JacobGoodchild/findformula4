#!/bin/bash
# Cheap supervisor: prints compact status, relaunches any dead/unfinished job (all jobs are resumable). Usage: bash status.sh
cd /home/user/findformula4/overnight
echo "time $(date -u +%H:%M) UTC"
# --- hypertree7 workers
for w in 0 1 2 3; do
  if grep -q FINISHED out_7_$w.txt 2>/dev/null; then s=done
  elif ps -eo args | grep -Eq "^./hypertree7 7 $w 4$"; then s=running
  else s=RELAUNCH; nohup ./hypertree7 7 $w 4 >> ht7_$w.log 2>&1 & fi
  echo "hypertree7 worker $w: $s"
done
python3 - <<'PY'
import glob,collections
tot=0;h=collections.Counter();pre=0
for f in glob.glob('out_7_*.txt'):
    for l in open(f):
        if l.startswith('FIN'): continue
        p=l.split(); tot+=int(p[1]); pre+=1
        for t in p[2:]:
            a,b=t.split(':'); h[int(a)]+=int(b)
print('hypertree7: prefixes',pre,'bases',tot,'|H| hist',dict(sorted(h.items())))
PY
# --- relation miners
for spec in "7 0" "7 1" "8 0"; do set -- $spec; log=relminer_$1$([ $2 = 1 ] && echo x).log
  if grep -q "^verified on all" $log 2>/dev/null; then echo "relminer n=$1 extra=$2: done ($(grep -c . $log) lines)"
  elif ps -eo args | grep -q "[r]elminer.py $1\( $2\)\?$" >/dev/null; then echo "relminer n=$1 extra=$2: running"
  else echo "relminer n=$1 extra=$2: RELAUNCH"; nohup python3 relminer.py $1 $2 > $log 2>&1 & fi
done
if [ ! -f candidates/ineq.txt ] && [ -f inv_8.pkl ] && ls inv_5.pkl inv_6.pkl >/dev/null 2>&1; then nohup python3 ineqminer.py > ineqminer.log 2>&1 & echo "ineqminer launched"; fi
[ -f candidates/ineq.txt ] && head -1 candidates/ineq.txt

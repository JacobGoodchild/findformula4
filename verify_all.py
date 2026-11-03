# Re-runs the scans that back statements in IDEAS.md (no theorem claims yet).
import subprocess, sys
for p in ["results/graphs_explore/scan.py","results/graphs_explore/rel.py"]:
    print("running",p); subprocess.run([sys.executable,p],check=True,cwd=__file__.rsplit("/",1)[0] or ".")

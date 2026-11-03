# Re-runs the exact/numeric checks behind the claims in results.md and IDEAS.md.
import subprocess, sys, os
here=os.path.dirname(os.path.abspath(__file__))
for p in ["results/resistance_simplex/cm.py","results/resistance_simplex/exact_circ.py",
          "results/resistance_simplex/exact_C.py","results/circumsphere/ub.py","results/random_target/mom.py"]:
    print("== running",p,flush=True)
    subprocess.run([sys.executable,os.path.join(here,p)],check=True,cwd=os.path.dirname(os.path.join(here,p)))
print("all checks completed")

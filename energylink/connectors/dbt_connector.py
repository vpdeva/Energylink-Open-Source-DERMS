
import os
import subprocess

def run_dbt_transformations(project_dir):
    """Run DBT transformations in the given project directory."""
    os.chdir(project_dir)
    subprocess.run(["dbt", "run"])
            
#!/usr/bin/env python3

import os
import subprocess
from multiprocessing import Pool

def run(task):
  # Do something with task here
  subprocess.call(task)


if __name__ == "__main__":
    src = "/data/prod/"         
    dest = "/data/prod_backup/" 
    tasks = []

   # Traverse the directory tree and prepare rsync for each file
    for dirpath, dirnames, filenames in os.walk(src):
        rel_dir = os.path.relpath(dirpath, src)
        dest_dir = os.path.join(dest, rel_dir)
        os.makedirs(dest_dir, exist_ok=True)
        for filename in filenames:
            src_file = os.path.join(dirpath, filename)
            dest_file = os.path.join(dest_dir, filename)
            # Prepare rsync command for each file
            tasks.append(["rsync", "-a", src_file, dest_file])

    # Use a pool of workers to copy files in parallel
    with Pool() as p:
        p.map(run, tasks)
 
    


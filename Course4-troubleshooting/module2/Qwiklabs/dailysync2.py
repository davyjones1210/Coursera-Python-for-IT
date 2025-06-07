#!/usr/bin/env python3

import os
import subprocess
from multiprocessing import Pool

def run(pair):
    src_dir, dest_dir = pair
    subprocess.call(["rsync", "-arq", src_dir, dest_dir])

if __name__ == "__main__":
    src_root = os.path.abspath("data/prod")
    dest_root = os.path.abspath("data/prod_backup")

    # List all top-level directories in /data/prod
    subdirs = [d for d in os.listdir(src_root) if os.path.isdir(os.path.join(src_root, d))]
    tasks = []
    for subdir in subdirs:
        src_dir = os.path.join(src_root, subdir) + "/"      # Ensure trailing slash for rsync
        dest_dir = os.path.join(dest_root, subdir) + "/"
        tasks.append((src_dir, dest_dir))

    # Use a pool of workers to sync each top-level directory in parallel
    with Pool(len(tasks)) as p:
        p.map(run, tasks)
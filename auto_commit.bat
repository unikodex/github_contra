@echo off

cd /d C:\Path\To\Repository

python update_counter.py

git add counter.txt history.log
git commit -m "Daily update"

git push origin main
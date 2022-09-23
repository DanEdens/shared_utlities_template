cd ..
type groups.py > Archive/groups.bak.py
type exclude.dat > Archive/exclude.bak.dat
git fetch
git switch --discard-changes production
git pull

cd ..
echo %CD%
git stash
git fetch
git pull
git checkout production
git stash apply
type devicelist.txt > Archive/devicelist.txt
REM type exclude.dat > Archive/exclude.bak.dat
echo %DATE% >> ../Archive/commit.log
git add . >> ../Archive/commit.log
if "%*" == "" goto :auto
GOTO :comment


:auto
set /p comment="Enter Brief comment: "
git commit -m "Update from %USERNAME%: %comment%" >> ../Archive/commit.log
echo ------------------- >> ../Archive/commit.log
git add ../Archive/commit.log
git commit -m "update Log"
goto :end


:comment
git commit -m "%*" >> ../Archive/commit.log
git commit -m "Update from %USERNAME%: %*" >> ../Archive/commit.log
echo ------------------- >> ../Archive/commit.log
git add ../Archive/commit.log
git commit -m "update Log"
goto :end

:end
git push -f >> ../Archive/commit.log

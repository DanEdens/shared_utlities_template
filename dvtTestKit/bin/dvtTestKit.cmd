REM dvtTestKit Entry
SET arg_makedoc=
SET arg_post=
FOR %%i IN (%*) DO (
  IF "%%i"=="--makedoc" SET arg_makedoc=1
  IF "%%i"=="--post" SET arg_post=1
)
IF DEFINED arg_makedoc (
  shift
  python dvttestkit/confluence_handler.py %*
) ELSE IF DEFINED arg_post (
  REM Call post.py with the arguments after "--post"
  shift
  python post.py %*
) ELSE (
  python dvttestkit/confluence_handler.py %*
)

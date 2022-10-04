call rost DVT/Jenkins/%0 %TIME% Running from "%cd%\\%0" 
es -r Jenkinsfile_* |grep cdroutertestkit > jenkinsCensus.txt

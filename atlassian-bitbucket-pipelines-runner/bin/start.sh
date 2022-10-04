#!/bin/sh

while true
do
  case $1 in
    -a|--accountUuid) shift; ACCOUNT_UUID="$1";;
    -r|--repositoryUuid) shift; REPOSITORY_UUID="$1";;
    -u|--runnerUuid) shift; RUNNER_UUID="$1";;
    -i|--OAuthClientId) shift; OAUTH_CLIENT_ID="$1";;
    -s|--OAuthClientSecret) shift; OAUTH_CLIENT_SECRET="$1";;
    -w|--workingDirectory) shift; WORKING_DIRECTORY="$1";;
    -e|--runnerEnvironment) shift; RUNNER_ENVIRONMENT="$1";;
    -t|--runtime) shift; RUNTIME="$1";;
    -k|--dockerUri) shift; DOCKER_URI="$1";;
    -d|--scheduledStateUpdateInitialDelaySeconds) shift; SCHEDULED_STATE_UPDATE_INITIAL_DELAY_SECONDS="$1";;
    -p|--scheduledStateUpdatePeriodSeconds) shift; SCHEDULED_STATE_UPDATE_PERIOD_SECONDS="$1";;
    -c|--cleanupPreviousFolders) shift; CLEANUP_PREVIOUS_FOLDERS="$1";;
    *) break
    ;;
  esac
  shift
done

ACCOUNT_UUID=${ACCOUNT_UUID:?'--accountUuid is required.'}
RUNNER_UUID=${RUNNER_UUID:?'--runnerUuid is required.'}
OAUTH_CLIENT_ID=${OAUTH_CLIENT_ID:?'--OAuthClientId is required.'}
OAUTH_CLIENT_SECRET=${OAUTH_CLIENT_SECRET:?'--OAuthClientSecret is required.'}
WORKING_DIRECTORY=${WORKING_DIRECTORY:?'--workingDirectory is required.'}
RUNTIME=${RUNTIME:?'--runtime is required.'}
REPOSITORY_UUID=${REPOSITORY_UUID:-''}
RUNNER_ENVIRONMENT=${RUNNER_ENVIRONMENT:-PRODUCTION}
DOCKER_URI=${DOCKER_URI:-''}
SCHEDULED_STATE_UPDATE_INITIAL_DELAY_SECONDS=${SCHEDULED_STATE_UPDATE_INITIAL_DELAY_SECONDS:-0}
SCHEDULED_STATE_UPDATE_PERIOD_SECONDS=${SCHEDULED_STATE_UPDATE_PERIOD_SECONDS:-30}
CLEANUP_PREVIOUS_FOLDERS=${CLEANUP_PREVIOUS_FOLDERS:-false}

java -version 2> /dev/null
if [ $? -ne 0 ]
then
  echo 'Java not installed'
  exit 1
fi

exec java \
  -jar \
  -Dbitbucket.pipelines.runner.account.uuid=$ACCOUNT_UUID \
  -Dbitbucket.pipelines.runner.repository.uuid=$REPOSITORY_UUID \
  -Dbitbucket.pipelines.runner.uuid=$RUNNER_UUID \
  -Dbitbucket.pipelines.runner.oauth.client.id=$OAUTH_CLIENT_ID \
  -Dbitbucket.pipelines.runner.oauth.client.secret=$OAUTH_CLIENT_SECRET \
  -Dbitbucket.pipelines.runner.directory.working=$WORKING_DIRECTORY \
  -Dbitbucket.pipelines.runner.environment=$RUNNER_ENVIRONMENT \
  -Dbitbucket.pipelines.runner.runtime=$RUNTIME \
  -Dbitbucket.pipelines.runner.docker.uri=$DOCKER_URI \
  -Dbitbucket.pipelines.runner.scheduled.state.update.initial.delay.seconds=$SCHEDULED_STATE_UPDATE_INITIAL_DELAY_SECONDS \
  -Dbitbucket.pipelines.runner.scheduled.state.update.period.seconds=$SCHEDULED_STATE_UPDATE_PERIOD_SECONDS \
  -Dbitbucket.pipelines.runner.cleanup.previous.folders=$CLEANUP_PREVIOUS_FOLDERS \
  -Dfile.encoding=UTF-8 \
  -Dsun.jnu.encoding=UTF-8 \
  ./runner.jar

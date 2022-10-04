Atlassian Bitbucket Pipelines Runner
======================

About
----------------------
Bitbucket Pipelines Runner

A self-hosted runner that allows you to execute pipelines steps on your own infrastructure.

Quick Installation
----------------------
Requirements:

* OpenJDK 11+ (Java)
* Git 2.2.0+

Extra requirements for Windows Runner:

* Window Server 2019 or above
* PowerShell 5+

### Linux Docker
Use the command provided in the pipelines UI to launch the runner:

Example:
```shell
docker container run -it \
-v /tmp:/tmp -v /var/run/docker.sock:/var/run/docker.sock \
-v /var/lib/docker/containers:/var/lib/docker/containers:ro \ 
-e ACCOUNT_UUID="${ACCOUNT_UUID}" \
-e REPOSITORY_UUID="${REPOSITORY_UUID}" \
-e RUNNER_UUID="${RUNNER_UUID}" \ 
-e RUNTIME_PREREQUISITES_ENABLED=true \
-e OAUTH_CLIENT_ID="${OAUTH_CLIENT_ID}" \
-e OAUTH_CLIENT_SECRET="${OAUTH_CLIENT_SECRET}" \
-e WORKING_DIRECTORY=/tmp \
--name "${RUNNER_NAME}" docker-public.packages.atlassian.com/sox/atlassian/bitbucket-pipelines-runner:1
```

### Windows Powershell
1. Open Powershell in admin mode.
2. Go to the <runner installation directory>\bin folder.
3. Use the command provided in the pipelines UI to launch the runner:

	```powershell
	.\start.ps1 -accountUuid "$Env:ACCOUNT_UUID" ` 
	-repositoryUuid "$Env:REPOSITORY_UUID" `
	-runnerUuid "$Env:RUNNER_UUID" `
	-OAuthClientId "$Env:OAUTH_CLIENT_ID" `
	-OAuthClientSecret "$Env:OAUTH_CLIENT_SECRET" `
	-workingDirectory "..\temp"
	```

### Mac OS

1. Open the terminal.
2. Decompress the tar.gz or zip file.
3. Go to the <runner installation directory>\bin folder.
4. Grant execution permission to `start.sh` file:
```bash
chmod +x start.sh
```
5. Use the command provided in the pipelines UI to launch the runner:

Example:
```shell
./start.sh --runtime macos-bash \
  --accountUuid "${ACCOUNT_UUID}" \
  --repositoryUuid "${REPOSITORY_UUID}" \
  --runnerUuid "${RUNNER_UUID}" \
  --OAuthClientId "${OAUTH_CLIENT_ID}" \
  --OAuthClientSecret "${OAUTH_CLIENT_SECRET}" \
  --workingDirectory "..\temp"
```

### Linux Shell

1. Open the terminal.
2. Decompress the tar.gz or zip file.
3. Go to the <runner installation directory>\bin folder.
4. Grant execution permission to `start.sh` file:
```bash
chmod +x start.sh
```
5. Use the command provided in the pipelines UI to launch the runner:

Example:
```shell
./start.sh --runtime linux-shell \
  --accountUuid "${ACCOUNT_UUID}" \
  --repositoryUuid "${REPOSITORY_UUID}" \
  --runnerUuid "${RUNNER_UUID}" \
  --OAuthClientId "${OAUTH_CLIENT_ID}" \
  --OAuthClientSecret "${OAUTH_CLIENT_SECRET}" \
  --workingDirectory "..\temp"
```

Documentation
----------------------
TBD

Licensing
----------------------
(c) Atlassian 2022. This software contains in part open sourced libraries. See licenses-and-attributions.txt and the associated licenses folder for details. This software is covered by the Atlassian Software License Agreement.

For details of licensing and privacy policy, see https://www.atlassian.com/legal/software-license-agreement and https://www.atlassian.com/legal/privacy-policy.
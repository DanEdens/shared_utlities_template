param (
    [string]$accountUuid = $(throw "-accountUuid is required."),
    [string]$repositoryUuid = "",
    [string]$runnerUuid = $(throw "-runnerUuid is required."),
    [string]$OAuthClientId = $(throw "-OAuthClientId is required."),
    [string]$OAuthClientSecret = $(throw "-OAuthClientSecret is required."),
    [string]$workingDirectory = $(throw "-workingDirectory is required."),
    [string]$runnerEnvironment = "PRODUCTION",
    [string]$scheduledStateUpdateInitialDelaySeconds = "0",    
    [string]$scheduledStateUpdatePeriodSeconds = "30",
    [string]$cleanupPreviousFolders = "false"
)

if (-not (Get-Command -name "java" -CommandType Application -errorAction SilentlyContinue))
{
    Write-Error "Java not installed"
    break
}


$argList = @("-jar",
            "-Dbitbucket.pipelines.runner.account.uuid=$accountUuid",
            "-Dbitbucket.pipelines.runner.repository.uuid=$repositoryUuid",
            "-Dbitbucket.pipelines.runner.uuid=$runnerUuid",
            "-Dbitbucket.pipelines.runner.environment=$runnerEnvironment",
            "-Dbitbucket.pipelines.runner.oauth.client.id=$OAuthClientId",
            "-Dbitbucket.pipelines.runner.oauth.client.secret=$OAuthClientSecret",
            "-Dbitbucket.pipelines.runner.directory.working=$workingDirectory",
            "-Dbitbucket.pipelines.runner.runtime=windows-powershell",
            "-Dbitbucket.pipelines.runner.scheduled.state.update.initial.delay.seconds=$scheduledStateUpdateInitialDelaySeconds",
            "-Dbitbucket.pipelines.runner.scheduled.state.update.period.seconds=$scheduledStateUpdatePeriodSeconds",
            "-Dbitbucket.pipelines.runner.cleanup.previous.folders=$cleanupPreviousFolders"
            "-Dfile.encoding=UTF-8",
            "-Dsun.jnu.encoding=UTF-8",
            "./runner.jar")

$params = @{
    FilePath = "java"
    ArgumentList = $argList
}

$p = Start-Process @params -NoNewWindow -Wait


curl --location --request POST 'https://your-domain.atlassian.net/rest/api/3/issue/TEST-123/attachments'
 -u 'email@example.com:<api_token>'
 -H 'X-Atlassian-Token: no-check'
 --form 'file=@"myfile.txt"'

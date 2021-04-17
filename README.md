# v2ray-plugin_Automatic
No need to remember the long command, just fillout the CSV and launch it :)

## How to
By execute:
```SHELL
$ python vpa.py v2ray-plugin vp-profile.csv
```
To get the result:
```
v2ray-plugin -localAddr 127.0.0.1 -server -host yourdomain.com -path /app -localPort 8389 -remotePort 8388
v2ray-plugin -localAddr 0.0.0.0 -localPort 1080 -remoteAddr yourdomain.com -remotePort 443 -host yourdomain.com -path /app -tls
```

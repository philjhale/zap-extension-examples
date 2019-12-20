# OWASP ZAP hooks example

This is an example of adding a HTTP header to all ZAP requests using a hook which loads a script. Doesn't currently work.


Comand to execute ZAP using the `hooks.py` file.
```
docker run --rm -v $(pwd):/zap/wrk/:rw \
-t owasp/zap2docker-stable zap-baseline.py -d -t http://docker.for.mac.localhost:3000 \
--hook=/zap/wrk/hooks.py
```

Example output.

```
2019-12-20 11:31:32,247 Target: http://docker.for.mac.localhost:3000
2019-12-20 11:31:32,255 Trigger hook: cli_opts, args: 1
2019-12-20 11:31:32,255 Using port: 56710
2019-12-20 11:31:32,255 Trigger hook: start_zap, args: 2
2019-12-20 11:31:32,255 Starting ZAP
2019-12-20 11:31:32,255 Params: ['zap-x.sh', '-daemon', '-port', '56710', '-host', '0.0.0.0', '-config', 'api.disablekey=true', '-config', 'api.addrs.addr.name=.*', '-config', 'api.addrs.addr.regex=true', '-config', 'spider.maxDuration=1', '-addonupdate', '-addoninstall', 'pscanrulesBeta']
2019-12-20 11:31:32,260 Starting new HTTP connection (1): localhost:56710
_XSERVTransmkdir: ERROR: euid != 0,directory /tmp/.X11-unix will not be created.
2019-12-20 11:31:33,264 Starting new HTTP connection (1): localhost:56710
2019-12-20 11:31:34,268 Starting new HTTP connection (1): localhost:56710
Dec 20, 2019 11:31:34 AM java.util.prefs.FileSystemPreferences$1 run
INFO: Created user preferences directory.
2019-12-20 11:31:35,270 Starting new HTTP connection (1): localhost:56710
2019-12-20 11:31:36,273 Starting new HTTP connection (1): localhost:56710
2019-12-20 11:31:37,277 Starting new HTTP connection (1): localhost:56710
2019-12-20 11:31:38,258 Starting new HTTP connection (1): localhost:56710
2019-12-20 11:31:39,261 Starting new HTTP connection (1): localhost:56710
2019-12-20 11:31:40,265 Starting new HTTP connection (1): localhost:56710
2019-12-20 11:31:41,268 Starting new HTTP connection (1): localhost:56710
2019-12-20 11:31:42,271 Starting new HTTP connection (1): localhost:56710
2019-12-20 11:31:43,275 Starting new HTTP connection (1): localhost:56710
2019-12-20 11:31:44,278 Starting new HTTP connection (1): localhost:56710
2019-12-20 11:31:44,316 http://localhost:56710 "GET http://zap/JSON/core/view/version/ HTTP/1.1" 200 19
2019-12-20 11:31:44,318 ZAP Version 2.8.0
2019-12-20 11:31:44,318 Took 12 seconds
2019-12-20 11:31:44,318 Trigger hook: zap_started, args: 2
2019-12-20 11:31:44,318 ***********CALLED HOOK**********
2019-12-20 11:31:44,320 Starting new HTTP connection (1): localhost:56710
2019-12-20 11:31:44,325 http://localhost:56710 "GET http://zap/JSON/script/action/load/?scriptEngine=jython&scriptName=add_header.py&scriptType=httpsender&apikey=&fileName=%2Fzap%2Fwrk%2Fadd_header.py HTTP/1.1" 400 52
2019-12-20 11:31:44,326 Starting new HTTP connection (1): localhost:56710
2019-12-20 11:31:44,330 http://localhost:56710 "GET http://zap/JSON/script/action/enable/?scriptName=add_header.py&apikey= HTTP/1.1" 400 52
2019-12-20 11:31:44,331 ***************Loaded: add_header.py - Does Not Exist
2019-12-20 11:31:44,331 Trigger hook: zap_access_target, args: 2
...
```
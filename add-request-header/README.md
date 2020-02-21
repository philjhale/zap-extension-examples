# Add request header

This is an example of adding a HTTP header to all ZAP requests using a hook which loads a script.

Command to execute ZAP using the `hooks.py` file.
```
docker run --rm -v $(pwd):/zap/wrk/:rw \
-t owasp/zap2docker-stable zap-baseline.py -d -t https://public-firing-range.appspot.com/ \
--hook=/zap/wrk/hooks.py
```

# Links

* [Hook docs](https://github.com/zaproxy/zaproxy/blob/develop/docker/docs/scan-hooks.md)
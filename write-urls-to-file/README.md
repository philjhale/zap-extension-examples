# Writing URLs to a file

This is an example of how to write the URLs discovered by the spider to a file.

Command to execute ZAP using the `hooks.py` file.
```
docker run --rm -v $(pwd):/zap/wrk/:rw \
-t owasp/zap2docker-stable zap-baseline.py -d -t https://public-firing-range.appspot.com/ \
--hook=/zap/wrk/hooks.py
```

# Links

* [Hook docs](https://github.com/zaproxy/zaproxy/blob/develop/docker/docs/scan-hooks.md)
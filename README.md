# OWASP ZAP hooks example

This is an example of adding a HTTP header to all ZAP requests using a hook which loads a script.


Comand to execute ZAP using the `hooks.py` file.
```
docker run --rm -v $(pwd):/zap/wrk/:rw \
-t owasp/zap2docker-stable zap-baseline.py -d -t http://docker.for.mac.localhost:3000 \
--hook=/zap/wrk/hooks.py
```
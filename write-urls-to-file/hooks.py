def zap_pre_shutdown(zap):
    # The base directory is hardcoded in this hook. This is fairly safe if running in Docker
    # as the value hardcoded in the source code https://github.com/zaproxy/zaproxy/blob/d91db825c988f2be808738983360fd31731815fd/docker/zap-baseline.py#L219
    # If running in another environment this probably won't work
    with open('/zap/wrk/urls.txt', mode='w') as file:
        file.write('\n'.join(zap.core.urls()))
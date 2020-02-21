import logging

# Script loading example https://github.com/zaproxy/zaproxy/blob/d91db825c988f2be808738983360fd31731815fd/docker/zap-api-scan.py#L353
def zap_started(zap, target):
    logging.debug("*********** zap_started hook")
    # Install the Python script engine as it's not installed by default
    response = zap.autoupdate.install_addon("jython")
    logging.debug("*************** Installed Python script engine add on - " + response)
    # Load and enable script
    response = zap.script.load("add_header.py", "httpsender", "jython", "/zap/wrk/add_header.py")
    zap.script.enable("add_header.py")
    logging.debug("*************** Loaded script add_header.py - " + response)
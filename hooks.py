import logging

# Script loading example https://github.com/zaproxy/zaproxy/blob/d91db825c988f2be808738983360fd31731815fd/docker/zap-api-scan.py#L353
def zap_started(zap, target):
    logging.debug("***********CALLED HOOK**********")
    response = zap.script.load("add_header.py", "httpsender", "jython", "/zap/wrk/add_header.py")
    zap.script.enable("add_header.py")
    logging.debug("***************Loaded: add_header.py - " + response)


# Some example code

# def add_proxy_scripts(zap):
# script_dir = os.path.join(os.path.dirname(os.path.realpath(__file__)), "proxy_scripts")
# for script in os.listdir(script_dir):
# 	filename = os.path.join(script_dir, script)
# 	# Note: scriptDescription parameter is required - API bug
# 	zap.script.load(script, "proxy", "ECMAScript : Oracle Nashorn", filename, "")
# 	response = zap.script.enable(script)
# 	logging.debug("Loaded: " + filename + " - " + response)


# zap.script.load('Alert_on_HTTP_Response_Code_Errors.js', 'httpsender', 'Oracle Nashorn', '/home/zap/.ZAP_D/scripts/scripts/httpsender/Alert_on_HTTP_Response_Code_Errors.js')
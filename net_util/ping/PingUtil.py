from concurrent.futures.thread import ThreadPoolExecutor
import subprocess
from subprocess import DEVNULL
import platform

# from util import PingUtil

PING_COMMAND = 'ping'
PING_COUNT = '1'
NO_OF_PROCESS = 300


# def getPingStatus(ip):
#     flag = isIPReachable(ip)
#     formattedOut = '%16s : %s' % (ip, flag)
#     return formattedOut


def getPingResponse(ip):
    flag = isPingOk(ip)
    # formattedOut = '%s:%s' % (ip, flag)
    # print("Format : ", formattedOut)
    # return formattedOut
    responseDict = {ip: flag}
    return responseDict;


def isPingOk(sHost):
    try:
        output = subprocess.check_output(
            "ping -{} 1 {}".format('n' if platform.system().lower() == "windows" else 'c', sHost), shell=True)
    except Exception as e:
        return False

    return True

def getAllPingStatusList(ips):
    executor = ThreadPoolExecutor(NO_OF_PROCESS)
    results = executor.map(getPingResponse, ips)
    datalist = list(results)
    return datalist;


# def pingAllIPs(ips):
#     executor = ThreadPoolExecutor(NO_OF_PROCESS)
#     results = executor.map(getPingStatus(), ips)
#     dataList = list(results)
#     for i in dataList:
#         print(i)


def isIPReachable(ipAddress):
    param = '-n' if platform.system().lower() == 'windows' else '-c'
    pingCmdArgs = [PING_COMMAND, param, PING_COUNT, ipAddress]

    # process = subprocess.Popen(pingCmdArgs, stdout=DEVNULL, stderr=DEVNULL)
    # out, error = process.communicate()
    # responseCode = process.returncode
    # print("============= Coming here =========",responseCode)
    # return (responseCode == 0)
    return subprocess.call(pingCmdArgs) == 0


def isIPReachableVerbose(ipAddress):
    param = '-n' if platform.system().lower() == 'windows' else '-c'
    command = [PING_COMMAND, param, PING_COUNT, ipAddress]
    return subprocess.call(command) == 0


def formatIPReachability(ipAddress, status):
    formattedOut = '%16s : %b' % (ipAddress, status)
    return formattedOut

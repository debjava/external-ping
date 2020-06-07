import argparse
import json

from net_util.ping import PingUtil

argParser = argparse.ArgumentParser()


def define_arguments():
    argParser.add_argument('-p', '--ping', nargs="+", help="Ping IP Addresses.")
    argParser.add_argument('-t', '--telnet', nargs="+", help="Telnet command")


def run_command():
    define_arguments()
    parsedargs = argParser.parse_args()
    argsDict = parsedargs.__dict__

    if parsedargs.ping:
        print("It is ping")
        commandName = "ping"
        argList = argsDict.get(commandName)
        ipString = argList[0];
        ips = ipString.split(',')
        print("All IPs: ", ips)
        resultList = PingUtil.getAllPingStatusList(ips)
        print("Result List:", resultList)
        str = json.dumps(resultList);
        print("In json format .....")
        print(str)
    elif parsedargs.telnet:
        print("It is Telnet")
        commandName = "telnet"


if __name__ == '__main__':
    run_command()

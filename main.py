import argparse

from ping import PingUtil


def hello():
    argParser = argparse.ArgumentParser()
    argParser.add_argument('-p', '--ping', nargs= "+", help="Ping IP Addresses.")
    argParser.add_argument('-t', '--telnet', nargs="+", help="Telnet command")

    args = argParser.parse_args()
    # print('Result:', vars(args)) # All passed arguments
    paramDict = args.__dict__
    commandName = None
    # print("Now Ping values : ",paramDict.get("ping"))
    # print("Arguments passed: ",paramDict.keys())
    if args.ping:
        print("It is ping")
        commandName = "ping"
        argList = paramDict.get(commandName)
        ipString = argList[0];
        ips = ipString.split(',')
        print("All IPs: ", ips)
        PingUtil.pingAllIPs(ips)
        # print("Now Ping values : ", paramDict.get("ping"))
        # for arg in argList:
        #     print("Argument value: ", arg)
    elif args.telnet:
        print("It is Telnet")
        commandName = "telnet"
        # print("Now Telnet values : ", paramDict.get("telnet"))

    # argList = paramDict.get(commandName)
    # for arg in argList:
    #     print("Argument value: ", arg)

    # if "ping" in paramDict:
    #     print('you have to ping IP address')
    #     print(vars(args).values())
    #     print("Now Actual Passed Ping values : ", paramDict.get("ping"))
    # elif "telnet" in paramDict:
    #     print("You have to perform telenet validations")
    #     argList = vars(args).values()
    #     for val in argList:
    #         print("Value as argument: ", val)

    # if args.ping == 'someip':
    #     print("=====================")
    #     print('you have to ping IP address')
    #     print(vars(args).values())
    #     # for arg in vars(args):
    #     #     print("Argument passed: ", arg)
    # print("Hello World")

if __name__ == '__main__':
    hello()
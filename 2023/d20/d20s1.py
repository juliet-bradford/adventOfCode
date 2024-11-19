
import queue

class PulseModule:
    def __init__(self, _t: str, _d: list[str]):
        self.typeName = _t
        self.destModuleNames = _d
        self.on = False
        self.memory = {}
    typeName: str
    destModuleNames: list[str]
    on: bool
    memory: dict[str, str]

def printModules(modulesDict: dict[str, PulseModule]):
    for key in modulesDict:
        print(modulesDict[key].typeName, "module found with name", key, "and destination modules:",end='')
        for destModuleName in modulesDict[key].destModuleNames:
            print(" ", destModuleName,sep='',end='')
        if modulesDict[key].typeName == "conjunction":
            print("\n  and input modules:",end='')
            for inputModuleName in modulesDict[key].memory:
                print(" ", inputModuleName,sep='',end='')
        print('')


def parseInputFile(input_file):
    with open(input_file, "r") as file:
        data = file.readlines()

    modulesDict: dict[str, PulseModule] = {}
    buttonModule = PulseModule("button", ["broadcaster"])
    modulesDict["button"] = buttonModule

    for line in data:
        moduleStr = line.strip('\n').split(' ')
        moduleName = moduleStr[0]
        match moduleName[0]:
            case '%':
                modulesDict[moduleName[1:]] = PulseModule("flip-flop", [destModName.strip(',') for destModName in moduleStr[2:]])
            case '&':
                modulesDict[moduleName[1:]] = PulseModule("conjunction", [destModName.strip(',') for destModName in moduleStr[2:]])
            case _:
                modulesDict[moduleName] = PulseModule("broadcaster", [destModName.strip(',') for destModName in moduleStr[2:]])

    # go back and fill out memory for conjunction modules
    for key in modulesDict:
        for destModuleName in modulesDict[key].destModuleNames:
            if modulesDict[destModuleName].typeName == "conjunction":
                modulesDict[destModuleName].memory[key] = "low"

    return modulesDict


def pressButton(modulesDict: dict[str, PulseModule]) -> tuple[int, int]:
    lowPulsesSent, highPulsesSent = 0, 0
    q = queue.Queue()
    q.put(("button", "low", "null"))

    while not q.empty():
        moduleName, pulse, senderModuleName = q.get()
        moduleType = modulesDict[moduleName].typeName
        match moduleType:
            case "button":
                print("sending",pulse,"pulse from",moduleName,"to broadcaster")
                if pulse == "low":
                    lowPulsesSent += 1
                    q.put(("broadcaster", "low", "button"))
                else:
                    print("button with high pulse. No presents this year")
                    exit(1)
            case "broadcaster":
                #print("sending",pulse,"pulse from",moduleName,"to ",end='')
                #for destModuleName in modulesDict[moduleName].destModuleNames:
                #    print(destModuleName,"",end='')
                #print('')
                if pulse == "low":
                    lowPulsesSent += len(modulesDict[moduleName].destModuleNames)
                    for destModuleName in modulesDict[moduleName].destModuleNames:
                        q.put((destModuleName, "low", moduleName))
                else:
                    print("broadcaster with high pulse. No presents this year")
            case "flip-flop":
                if pulse == "low":
                    if modulesDict[moduleName].on:
                        #print("sending low pulse from",moduleName,"to ",end='')
                        #for destModuleName in modulesDict[moduleName].destModuleNames:
                        #    print(destModuleName," ",end='')
                        #print('')
                        lowPulsesSent += len(modulesDict[moduleName].destModuleNames)
                        for destModuleName in modulesDict[moduleName].destModuleNames:
                            q.put((destModuleName, "low", moduleName))
                        modulesDict[moduleName].on = False
                    else:
                        #print("sending high pulse from",moduleName,"to ",end='')
                        #for destModuleName in modulesDict[moduleName].destModuleNames:
                        #    print(destModuleName," ",end='')
                        #print('')
                        highPulsesSent += len(modulesDict[moduleName].destModuleNames)
                        for destModuleName in modulesDict[moduleName].destModuleNames:
                            q.put((destModuleName, "high", moduleName))
                        modulesDict[moduleName].on = True
            case "conjunction":
                modulesDict[moduleName].memory[senderModuleName] = pulse
                if all("high"==senderPulse for senderPulse in modulesDict[moduleName].memory.values()):
                    #print("sending low pulse from",moduleName,"to ",end='')
                    #for destModuleName in modulesDict[moduleName].destModuleNames:
                    #    print(destModuleName," ",end='')
                    #print('')
                    lowPulsesSent += len(modulesDict[moduleName].destModuleNames)
                    for destModuleName in modulesDict[moduleName].destModuleNames:
                        q.put((destModuleName, "low", moduleName))
                else:
                    #print("sending high pulse from",moduleName,"to ",end='')
                    #for destModuleName in modulesDict[moduleName].destModuleNames:
                    #    print(destModuleName," ",end='')
                    #print('')
                    highPulsesSent += len(modulesDict[moduleName].destModuleNames)
                    for destModuleName in modulesDict[moduleName].destModuleNames:
                        q.put((destModuleName, "high", moduleName))
    
    return lowPulsesSent, highPulsesSent


def main():

    input_file = "d20/test1.txt"
    modulesDict: dict[str, PulseModule] = parseInputFile(input_file)
    printModules(modulesDict)
    print('')
    lowPulsesSent, highPulsesSent = pressButton(modulesDict)
    print("Low Pulses Sent:", lowPulsesSent, "\nHigh Pulses Sent:",highPulsesSent)


if __name__ == "__main__":
    main()
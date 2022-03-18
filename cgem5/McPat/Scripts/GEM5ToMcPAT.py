#!/usr/bin/python
from optparse import OptionParser
import sys
import re
import json
import types
import math

import xml.etree.cElementTree as ET

def parse(source):
    return ET.parse(source)

def main():
    global opts
    usage = "usage: %prog [options] <gem5 stats file> <gem5 config file (json)> <mcpat template file>"
    parser = OptionParser(usage=usage)
    parser.add_option("-q", "--quiet", 
        action="store_false", dest="verbose", default=True,
        help="don't print status messages to stdout")
    parser.add_option("-o", "--out", type="string",
        action="store", dest="out", default="mcpat-out.xml",
        help="output file (input to McPAT)")
    (opts, args) = parser.parse_args()
    if len(args) != 3:
        parser.print_help()
        sys.exit(1)
    readStatsFile(args[0]) #
    readConfigFile(args[1])
    readMcpatFile(args[2])
    dumpMcpatOut(opts.out)

def dumpMcpatOut(outFile):
    rootElem = templateMcpat.getroot()
    configMatch = re.compile(r'config\.([a-zA-Z0-9_:\.]+)')
    #replace params with values from the GEM5 config file 
    #for param in rootElem.iter('param'):
    for param in rootElem.getiterator('param'):
        name = param.attrib['name']
        value = param.attrib['value']
        if 'config' in value:
            allConfs = configMatch.findall(value)
            for conf in allConfs:
                confValue = getConfValue(conf)
         
#Be careful because in some cases, GEM5 seems to post a single value but inside [...]
#python seems to think this is a list and creates problems         
         
                if isinstance(confValue, types.ListType):
                    if (len(confValue)==1):
                        confValue=confValue[0]
     
                    
                value = re.sub("config."+ conf, str(confValue), value)
            if "," in value:
                exprs = re.split(',', value)
                for i in range(len(exprs)):
                    exprs[i] = str(eval(exprs[i]))
                param.attrib['value'] = ','.join(exprs)
            else:
                param.attrib['value'] = str(eval(str(value)))

    #replace stats with values from the GEM5 stats file 
    statRe = re.compile(r'stats\.([a-zA-Z0-9_:\.]+)')
    #for stat in rootElem.iter('stat'):
    for stat in rootElem.getiterator('stat'):
        name = stat.attrib['name']
        value = stat.attrib['value']
        if 'stats' in value:
            allStats = statRe.findall(value)
            expr = value
            for i in range(len(allStats)):
                if allStats[i] in stats:
                    expr = re.sub('stats.%s' % allStats[i], stats[allStats[i]], expr)
                else:
                    print ("***WARNING: %s does not exist in stats***" % allStats[i])
                    print ("\t Please use the right stats in your McPAT template file")

            if 'config' not in expr and 'stats' not in expr:
                stat.attrib['value'] = str(eval(expr))
    #Write out the xml file
    if opts.verbose: print ("Writing input to McPAT in: %s" % outFile)
    templateMcpat.write(outFile)

def getConfValue(confStr):
    spltConf = re.split('\.', confStr) 
    currConf = config
    currHierarchy = ""
    for x in spltConf:
        currHierarchy += x
        if x not in currConf:
            if isinstance(currConf, types.ListType):
                #this is mostly for system.cpu* as system.cpu is an array
                #This could be made better
                if x not in currConf[0]:
                    print ("%s does not exist in config" % currHierarchy)
                else:
                    currConf = currConf[0][x]
            else:
                    print ("***WARNING: %s does not exist in config.***" % currHierarchy)
                    print ("\t Please use the right config param in your McPAT template file")
        else:
            currConf = currConf[x]
        currHierarchy += "."
    return currConf
    

def readStatsFile(statsFile):
    global stats
    stats = {}
    if opts.verbose: print ("Reading GEM5 stats from: %s" %  statsFile)
    F = open(statsFile)
    ignores = re.compile(r'^---|^$')
    #Please note that changes in the gem5 stats file may require changes here.
    #Note for last stable version of gem5: Some statistics names are appended by numbers similar to this: 5e+10-1e+11 .
    statLine = re.compile(r'([a-zA-Z0-9_\.:+-]+)\s+([-+]?[0-9]+\.[0-9]+|[-+]?[0-9]+|nan|inf)')
    count = 0 
    for line in F:
        #ignore empty lines and lines starting with "---"  
        if not ignores.match(line):
            count += 1
        #Exceptions are used to make sure that updates to gem5 stats file do not break the converter.
        try:
            statKind = statLine.match(line).group(1)
            statValue = statLine.match(line).group(2)
        except Exception as e:
            continue
            if statValue == 'nan':
                print ("\tWarning (stats): %s is nan. Setting it to 0" % statKind)
                statValue = '0'
            if statKind == 'testsys.cpu.num_idle_cycles':
                stats[statKind] = str(int(float(statValue) + 0.5))
        else:
            if statKind == 'testsys.cpu.num_busy_cycles':
                stats[statKind] = str(int(float(statValue) + 0.5))
            else:
                stats[statKind] = statValue
            
    F.close()

def readConfigFile(configFile):
    global config
    if opts.verbose: print ("Reading config from: %s" % configFile)
    F = open(configFile)
    config = json.load(F)
    
    F.close()

def readMcpatFile(templateFile):
    global templateMcpat 
    if opts.verbose: print ("Reading McPAT template from: %s" % templateFile)
    templateMcpat = parse(templateFile)
   
    
    

if __name__ == '__main__':
    main()

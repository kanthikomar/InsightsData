import operator
import sys,re

def SortedDictionary(dictionary):
    return sorted(dictionary.items(), key=lambda kv: (-kv[1], kv[0]))

def writeToFiles(output,data,totaldata):
    for item, count in data[:10]:
        output.write("{0};{1};{2}%{3}".format(item, count, (count / totaldata) * 100, "\n"))

if __name__ == '__main__':
    # Input and output files
    # inputFileName = open("..\input\\h1b_input.csv","r",encoding="utf8")
    # output1 = open("..\output\\top_10_states.txt", "w+")
    # output2 = open("..\output\\top_10_occupations.txt","w+")
    inputFileName = open(sys.argv[1],"r",encoding="utf8")
    output2 = open(sys.argv[2], "w+")
    output1 = open(sys.argv[3], "w+")

    # Initializing variables
    states= {}
    jobTitle = {}
    totalStates = 0
    totalJobTitle = 0
    listOfLabels = []
    certificationIndex = 0
    regex = re.compile('"')
    # Prepare dictionary of States and Job Titles
    for i in inputFileName:
        attributes = [regex.sub('', x) for x in i.split(";")]
        if( attributes[0] == ''):
            listOfLabels = attributes
            stateIndex = listOfLabels.index("WORKSITE_STATE")
            jobTitleIndex = listOfLabels.index("SOC_NAME")
            certificationIndex = listOfLabels.index("CASE_STATUS")
        else:
            if attributes[certificationIndex] == 'CERTIFIED':
                if(attributes[stateIndex] not in states):
                    states[attributes[stateIndex]] = 1
                    totalStates+=1
                else:
                    states[attributes[stateIndex]]+=1
                    totalStates += 1
                if(attributes[jobTitleIndex] not in jobTitle):
                    jobTitle[attributes[jobTitleIndex]] = 1
                    totalJobTitle+=1
                else:
                    jobTitle[attributes[jobTitleIndex]]+=1
                    totalJobTitle+=1
    # Sort the dictionaries with respect to the values
    sortedStates = SortedDictionary(states)
    sortedJobTitle = SortedDictionary(jobTitle)

    # Write output to file
    output1.write("TOP_STATES;NUMBER_CERTIFIED_APPLICATIONS;PERCENTAGE\n")
    writeToFiles(output1,sortedStates,totalStates)
    output2.write("TOP_OCCUPATIONS;NUMBER_CERTIFIED_APPLICATIONS;PERCENTAGE\n")
    writeToFiles(output2,sortedJobTitle,totalJobTitle)

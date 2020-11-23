import sys
import re
import os

arguments = sys.argv[1:]

def validate_hostanme(file):
    if os.path.exists(file):
        with open(file, "r") as file_object:
            if os.path.getsize(sys.argv[2]) == 0:
                print("No Hosts")
            else:
                line = file_object.readlines()
                counter_flag = 0
                print("Hostnames:")
                for x in line:
                    x = x.rstrip()
                    result = x.split()
                    if not x:
                        continue
                    hostnames = re.match(
                        '^(([a-zA-Z0-9]|[a-zA-Z0-9][a-zA-Z0-9\-]*[a-zA-Z0-9])\.)*([A-Za-z0-9]|[A-Za-z0-9][A-Za-z0-9\-]*[A-Za-z0-9])$',
                        str(result[1])) #“Match a valid hostname - Regex Pal” 2020, Regexpal.com, viewed 21 October 2020, <https://www.regexpal.com/23>.
                    if hostnames:
                        counter_flag += 1
                        print (hostnames.group())
                    elif hostnames is None:
                        continue
                if counter_flag == 0:
                    print("No hosts")
    else:
        print("Invalid host file name")

def validate_domain(file):
    if os.path.exists(file):
        with open(file, "r") as file_object:
            if os.path.getsize(sys.argv[3]) == 0:
                print("No hosts in the given domain")
            else:
                counter_flag = 0
                line = file_object.readlines()
                for x in line:
                    x = x.rstrip()
                    result = x.split()
                    if not x:
                        continue
                    domain_name = sys.argv[2]
                    domains = re.search('^(http:\/\/)?(\w*\.)*' + domain_name + '(\/.*)?$', str(result[1])) #Dominic 2012, “What is a regular expression which will match a valid domain name without a subdomain?,” Stack Overflow,
                                                                                                            #viewed 21 October 2020, <https://stackoverflow.com/questions/10306690/what-is-a-regular-expression-which-will-match-a-valid-domain-name-without-a-subd?rq=1>.
                    if domains:
                        counter_flag += 1
                        print(result[0] + '\t' + domains.group() + '\t' + result[2])

                if counter_flag == 0:
                    print("No hosts in the given domain")
    else:
        print("Invalid Host File Name")

def validate_ip_class(file):
    if os.path.exists(file):
        with open(file, "r") as file_object:
            if os.path.getsize(sys.argv[3]) == 0:
                print("No hosts in the given domain")
            else:
                counter_flag = 0
                error_flag=0
                line = file_object.readlines()
                for x in line:
                    x = x.rstrip()
                    result = x.split()
                    if not x:
                        continue
                    class_name = sys.argv[2]
                    if class_name == 'A':
                        ip_address = re.search(
                            '^([0-9]|[1-8][0-9]|9[0-9]|1[01][0-9]|12[0-7])\.(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\.(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\.(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])$',
                            str(result[0]))
                        if ip_address:
                            counter_flag += 1
                            print(ip_address.group() + '\t' + result[1] + '\t' + result[2])
                    elif class_name == 'B':
                        ip_address = re.search(
                            '^(12[89]|1[3-8][0-9]|19[01])\.(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\.(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\.(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])$',
                            str(result[0]))
                        if ip_address:
                            counter_flag += 1
                            print(ip_address.group() + '\t' + result[1] + '\t' + result[2])
                    elif class_name == 'C':
                        ip_address = re.search(
                            '^(19[2-9]|2[0-4][0-9]|25[0-5])\.(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\.(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\.(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])$',
                            str(result[0]))
                        if ip_address:
                            counter_flag += 1
                            print(ip_address.group() + '\t' + result[1] + '\t' + result[2])
                    else:
                        error_flag=1
                        print("Error - Class argument not Valid\nAvailable class arguments are A, B or C")
                        break

                if counter_flag == 0 and error_flag == 0:
                    print("No Hosts in The Given Class")
    else:
        print("Invalid Host File Name")

def my_info(file):
    if os.path.exists(file):
        print("\n\nName:\t\t\tAbhinav\nSurname:\t\tChaudhary\nStudent ID:\t\t13313162\nCompletion Data:\t21 October 2020\n\n")
    else:
        print("Invalid Host File Name")

def invoke_arguments():
    if sys.argv[1] == '-a' and len(arguments) == 2:
        validate_hostanme(sys.argv[2])
    elif sys.argv[1] == '-a' and len(arguments) < 2:
        print("Host file missing")

    elif sys.argv[1] == '-d' and len(arguments) == 3:
        validate_domain(sys.argv[3])
    elif sys.argv[1] == '-d' and len(arguments) == 1:
        print("Domain argument and host file missing")
    elif sys.argv[1] == '-d' and len(arguments) == 2:
        print("Host file missing")

    elif sys.argv[1] == '-c' and len(arguments) == 3:
        validate_ip_class(sys.argv[3])
    elif sys.argv[1] == '-c' and len(arguments) == 1:
        print("Class argument and host file missing\nAvailable class arguments are A, B or C")
    elif sys.argv[1] == '-c' and len(arguments) == 2:
        print("Host file missing")

    elif sys.argv[1] == '-v' and len(arguments) == 2:
        my_info(sys.argv[2])
    elif sys.argv[1] == '-v' and len(arguments) < 2:
        print("Host file missing")

    else:
        print("Invalid Option Specified")

invoke_arguments()

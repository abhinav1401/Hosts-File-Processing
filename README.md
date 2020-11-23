# Hosts-File-Processing

<h3> Tools Used - Python and Terminal </h3>

<img align="left" alt="Python" width="26px" src="https://cdn4.iconfinder.com/data/icons/logos-and-brands/512/267_Python_logo-512.png"/>
<img align="left" alt="Terminal" width="26px" src="https://raw.githubusercontent.com/github/explore/80688e429a7d4ef2fca1e82350fe8e3517d3494d/topics/terminal/terminal.png" />

<br> </br>

The script is invoked as:

<b>python hosts.py option hosts_file</b>

This works on a host file of the given format,

![alt text](https://github.com/abhinav1401/Hosts-File-Processing/blob/main/Host_File_Sample.png)

The script can be invoked with the following options:

<b>-a</b>

In this case, it prints all the hostnames in the order in which they appear in file hosts file.

<b>-d</b>

In this case the domain argument is a string that represents the top-level domain of a hostname (the string after the right-most dot in the hostname). For example, if in the sample hosts file, strings localdomain, edu, org and com are all top-level domains. The script in this case prints all the lines of file hosts file where the top-level domain of the hostname matches the given domain argument, in the order in which they appear in the file. 

<b>-c</b>

Here the class argument is a string of one character that can only take values A, B or C (please note: only uppercase).

Example code: python hosts.py -c A hosts_file

In the case in which the value is A, the script prints all the lines of file hosts file where the number before the first dot in the IPv4 address field is between 0 and 127, included, in the order in which they appear in the file. 

In the case in which the value is B, the script prints all the lines of file hosts file where the number before the first dot in the IPv4 address field is between 128 and 191, included, in the order in which they appear in the file. 

In the case in which the value is C, the script prints all the lines of file hosts file where the number before the first dot in the IPv4 address field is between 192 and 255, included, in the order in which they appear in the file. 


    


###################################################
# IP address validator
# details: https://en.wikipedia.org/wiki/IP_address
# Student should enter function on the next lines.
#
#
# First function is_valid_ip() should return:
# True if the string inserted is a valid IP address
# or False if the string is not a real IP
#
#
# Second function get_ip_class() should return a string:
# "X is a class Y IP" or "X is classless IP" (without the ") or "X is not a valid IP"
# where X represent the IP string,
# and Y represent the class type: A, B, C, D, E
# ref: http://www.cloudtacker.com/Styles/IP_Address_Classes_and_Representation.png
# Note: if an IP address is not valid, the function should return
# "X is not a valid IP address"
###################################################
import re


def is_valid_ip(ip):

    valid_octet = []
    #  find all instances of ip addresses in given input (ip) and puts it in a list
    ip_list = re.findall(r"\d+.\d+.\d+.\d+", ip)
    # if input does not have any IP addresses, prints notification
    if not ip_list:
        print("No IP addresses exist")
    else:
        # makes a list of all octets in each IP address
        for each_ip in ip_list:
            four_octets = re.findall(r"\d+", each_ip)
        # turns octet into integer and checks if octet falls between 0 and 255
        for each_octet in four_octets:
            each_octet = int(each_octet)
            if 0 <= each_octet <= 255:
                valid_octet.append(True)
            else:
                valid_octet.append(False)
    #  check if all 4 octets are valid (between 0 and 255)
    if False in valid_octet:
        valid_flag = False
    else:
        valid_flag = True

    return valid_flag



def get_ip_class(ip):
    if is_valid_ip(ip) == False:
        return ip + " is not a valid IP address"
    if is_valid_ip(ip) == True:
        #  identifies ip address and splits it into a list of octets
        ip_address = re.search(r"\d+.\d+.\d+.\d+", ip)
        ip_address = ip_address.group()
        octets = re.findall(r"\d+", ip_address)
        #  converts octets into integers
        octets = list(map(int, octets))
        #  checks first octet to see which class it belongs to
        if 1 <= octets[0] <= 127:
            return ip_address + " is a class A IP"
        elif 128 <= octets[0] <= 191:
            return ip_address + " is a class B IP"
        elif 192 <= octets[0] <= 223:
            return ip_address + " is a class C IP"
        elif 224 <= octets[0] <= 239:
            return ip_address + " is a class D IP"
        elif 240 <= octets[0] <= 255:
            return ip_address + " is a class E IP"
    # return return_text


# To be continued...
# To check for classless IP address, I assume I'll need to check the subnet mask. Class A should have 8 bits in subnet mask, Class B - 16 bits, Class C - 24 bits. I assume if subnet mask has anything other than 8, 16, or 24 bits then it must be classless?

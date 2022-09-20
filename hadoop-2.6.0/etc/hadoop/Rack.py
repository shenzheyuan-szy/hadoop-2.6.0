#!/usr/bin/python
#-*-coding:UTF-8 -*-
import sys

rack = {"slave1":"dc1/rack4",
        "slave2":"dc2/rack6",
        "slave3":"dc1/rack4",
        "slave4":"dc1/rack1",
        "slave5":"dc1/rack1",
        "slave6":"dc2/rack8",
        "slave7":"dc1/rack5",
        "slave8":"dc2/rack9",
        "slave9":"dc2/rack10",
        "slave10":"dc2/rack8",
        "slave11":"dc2/rack10",
        "slave12":"dc2/rack6",
        "slave13":"dc1/rack1",
        "slave14":"dc1/rack2",
        "slave15":"dc1/rack4",
        "slave16":"dc2/rack10",
        "10.0.0.15":"dc1/rack4",
        "10.0.0.16":"dc2/rack6",
        "10.0.0.17":"dc1/rack4",
        "10.0.0.18":"dc1/rack1",
        "10.0.0.19":"dc1/rack1",
        "10.0.0.20":"dc2/rack8",
        "10.0.0.21":"dc1/rack5",
        "10.0.0.22":"dc2/rack9",
        "10.0.0.23":"dc2/rack10",
        "10.0.0.24":"dc2/rack8",
        "10.0.0.25":"dc2/rack10",
        "10.0.0.26":"dc2/rack6",
        "10.0.0.38":"dc1/rack1",
        "10.0.0.35":"dc1/rack2",
        "10.0.0.41":"dc1/rack4",
        "10.0.0.37":"dc2/rack10"
        #"192.168.0.27":"dc1/rack1",
        #"192.168.0.18":"dc2/rack2",
        #"192.168.0.24":"dc2/rack3",
	#"192.168.0.26":"dc1/rack1"
        }

if __name__=="__main__":
        print "/" + rack.get(sys.argv[1],"rack0")

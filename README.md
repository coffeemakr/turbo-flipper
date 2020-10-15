# Turbo Flipper
A script to simplify bit manipulation that can be used in turbo intruder. The code is therefore Python 2 (Jython) compatible.

## Usage
Get the latest turbo intruder jar from [their release page](https://github.com/PortSwigger/turbo-intruder/releases) and run the example from the root directory:
```
java -jar turbo-intruder-all.jar examples/flip-bits-base64.py request.txt http://localhost:8000  YWJjZGVmZ2hpams=
```

```
ID | Word | Status | Wordcount | Length | Time
Starting attack...
Warming up...
1 | YeJjZGVmZ2hpams= | 404 | 246 | 653 | 3
4 | ZWJjZGVmZ2hpams= | 404 | 246 | 653 | 4
2 | 4WJjZGVmZ2hpams= | 404 | 246 | 653 | 1
3 | IWJjZGVmZ2hpams= | 404 | 246 | 653 | 5
5 | QWJjZGVmZ2hpams= | 404 | 246 | 653 | 1
6 | Y2JjZGVmZ2hpams= | 404 | 246 | 653 | 4
8 | YWJjZGVmZ2hpams= | 404 | 246 | 653 | 0
7 | cWJjZGVmZ2hpams= | 404 | 246 | 653 | 2
9 | aWJjZGVmZ2hpams= | 404 | 246 | 653 | 5
11 | YGJjZGVmZ2hpams= | 404 | 246 | 653 | 3```
```

## Scripting

#!/usr/bin/python
# -*- coding: utf-8 -*-

import argparse
import re


class LEDSwitcher:

    def __init__(self, size):
        self.a2d = [ [1]*size for _ in range(size) ]
        self.n = size
        pass

    def _setValu(self, x1,x2,y1,y2, x):
        for i in range(x1, x2+1):
            for j in range(y1, y2+1):
                self.a2d[i][j]=x
        pass

    def turn_on(self, x1,x2,y1,y2):
        self._setValu(x1, x2, y1, y2, 1)
        pass

    def turn_off(self, x1,x2,y1,y2):
        self._setValu(x1, x2, y1, y2, 0)
        pass

    def switch(self, x1,x2,y1,y2):
        
        for i in range(x1, x2+1):
            for j in range(y1, y2+1):
                self.a2d[i][j] ^= 1
        pass

    def count(self):
        sum=0;
        
        for i in range(self.n):
            for j in range(self.n):
                sum += self.a2d[i][j]
        
        return sum
        pass

    def parse_cmd_str(self, cmd_str):
        """
        extract the command (turn on/off/switch) and the ranges (x1,y1,x2,y2) from the cmd_str
        """
        # cmd_str is a line from the file: "turn on 0,0, through 9,9" 
        # you need to write the pat here
        
        pat = re.compile("([\w\s]+)\s(\d+),(\d+)\s\w+\s(\d+),(\d+)")
        cmd, x1, y1, x2, y2 = ('', '0', '0', '0', '0')
        m = re.match(pat, cmd_str)
        
        if m!=None:
            cmd, x1, y1, x2, y2 = re.match(pat, cmd_str).groups()

        # maybe check consistency of cmds, ranges...
        return cmd, x1, y1, x2, y2
        
        pass

    def execute_command(self, line):
        #return
        #print(line)
        cmd, x1, y1, x2, y2 = self.parse_cmd_str(line)
        x1 = int(x1)
        y1 = int(y1)
        x2 = int(x2)
        y2 = int(y2)
        
        if cmd == 'turn on':
            self.turn_on(x1, x2, y1, y2)
            pass
        elif cmd == 'turn off':
            self.turn_off(x1, x2, y1, y2)
            pass
        elif cmd == 'switch':
            self.switch(x1, x2, y1, y2)
        
        pass
    
    

def main():    
    print('515')
    # parse the command line arguments to get the input filename
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', help='input help')
    args = parser.parse_args()

    # now the filename arguments is in args.input
    filename = args.input
    print(filename)
    if filename is None:
        return

    # read_file reads the contents of the buffer into a single string
    buffer =  open(filename).read()

    # break the buffer into lines
    lines = buffer.split('\n')

    # the first line is the size of the LED array
    size = int(lines[0])

    # I construct a class to do the testing
    tester = LEDSwitcher(size)

    # now loop over each line (except the first) and process the commands (turn on/off, switch)
    for i, line in enumerate(lines[1:]):
        tester.execute_command(line)

    # at the end, count the number of lights that are on
    print("{} {}".format(filename, tester.count()))
    
    #pat = re.compile("User-Agent: (\w+) (.*) \(X11/(\d+)\)")        
    #m = pat.match("User-Agent: Thunderbird 1.5.0.9 (X11/20061227)")
    
    
    #pat = re.compile("([\w\s]+)\s(\d+),(\d+)\s\w+\s(\d+),(\d+)")        
    #m = pat.match("turn off 660,55 through 986,197")
    #m = pat.match("switch 660,55 through 986,197")
    #print("matched: ", m is not None, m.groups())
    
    return

if __name__ == '__main__':
    main()
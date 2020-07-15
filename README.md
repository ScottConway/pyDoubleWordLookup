# pyDoubleWordLookup

This was a little cheat tool I created to help solve a puzzle in the July 2020 Mensa Bulletin 
(page 15 - Split Decisions). And to help learn more about Python (because otherwise I would have 
totally done it in Java though the result would have been much longer).  

The puzzle is sort of like a cross word except that the clues are embedded in the words themselves.  
They give you they give you two sets of two letters so it is really two words you are creating.   

An example is as follows
 
```
      at
    /    \
___         ___
    \    /  /  \
      el     ou
             gn
            \  /
             __
```

The answers for the three blanks are w, t, and a giving the first word pair of watt & welt and the 
second word pair of toga & tuna. 

So I created a program that would take two patterns, ?at? and ?el?, convert them to regular
expressions, and search through a dictionary of words to find possible matches.  

    
## Running pyDoubleWordLookup.py

    ./pyDoubleWordLookup.py -h                                                                             0 (0.002s) < 21:19:34
    usage: pyDoubleWordLookup.py [-h] [-p1 PATTERN1] [-p2 PATTERN2] [--version]
    
    Find words in dictionary against two patterns whose unknown letters match.
    
    optional arguments:
      -h, --help    show this help message and exit
      -p1 PATTERN1  First pattern to look up.
      -p2 PATTERN2  Second pattern to look up.
      --version     show program's version number and exit
      
      
    ./pyDoubleWordLookup.py -p1 \?og\? -p2 \?un\?                                                          0 (0.276s) < 17:26:31
    pattern1 = ?og?
    pattern2 = ?un?
    hogs / huns
    pogo / puno
    nogs / nuns
    bogs / buns
    toga / tuna
    fogs / funs
    doge / dune
    togs / tuns
    dogy / duny
    mogs / muns
    pogy / puny
    hogg / hung
    boga / buna
    dogs / duns
    togo / tuno
    logy / luny
    loge / lune
      
## Sources

The word list Is from a github project [dwyl/english-words](https://github.com/dwyl/english-words).

# signletters

Python program to determine if messages can be spelled given the availability of letters for a sign.

You work at a business where the boss likes to put clever messages on the marquee sign.
In the "messages" directory, you'll find many text files each containing a short message such as:

```
$ cat messages/1.txt
Dogs can't operate MRI scanners but catscan.
```

Not all characters of the alphabet are represented in the letters for the marquee.
Further, the characters occur in different frequencies based upon their relative use in the English language.
In the "letters" directory, you'll find text files detailing the number of times you'll find each letter in a given set:

```
$ cat letters/1.txt
12: A E I N O R S
8: L T 5 6
6: B C D F G H J K M P U W Y
4: Q V X Z 1 2 3 4 7 8 0 ! * .
2: - ! / % &
```

The `signletters.py` program will check if there are sufficient characters to spell the given message(s):

```
$ ./signletters.py -h
usage: signletters.py [-h] [-t str [str ...]] [-l LETTERS]

Spell messages with limited letters

optional arguments:
  -h, --help            show this help message and exit
  -t str [str ...], --text str [str ...]
                        Input message or file (default: None)
  -l LETTERS, --letters LETTERS
                        File with letter frequencies (default: None)
```

The message may be given as text on the command line.
Note that the letters are UPPERCASE ONLY:

```
$ ./signletters.py -l letters/1.txt -t "Dogs can't operate MRI scanners but catscan."
OK  : DOGS CAN'T OPERATE MRI SCANNERS BUT CATSCAN.
```

Or the message argument may be the name of a file containing the message:

```
$ ./signletters.py -l letters/1.txt -t messages/2.txt
OK  : OUR MOUNTAINS AREN'T JUST FUNNY THEY'RE HILL AREAS.
```

One of the "letters" inputs has very few letters, and so many messages cannot be spelled:

```
$ ./signletters.py -l letters/3.txt -t messages/*
Nope: DOGS CAN'T OPERATE MRI SCANNERS BUT CATSCAN.
Nope: FOR CHEMISTS ALCOHOL IS NOT A PROBLEM, IT'S A SOLUTION.
Nope: MY MOOD RING IS MISSING AND I DON'T KNOW HOW I FEEL ABOUT THAT.
Nope: I SCREAM, YOU SCREAM, THE POLICE COME, IT'S AWKWARD.
OK  : DESPITE THE HIGH COST OF LIVING, IT REMAINS POPULAR.
Nope: I'M FRIENDS WITH 25 LETTERS OF THE ALPHABET. I DON'T KNOW Y.
Nope: COW STUMBLES INTO POT FIELD! THE STEAKS HAVE NEVER BEEN HIGHER.
OK  : CRUSHING POP CANS IS SODA PRESSING.
Nope: IN SEARCH OF FRESH VEGETABLE PUNS. LETTUCE KNOW.
OK  : HE WHO LAUGHS LAST DIDN'T GET IT.
Nope: BIG SHOUT OUT TO MY FINGERS. I CAN ALWAYS COUNT ON THEM.
Nope: OUR MOUNTAINS AREN'T JUST FUNNY THEY'RE HILL AREAS.
OK  : TURNING VEGAN WOULD BE A BIG MISSED STEAK.
OK  : WELL, TO BE FRANK, I'D HAVE TO CHANGE MY NAME.
Nope: FORGET WORLD PEACE, VISUALIZE USING YOUR TURN SIGNAL.
Nope: LIFE IS SHORT. IF YOU CAN'T LAUGH AT YOURSELF, CALL ME. I WILL.
Nope: QU!T ST3AL!NG R 7ETT3R$
Nope: IN 20 YEARS THIS COUNTRY WILL BE RUN BY PEOPLE HOMESCHOOLED BY DAY DRINKERS.
Nope: ELECTRICIANS HAVE TO STRIP TO MAKE ENDS MEET.
```

To test:

```
$ make test
pytest -xv signletters.py test.py
============================= test session starts ==============================
...

signletters.py::test_read_letters PASSED                                 [ 12%]
signletters.py::test_check_test PASSED                                   [ 25%]
test.py::test_exists PASSED                                              [ 37%]
test.py::test_usage PASSED                                               [ 50%]
test.py::test_bad_file PASSED                                            [ 62%]
test.py::test_ok_command_line PASSED                                     [ 75%]
test.py::test_ok_file PASSED                                             [ 87%]
test.py::test_not_ok_file PASSED                                         [100%]

============================== 8 passed in 0.31s ===============================
```

# Author

Ken Youens-Clark <kyclark@gmail.com>

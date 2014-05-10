True and True # True
False and True # False
1 == 1 and 2 == 1 # False
"test" == "test" # True
1 == 1 or 2 != 1 # True or True is True
True and 1 == 1 # True and True is True
False and 0 != 0 # False and False is False
True or 1 == 1 # True or True is True
"test" == "testing" # False
1 != 0 and 2 == 1 # True and False is False
"test" != "testing" # True
"test" == 1 # False
not (True and False) # not False is True
not (1 == 1 and 0 != 1) # not (True and True) is not True is False
not (10 == 1 or 1000 == 1000) # not (False or True) is not True is False
not (1 != 10 or 3 == 4) # not (True or False) is not True is False
not ("testing" == "testing" and "Zed" == "Cool Guy") # not (True and False) is not False is True
1 == 1 and not ("testing" == 1 or 1 == 0) # True and not (False or False) is True and not False is True and True is True
"chunky" == "bacon" and not (3 == 4 or 3 == 3) # False and not (False or True) is False and not True is False and False is False
3 == 3 and not ("testing" == "testing" or "Python" == "Fun") # True and not (True or False) is True and not True is True and False is False

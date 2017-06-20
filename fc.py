# Make sure that the_flying_circus() returns True
def the_flying_circus():
    if (100 != 10*10) and (False or True):
        print "The Flying Circus returns Truiesh!"
        return True
        
    elif (120 != 10*10)  and (not False and not False):
        print "The Flying Circus returns True!"
        return True
    else:
        print "The Flying Circus is a numpty!"
        return False

the_flying_circus()
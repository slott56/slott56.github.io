Schrodinger's cat lives! Or doesn't!
====================================

:date: 2008-11-22 23:27
:tags: architecture,design,data structure,algorithm
:slug: 2008_11_22-schrodingers_cat_lives_or_doesnt
:category: Architecture & Design
:status: published







See this question on `Python objects deleting themselves <http://stackoverflow.com/questions/293431/python-object-deleting-itself>`_ .  There was some fundamental confusion about objects, deletion and garbage collection.



Some additional material was posted in an answer (not in the question, where it belongs) making it a little hard to go from question to answers.  The original poster's non-answer had a great little block of code that's potentially funny.  [This is the real example; I tidied it up a little.]

..  code:

::

    class Generic:
        ''' Generic class all other classes inherit '''
        def kill(self):
            del self
            #Need a way to remove the instance of the class
    
    class Item(Generic):
        def __init__(self,name):
            self.name = name
    
    class Being(Generic):
        def __init__(self,name):
            self.name = name
            self.bag = []
        def pick_up(self,target):
            self.bag.append(target)
            target.kill()
    
    player = Being('Hero')
    cat = Item('Cat')
    
    print'Players inventory',player.bag
    
    print'Picking up the cat'
    player.pick_up(cat)
    
    print'Players inventory',player.bag





:strong:`The Cat is Out of the Bag` 



Really.  The example was about letting the cat out of the bag.



`My answer <http://stackoverflow.com/questions/293431/python-object-deleting-itself#293920>`_  included the following.

    

    Under no circumstances does any Python object ever need to get deleted. If an item is "destroyed", then it's not in a Being's bag. It's not in a location.

    ..  code:

    ::

        player.bag.remove(cat)

    

    

    Is all that's required to let the cat out of the bag. Since the cat is not used anywhere else, it will both exist as "used" memory and not exist because nothing in your program can access it. It will quietly vanish from memory when some quantum event occurs and memory references are garbage collected.





Anyway, I think there is a parallel between Schrodinger's cat and garbage collection.  The cat exists while you're using it.  After you cease to reference it, it may -- or may not -- exist.



Okay, maybe it wasn't that funny.






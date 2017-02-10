#! /usr/bin/env python
'Assorted class utilites and tools'

class AttrDisplay:
    '''
    Provides an inheritable print overload method that displays
    instances with their class names and a name+value pair for 
    each attribute stored on the instance itself (but not attrs 
    inherited its classes). Can be mixed into any class,
    and will work on any instance.
    '''

    def gatherAttrs(self):
        attr = []
        for key in sorted(self.__dict__):
            attr.append('%s = %s' % (key, getattr(self, key)))
        return ', '.join(attr)
    def __str__(self):
        return '[%s: %s]' % (self.__class__.__name__, self.gatherAttrs())

if __name__ == '__main__':
    class TopTest(AttrDisplay):
        count = 0
        def __init__(self):
            self.attr1 = TopTest.count
            self.attr2 = TopTest.count + 1
            TopTest.count += 2

    class SubTest(TopTest):
        pass

    x, y = TopTest(), SubTest()
    print(x)
    print(y)

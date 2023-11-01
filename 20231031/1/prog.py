class Omnibus :
    attr_counter = {}

    def __setattr__(self, name, mean) :
        if name in Omnibus.attr_counter.keys() :
            Omnibus.attr_counter[name][0] += 1
            if not self in Omnibus.attr_counter[name][1] :
                Omnibus.attr_counter[name][1].append(self)
        else :
            Omnibus.attr_counter[name] = [0,[]]
            Omnibus.attr_counter[name][0] = 1
            Omnibus.attr_counter[name][1] = [self]
        pass
    
    def __getattr__(self, name) :
        if self in Omnibus.attr_counter[name][1] :
            return Omnibus.attr_counter[name][0]
        return

    def __delattr__(self, name) :
        if name in Omnibus.attr_counter.keys() and self in Omnibus.attr_counter[name][1]:
            Omnibus.attr_counter[name][0] -= 1
            Omnibus.attr_counter[name][1].remove(self)
        
        pass

import sys
exec(sys.stdin.read())

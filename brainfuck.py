import sys
from itertools import repeat, takewhile

interpret = (
    lambda inst: (
         lambda ins: (
                 lambda state: (
                     lambda f: [ i for i in
                             takewhile(
                             lambda d: (d['i'] < len(ins), state.update(dict(zip(['ptr', 'i'], f(ins, **d)))))[0],
                             repeat(state),
                         )
                     ]*0 or None
                 )
         )(
             {
                 'ptr':0,
                 'i':0,
                 'data':[0]*100000,
                 'bp':(
                     (lambda f: f(f, [], {}, 0)[0][1])(
                         lambda g, bs, bp, ix: (
                             ((bs, bp),) if ix >= len(ins) else (
                                 (g(g, bs + [ix], bp, ix+1), )[0] if ins[ix] == '['
                                 else (
                                     (g(g, bs[:-1], bp, ix+1), bp.update({ix: bs[-1], bs[-1]:ix}),)[0] if ins[ix] == ']'
                                     else g(g, bs, bp, ix+1)
                                 )
                             )
                         )
                     )
                 )
             },
         )(
             lambda ins, ptr, i, data, bp: (
                 (ptr, i) if i >= len(ins)
                 else {
                     '>': lambda p, i: (p + 1, i+1,),
                     '<': lambda p, i: (p - 1, i+1,),
                     '+': lambda p, i: (p, i+1, data.__setitem__(p, (data[p]+1)%256))[:-1],
                     '-': lambda p, i: (p, i+1, data.__setitem__(p, (data[p]-1)%256))[:-1],
                     '.': lambda p, i: (p, i+1, sys.stdout.write(chr(data[p])))[:-1],
                     ',': lambda p, i: (p, i+1, data.__setitem__(p, ord(sys.stdin.buffer.read(1))))[:-1],
                     '[': lambda p, i: (p, bp[i] + 1 if not data[p] else i+1, ),
                     ']': lambda p, i: (p, bp[i] + 1 if data[p] else i+1, ),
                 }[ins[i]](ptr, i))
         )
    )(''.join(i for i in inst if i in '<>+-.,[]'))
)

if __name__=='__main__':
    with open(sys.argv[1]) as f:
        s = f.read()
    interpret(s)

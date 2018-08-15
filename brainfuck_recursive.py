(
    lambda ins, sys: (
        (
            lambda f: f(
                f, 0, 0,
                data=[0]*100000,
                bp=(
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
            )
        )(
            lambda g, ptr, i, data, bp: (
                None if i >= len(ins)
                else g(g, *{
                    '>': lambda d, p, i, brace_pairs: (p + 1, i+1,),
                    '<': lambda d, p, i, brace_pairs: (p - 1, i+1,),
                    '+': lambda d, p, i, brace_pairs: (p, i+1, d.__setitem__(p, (d[p]+1)%256))[:-1],
                    '-': lambda d, p, i, brace_pairs: (p, i+1, d.__setitem__(p, (d[p]-1)%256))[:-1],
                    '.': lambda d, p, i, brace_pairs: (p, i+1, sys.stdout.write(chr(d[p])))[:-1],
                    ',': lambda d, p, i, brace_pairs: (p, i+1, d.__setitem__(p, ord(sys.stdin.buffer.read(1))))[:-1],
                    '[': lambda d, p, i, brace_pairs: (p, brace_pairs[i] + 1 if not d[p] else i+1, ),
                    ']': lambda d, p, i, brace_pairs: (p, brace_pairs[i] + 1 if d[p] else i+1, ),
                }[ins[i]](data, ptr, i, bp), data, bp)
            )
        )
    )
)(
    ''.join(i for i in open(__import__('sys').argv[1]).read() if i in {'<', '>', '+', '-', '.', ',', '[', ']'}),
    (__import__('sys'), __import__('sys').setrecursionlimit(100000))[0],
)

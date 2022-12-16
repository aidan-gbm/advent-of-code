def solve(path: str):
    with open(path) as fd:
        stream = fd.readline()
    
    pkt_mark = 4
    while len(set(stream[pkt_mark-4:pkt_mark])) < 4:
        pkt_mark += 1

    msg_mark = 14
    while len(set(stream[msg_mark-14:msg_mark])) < 14:
        msg_mark += 1

    print('[+] Part 1:', pkt_mark)
    print('[+] Part 2:', msg_mark)

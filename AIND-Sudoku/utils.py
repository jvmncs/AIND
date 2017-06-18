def cross(A, B):
    "Cross product of elements in A and elements in B."
    return [s+t for s in A for t in B]

rows = 'ABCDEFGHI'
cols = '123456789'
boxes = cross(rows,cols)
row_units = [cross(r,cols) for r in rows]
col_units = [cross(rows,c) for c in cols]
square_units = [cross(rs,cs) for rs in ('ABC','DEF','GHI') for cs in ('123','456','789')]
diagonal_unit_lr = [rows[x]+cols[x] for x in range(9)]
diagonal_unit_rl = [rows[8-x]+cols[x] for x in range(9)]
unitlist = row_units+col_units+square_units+[diagonal_unit_lr]+[diagonal_unit_rl]
units = dict((s, [u for u in unitlist if s in u]) for s in boxes)
peers = dict((s, set(sum(units[s],[]))-set([s])) for s in boxes)
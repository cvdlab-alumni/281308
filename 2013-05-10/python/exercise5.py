# EXE 5

domain = GRID([25,25])

Pu0 = [(0,0,0),(0,0,1),(2,0,1),(2,0,0)]
Pu1 = [(0,1,0),(0,1,1),(2,1,1),(2,1,0)]
P0v = [(0,0,0),(0,0,1),(0,1,1),(0,1,0)]
P1v = [(2,0,0),(0,0,1),(2,1,1),(2,1,0)]
Dom1D = INTERVALS(1)(24)

cu0 = MAP(BEZIER(S1)(Pu0))(Dom1D)
cu1 = MAP(BEZIER(S1)(Pu1))(Dom1D)
c0v = MAP(BEZIER(S1)(P0v))(Dom1D)
c1v = MAP(BEZIER(S1)(P1v))(Dom1D)

Cu0 = BEZIER(S1)([Pu0])
Cu1 = BEZIER(S1)([Pu1])
Cua = [[0,0,1],[0,0,2],[1,0,2],[1,0,1]]
Cub = [[0,1,1],[0,1,2],[1,1,2],[1,1,1]]

pu0 = POLYLINE(Pu0)
pu1 = POLYLINE(Pu1)
p0v = POLYLINE(P0v)
p1v = POLYLINE(P1v)
#VIEW(STRUCT([cu0,pu0, cu1,pu1, c0v,p0v, c1v,p1v]))

C0v = BEZIER(S1)([Pu0])
C1v = BEZIER(S1)([Pu1])

mapping = BEZIER(S2)([Cu0, Cua,  Cub, Cu1])

VIEW(MAP(mapping)(domain)) 
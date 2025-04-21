from z3 import Ints, Solver, sat

def _pt1(pos, speed):
    cnt = 0
    lower = 200000000000000
    upper = 400000000000000
    for i in range(len(pos)):
        for k in range(i+1,len(pos)):
            xi,vix,yi,viy,xk,vkx,yk,vky = pos[i][0],speed[i][0],pos[i][1],speed[i][1],pos[k][0],speed[k][0],pos[k][1],speed[k][1]
            mi = viy/vix
            mk = vky/vkx
            bi = yi-mi*xi
            bk = yk-mk*xk
            if mi == mk:
                continue
            x_int = (bk-bi)/(mi-mk)
            y_int = mi*x_int + bi
            if (x_int-xi)*vix > 0 and (y_int-yi)*viy > 0 and (x_int-xk)*vkx > 0 and (y_int-yk)*vky > 0:
                if lower <= x_int <= upper and lower <= y_int <= upper:
                    cnt += 1
    print(cnt)

def _pt2(pos, speed):
    #couldn't find a way to solve this without a SAT module
    #used z3 as it's the best one for integer solutions
    #rock equations 
    #x = x0 + v_x*t
    #y = y0 + v_y*t
    #z = z0 + v_z*t
    xr,vxr,yr,vyr,zr,vzr = Ints('xr vxr yr vyr zr vzr')    
    s = Solver()
    l = locals()
    for i in range(len(pos)):
        var_str_x = 'x'+str(i)
        var_str_y = 'y'+str(i)
        var_str_z = 'z'+str(i)
        var_str_t = 't'+str(i)
        l[var_str_x],l[var_str_y],l[var_str_z],l[var_str_t] = Ints(f'{var_str_x} {var_str_y} {var_str_z} {var_str_t}')
        s.add(l[var_str_t] > 0)
        s.add(l[var_str_x] == xr + vxr*l[var_str_t], l[var_str_y] == yr + vyr*l[var_str_t],l[var_str_z] == zr + vzr*l[var_str_t])
        s.add(l[var_str_x] == pos[i][0] + speed[i][0]*l[var_str_t])
        s.add(l[var_str_y] == pos[i][1] + speed[i][1]*l[var_str_t])
        s.add(l[var_str_z] == pos[i][2] + speed[i][2]*l[var_str_t])
    if s.check() == sat:
        m = s.model()
        print(m[xr].as_long()+m[yr].as_long()+m[zr].as_long())

def run():    
    pos = []
    speed = []
    lines = open('input24.txt', 'r').read().splitlines()
    for line in lines:
        p,s = line.split(' @ ')
        pos.append([int(x) for x in p.split(', ')])
        speed.append([int(x) for x in s.split(', ')])
    _pt1(pos,speed)
    _pt2(pos,speed)

run()
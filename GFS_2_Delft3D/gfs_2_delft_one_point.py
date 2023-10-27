import numpy as np
from netCDF4 import Dataset as dat
import xarray as xr

tgtbase='saida'
#ufile='/mnt/c/Users/fernando.barreto/Downloads/eranovdec.nc'
#vfile='/mnt/c/Users/fernando.barreto/Downloads/eranovdec.nc'
ufile='/mnt/c/Users/fernando.barreto/Downloads/previsao_vento_u_20231027.nc'
vfile='/mnt/c/Users/fernando.barreto/Downloads/previsao_vento_v_20231027.nc'

fileu=xr.open_dataset(ufile)
filev=xr.open_dataset(vfile)


uv=fileu.interp(lat=-21.8166667 , lon=-40.5811111 + 360).ugrd10m.values
vv=filev.interp(lat=-21.8166667 , lon=-40.5811111 + 360).vgrd10m.values

def uv2vd_wind(u,v):
    vel = np.hypot(u,v)
    dire = np.arctan2(-u,-v) * 180/np.pi
    if isinstance(dire,xr.DataArray):
        direction = dire.values
        direction[direction<0] = direction[direction<0] + 360
        dire.values = direction
    else:
        dire[dire<0] = dire[dire<0] + 360
    return vel,dire

vel, dir=uv2vd_wind(uv, vv)

fileu.time[6:][0]
vel=vel[6:]
dir=dir[6:]

unet=dat(ufile)

vnet=dat(vfile)

intervalu = int( np.diff(unet['time'][::])[0]*24 )

intervalv = int( np.diff(vnet['time'][::])[0]*24 )

c=0
with open('vento_delft.wnd', 'w') as file: 
    # Iterate from 1 to 10
    for i in range(len(vel)):
        # Calculate the square and cube
        square = i ** 2
        cube = i ** 3
        # Write the values to the file with commas as separators
        file.write(f"{c},{np.round(vel[i], 2)},{np.round(dir[i], 2)}\n")
        c=c+ intervalu*60
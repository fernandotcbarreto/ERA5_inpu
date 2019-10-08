import numpy as np
from netCDF4 import Dataset as dat
import numpy as np

datest='2016-01-01'

tgtbase='saida'
pfile='download_cloud_10.nc'
pnet=dat(pfile)
intervalp = int( np.diff(pnet['time'][::])[0] )
p=np.squeeze(pnet['tcc'][::])*100
pwnd = tgtbase+'_era_5'+'.amc'
lonp = pnet['longitude'][::]
latp = pnet['latitude'][::]
dlatp=np.diff(latp)
dlonp=np.diff(lonp)
if (dlatp[0] < 0):
   dlatp=dlatp*(-1)
pfid = open(pwnd,'w');
pfid.write('FileVersion      = 1.03\n')
pfid.write('Filetype         = meteo_on_equidistant_grid\n')
pfid.write('NODATA_value         = -999.000\n')
pfid.write('n_cols           = %d\n' %(p.shape[2]) )
pfid.write('n_rows           = %d\n' %(p.shape[1]) )
pfid.write('grid_unit        = degree\n')
pfid.write('x_llcorner       = %f\n' %(lonp.min()) )
pfid.write('dx               = %f\n'% (dlonp[0]))
pfid.write('y_llcorner       = %f\n' %(latp.min()) )
pfid.write('dy               = %f\n'% (dlatp[0]))
pfid.write('n_quantity       = 1\n')
pfid.write('quantity1        = cloudiness\n')
pfid.write('unit1            = %\n')
[ntp,nip,njp] = p.shape;
c=0
for t in range(ntp):
  pfid.write('TIME = ' +str(c)+ ' hours since '+datest+ ' 00:00:00 +00:00\n')
  for i in range(nip):
     for j in range(njp):
       pfid.write('%15.5f'%(p[t,i,j]))
     pfid.write('\n')  
  c=c+intervalp
pfid.close()

############################################################################# humidity
tgtbase='saida'
pfile='download_humidity_10.nc'
pnet=dat(pfile)
intervalp = int( np.diff(pnet['time'][::])[0] )
p=np.squeeze(pnet['r'][::])
pwnd = tgtbase+'_era_5'+'.amd'
lonp = pnet['longitude'][::]
latp = pnet['latitude'][::]
dlatp=np.diff(latp)
dlonp=np.diff(lonp)
if (dlatp[0] < 0):
   dlatp=dlatp*(-1)
pfid = open(pwnd,'w');
pfid.write('FileVersion      = 1.03\n')
pfid.write('Filetype         = meteo_on_equidistant_grid\n')
pfid.write('NODATA_value         = -999.000\n')
pfid.write('n_cols           = %d\n' %(p.shape[2]) )
pfid.write('n_rows           = %d\n' %(p.shape[1]) )
pfid.write('grid_unit        = degree\n')
pfid.write('x_llcorner       = %f\n' %(lonp.min()) )
pfid.write('dx               = %f\n'% (dlonp[0]))
pfid.write('y_llcorner       = %f\n' %(latp.min()) )
pfid.write('dy               = %f\n'% (dlatp[0]))
pfid.write('n_quantity       = 1\n')
pfid.write('quantity1        = relative_humidity\n')
pfid.write('unit1            = %\n')
[ntp,nip,njp] = p.shape;
c=0
for t in range(ntp):
  pfid.write('TIME = ' +str(c)+ ' hours since '+datest+ ' 00:00:00 +00:00\n')
  for i in range(nip):
     for j in range(njp):
       pfid.write('%15.5f'%(p[t,i,j]))
     pfid.write('\n')  
  c=c+intervalp
pfid.close()



############################################################################# temperature

tgtbase='saida'
pfile='download_temperature_10.nc'
pnet=dat(pfile)
intervalp = int( np.diff(pnet['time'][::])[0] )
p=np.squeeze(pnet['t2m'][::]) - 273.15
pwnd = tgtbase+'_era_5'+'.amt'
lonp = pnet['longitude'][::]
latp = pnet['latitude'][::]
dlatp=np.diff(latp)
dlonp=np.diff(lonp)
if (dlatp[0] < 0):
   dlatp=dlatp*(-1)
pfid = open(pwnd,'w');
pfid.write('FileVersion      = 1.03\n')
pfid.write('Filetype         = meteo_on_equidistant_grid\n')
pfid.write('NODATA_value         = -999.000\n')
pfid.write('n_cols           = %d\n' %(p.shape[2]) )
pfid.write('n_rows           = %d\n' %(p.shape[1]) )
pfid.write('grid_unit        = degree\n')
pfid.write('x_llcorner       = %f\n' %(lonp.min()) )
pfid.write('dx               = %f\n'% (dlonp[0]))
pfid.write('y_llcorner       = %f\n' %(latp.min()) )
pfid.write('dy               = %f\n'% (dlatp[0]))
pfid.write('n_quantity       = 1\n')
pfid.write('quantity1        = air_temperature\n')
pfid.write('unit1            = Celsius\n')
[ntp,nip,njp] = p.shape;
c=0
for t in range(ntp):
  pfid.write('TIME = ' +str(c)+ ' hours since '+datest+ ' 00:00:00 +00:00\n')
  for i in range(nip):
     for j in range(njp):
       pfid.write('%15.5f'%(p[t,i,j]))
     pfid.write('\n')  
  c=c+intervalp
pfid.close()

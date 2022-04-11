import numpy as np
from pylab import *
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import seaborn as sns
import matplotlib.cm as cm
from matplotlib import rc,rcParams

def make_arrow(x,y,dx,dy,color,width=0.05):
	arrow = ax1.arrow(x,y,dx,dy,color=color,width=width)
	return arrow,

sns.set_context("talk")
sns.set_style("ticks")

rc('font', **{'family': 'Helvetica'})
rc('text', usetex=True)
matplotlib.rcParams.update({'font.size':50})
plt.rc('legend', **{'fontsize':7})

# Ticks to the outside:
rcParams['axes.linewidth'] = 3.0
rcParams['xtick.direction'] = 'out'
rcParams['ytick.direction'] = 'out'

Writer = animation.writers['ffmpeg']
writer = Writer(fps=30, metadata=dict(artist='Me'), bitrate=1800)
#fig = plt.figure()
fig = plt.figure(figsize=(15,20))

ax1 = fig.add_subplot(411)
ax2 = fig.add_subplot(412)
ax3 = fig.add_subplot(413)
ax4 = fig.add_subplot(414)
m0 = 1.
F0 = 1.

def Force(x):
	if x > 0:
		F = -F0
	elif x < 0:
		F = F0
	else:
		F = 0
	return F

def acc(x):
	return Force(x)/m0

def vel(x,vi,t):
	return vi + a(x)*t

x0 = 3.
vi0 = 0.

dt = 0.001
ts = np.arange(0,20,dt)

t = 0
xss = [x0]
vss = [vi0]
ass = [acc(x0)]
x = x0
v = vi0
a = acc(x0)

ax1.axhline(0)
ax2.axhline(0)
ax3.axhline(0)
ax4.axhline(0)


ax1.axvline(0)
ax1.set_ylim([-1,1])

ax1.set_xlabel(r'x [m]')
ax2.set_ylabel(r'a [m/s$^2$]')
ax3.set_ylabel(r'v [m/s]')
ax4.set_ylabel(r'x [m]')
ax4.set_xlabel(r't [s]')


ims = []
tts = [0]
count = 0
for t in ts:
	x = x + v*dt + a*dt*dt/2.
	v = v + a*dt
	a = acc(x)
	if count % 100 == 0:
		im, = ax1.plot(x,0,'ro',markersize=80)
		im2, = ax2.plot(tts,ass,'b',linewidth=6)
		im5, = ax2.axvline(tts[-1]),
		im3, = ax3.plot(tts,vss,'b',linewidth=6)
		im6, = ax3.axvline(tts[-1]),
		im4, = ax4.plot(tts,xss,'b',linewidth=6)
		im7, = ax4.axvline(tts[-1]),
		force, = make_arrow(x,0,Force(x),0,'black')
		ims.append([im,im2,im3,im4,im5,im6,im7,force])
	xss.append(x)
	vss.append(v)
	ass.append(a)
	tts.append(t)
	count+=1
ax1.tick_params(axis='y', labelsize=30)
ax2.tick_params(axis='y', labelsize=30)
ax3.tick_params(axis='y', labelsize=30)
ax4.tick_params(axis='y', labelsize=30)
ax1.tick_params(axis='x', labelsize=30)
ax2.tick_params(axis='x', labelsize=30)
ax3.tick_params(axis='x', labelsize=30)
ax4.tick_params(axis='x', labelsize=30)
fig.tight_layout()
ani = animation.ArtistAnimation(fig, ims, interval=50, blit=True, repeat_delay=1000)
ani.save('osc1.mp4', writer=writer)

#print(x,y)
#plot(xs,ys,'ro')
plt.show()


#plot(ts,xss[:-1])
#show()




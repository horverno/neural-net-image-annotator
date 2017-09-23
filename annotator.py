import numpy as np
import cv2
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.widgets import Button
from matplotlib.patches import Polygon
from matplotlib.collections import PatchCollection
from os import walk

class LineBuilder:
    ind = 1
    poly = []
    def __init__(self, line):
        self.line = line
        self.xs = []#list(line.get_xdata())
        self.ys = []#list(line.get_ydata())
        self.cid = line.figure.canvas.mpl_connect('button_press_event', self)
        

    def __call__(self, event):
        #print('click:', event)
        if event.inaxes!=self.line.axes: return
        self.xs.append(event.xdata)
        self.ys.append(event.ydata)
        self.poly.append([event.xdata, event.ydata])
        #axes[1].cla()
        #axes[1].imshow(img1, cmap = 'gray', interpolation = 'bicubic')
        if np.shape(self.xs)[0] > 1:
            #axes[1].fill_between(self.xs, self.ys,color="green", alpha=0.5)
            self.line.set_data(self.xs, self.ys)
            self.line.figure.canvas.draw()
            #print(self.poly)
            patches = []
            polygon = Polygon(self.poly, True)
            patches.append(polygon)
            if self.ind == 0:
                c = '#781d8e'
            elif self.ind == 1:
                c = '#f2e835'
                print("printing line")
            elif self.ind == 2:
                c = '#4286f4'
            else:
                c = '#C0FFEE'
            p = PatchCollection(patches, color=c, alpha=0.4)
            axes[1].add_collection(p)
        
    def clear(self):
        self.ind = 1
        self.poly = []
        self.xs = []
        self.ys = []
        self.line.set_data(self.xs, self.ys)
        
    def next(self, event):
        self.ind += 1
        self.poly = []
        self.xs = []
        self.ys = []
        print(self.ind)

    def prev(self, event):
        self.ind -= 1
        print(self.ind)

    def save(self, event):
        dpi = 80
        im_data = img1
        height, width, nbands = im_data.shape
        # What size does the figure need to be in inches to fit the image?
        figsize = width / float(dpi), height / float(dpi)
        # Create a figure of the right size with one axes that takes up the full figure
        fig2 = plt.figure(figsize=figsize)
        ax = fig2.add_axes([0, 0, 1, 1])
        # Hide spines, ticks, etc.
        ax.axis('off')
        # Display the image.
        #a = plt.gca()
        ax.imshow(im_data, interpolation='nearest')
        # Ensure we're displaying with square pixels and the right extent.
        # This is optional if you haven't called `plot` or anything else that might
        # change the limits/aspect.  We don't need this step in this case.
        ax.set(xlim=[0, width], ylim=[height, 0], aspect=1)
        if np.shape(self.xs)[0] > 1:
            #axes[1].fill_between(self.xs, self.ys,color="green", alpha=0.5)
            self.line.set_data(self.xs, self.ys)
            self.line.figure.canvas.draw()
            #print(self.poly)
            patches = []
            polygon = Polygon(self.poly, True)
            patches.append(polygon)
            if self.ind == 0:
                c = '#781d8e'
            elif self.ind == 1:
                c = '#f2e835'
            elif self.ind == 2:
                c = '#4286f4'
            else:
                c = '#C0FFEE'
            p = PatchCollection(patches, color=c, alpha=0.4)
            axes[1].add_collection(p)
        fig2.savefig(str(position) + '.jpg', dpi=dpi, transparent=True)
        #plt.show()
        #fig.set_size_inches(30, fig.get_figheight(), forward=True)
        print("saved %dx%d" % (width, height) )
        
                
# Get file names
path = "test\\inp\\"
files = []
position = 0
for (dirpath, dirnames, filenames) in walk(path):
    files.extend(filenames)
    break

def load_next_image(event):
    global position
    position += 1
    
    if position >= len(files):
        print("No more files")
    else:
        global img1
        global line
        global patches
        global polygon
        global fig, axes, p, plt
    
        print("Load next image: " + files[position])

        img1 = cv2.imread(path + files[position])
        img1 = img1[:,:,::-1]
        axes[0].imshow(img1, interpolation = 'bicubic')
        axes[1].cla()
        plt.setp(axes, xticks=[], yticks=[])
        axes[1].imshow(img1[:,:,0], cmap= "Purples_r", interpolation = 'bicubic')
        fig.canvas.set_window_title("Neural net image annotator - " + files[position])
        
        linebuilder.clear()
        
fig, axes = plt.subplots(1, 2, figsize=(16,6))
plt.subplots_adjust(bottom=0.2)
img1 = cv2.imread(path + files[position])
img1 = img1[:,:,::-1]
axes[0].imshow(img1, interpolation = 'bicubic')
axes[1].imshow(img1[:,:,0], cmap= "Purples_r", interpolation = 'bicubic')
fig.canvas.set_window_title("Neural net image annotator - " + files[position])

axes[0].set_title("click to annotate")
axes[1].set_title("preview")
line, = axes[0].plot([0], [0])  # empty line
linebuilder = LineBuilder(line)
plt.setp(axes, xticks=[], yticks=[]) # to hide tick values on X and Y axis
axes[0].set_axis_off() , axes[1].set_axis_off() # to hide border

patches = []
polygon = Polygon([[-1,-1], [-1,-1], [-1,-1]], True)
patches.append(polygon)
p = PatchCollection(patches, cmap=matplotlib.cm.jet, alpha=0.4)
axes[1].add_collection(p)

axsave = plt.axes([0.81, 0.05, 0.1, 0.075])
axnext = plt.axes([0.7, 0.05, 0.1, 0.075])
axnextimage = plt.axes([0.25, 0.05, 0.1, 0.075])

bnextimage = Button(axnextimage, 'Next image')
bnextimage.on_clicked(load_next_image)
bnext = Button(axnext, 'Next')
bnext.on_clicked(linebuilder.next)
bprev = Button(axsave, 'Save')
bprev.on_clicked(linebuilder.save)

plt.show()

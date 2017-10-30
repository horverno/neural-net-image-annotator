import numpy as np
import cv2
import tkinter
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.widgets import Button
from matplotlib.patches import Polygon
from matplotlib.collections import PatchCollection
from os import walk

class LineBuilder:
    ind = 1
    poly = []
    poly1 = []
    poly2 = []
    poly3 = []
    poly4 = []
    poly5 = []
    poly6 = []
    poly7 = []
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
                c = '#000000'
            elif self.ind == 1:
                c = '#014080'
                self.poly1.append([event.xdata, event.ydata])
            elif self.ind == 2:
                c = '#02ff80'
                self.poly2.append([event.xdata, event.ydata])
            elif self.ind == 3:
                c = '#02ff80'
                self.poly3.append([event.xdata, event.ydata])
            elif self.ind == 4:
                c = '#02ff80'
                self.poly4.append([event.xdata, event.ydata])
            elif self.ind == 5:
                c = '#038fff'
                self.poly5.append([event.xdata, event.ydata])
            elif self.ind == 6:
                c = '#038fff'
                self.poly6.append([event.xdata, event.ydata])
            elif self.ind == 7:
                c = '#038fff'
                self.poly7.append([event.xdata, event.ydata])
            p = PatchCollection(patches, color=c, alpha=0.4)
            axes[1].add_collection(p)
        
    def clear(self):
        self.ind = 1
        self.poly = []
        self.poly1 = []
        self.poly2 = []
        self.poly3 = []
        self.poly4 = []
        self.poly5 = []
        self.poly6 = []
        self.poly7 = []
        self.xs = []
        self.ys = []
        self.line.set_data(self.xs, self.ys)
        
    def undo(self):
        if self.ind == 1:
            self.poly1 = []
        if self.ind == 2:
            self.poly2 = []
        if self.ind == 3:
            self.poly3 = []
        if self.ind == 4:
            self.poly4 = []
        if self.ind == 5:
            self.poly5 = []
        if self.ind == 6:
            self.poly6 = []
        if self.ind == 7:
            self.poly = []
            
        self.poly = []
        self.xs = []
        self.ys = []
        self.line.set_data(self.xs, self.ys)    
    
    def next(self, event):
        self.ind += 1
        global fig
        if self.ind == 2:
            fig.canvas.set_window_title("Neural net image annotator - Akadály megjelölése #1")
        if self.ind == 3:
            fig.canvas.set_window_title("Neural net image annotator - Akadály megjelölése #2")
        if self.ind == 4:
            fig.canvas.set_window_title("Neural net image annotator - Akadály megjelölése #3")
        if self.ind == 5:
            fig.canvas.set_window_title("Neural net image annotator - Határoló megjelölése")

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
        fig3 = plt.figure(figsize=figsize)
        ax = fig2.add_axes([0, 0, 1, 1])
        ax2 = fig3.add_axes([0, 0, 1, 1])
        # Hide spines, ticks, etc.
        ax.axis('off')
        ax.imshow(im_data, interpolation='nearest')
        ax2.axis('off')
        ax2.imshow(im_data, interpolation='nearest')
        # Ensure we're displaying with square pixels and the right extent.
        # This is optional if you haven't called `plot` or anything else that might
        # change the limits/aspect.  We don't need this step in this case.
        ax.set(xlim=[0, width], ylim=[height, 0], aspect=1)
        #ax2.set(xlim=[0, width], ylim=[height, 0], aspect=1)
        
        if np.shape(self.xs)[0] > 1:
            #axes[1].fill_between(self.xs, self.ys,color="green", alpha=0.5)
            
            self.line.set_data(self.xs, self.ys)
            self.line.figure.canvas.draw()
            patches0 = []
            patches1 = []
            patches2 = []
            patches3 = []
            patches4 = []
            patches5 = []
            patches6 = []
            patches7 = []
            
            poly0 = []
            poly0.append([0, 0])
            poly0.append([0, width])
            poly0.append([width, width])
            poly0.append([width, 0])
            polygon0 = Polygon(poly0, True)
            patches0.append(polygon0)
            
            polygon1 = Polygon(self.poly1, True)
            patches1.append(polygon1)
            if len(self.poly2) > 0:
                polygon2 = Polygon(self.poly2, True)
                patches2.append(polygon2)
            if len(self.poly3) > 0:
                polygon3 = Polygon(self.poly3, True)
                patches3.append(polygon3)
            if len(self.poly4) > 0:
                polygon4 = Polygon(self.poly4, True)
                patches4.append(polygon4)
            if len(self.poly5) > 0:
                polygon5 = Polygon(self.poly5, True)
                patches5.append(polygon5)
            if len(self.poly6) > 0:
                polygon6 = Polygon(self.poly6, True)
                patches6.append(polygon6)
            if len(self.poly7) > 0:
                polygon7 = Polygon(self.poly7, True)
                patches7.append(polygon7)
                
            # Mer - Ellenorzeshez
            ax2.add_collection(PatchCollection(patches1, color='#014080', alpha=0.4))
            ax2.add_collection(PatchCollection(patches5, color='#038fff', alpha=0.4))
            ax2.add_collection(PatchCollection(patches6, color='#038fff', alpha=0.4))
            ax2.add_collection(PatchCollection(patches7, color='#038fff', alpha=0.4))
            ax2.add_collection(PatchCollection(patches2, color='#02ff80', alpha=0.4))
            ax2.add_collection(PatchCollection(patches3, color='#02ff80', alpha=0.4))
            ax2.add_collection(PatchCollection(patches4, color='#02ff80', alpha=0.4))

            # Hatter
            for patch0 in patches0:
                patch0.set_color('#000000')
                patch0.alpha=0.4
                ax.add_patch(patch0)
                
            # Ut kategoria
            for patch1 in patches1:
                patch1.set_color('#014080')
                patch1.alpha=0.4
                ax.add_patch(patch1)
            
            # Hatarolo
            for patch5 in patches5:
                patch5.set_color('#038fff')
                patch5.alpha=0.4
                ax.add_patch(patch5)
            
            # Hatarolo
            for patch6 in patches6:
                patch6.set_color('#038fff')
                patch6.alpha=0.4
                ax.add_patch(patch6)
        
            # Hatarolo
            for patch7 in patches7:
                patch7.set_color('#038fff')
                patch7.alpha=0.4
                ax.add_patch(patch7)
  
            # Jarmu vagy egyeb uton levo targy
            for patch2 in patches2:
                patch2.set_color('#02ff80')
                patch2.alpha=0.4
                ax.add_patch(patch2)
                
            # Jarmu vagy egyeb uton levo targy
            for patch3 in patches3:
                patch3.set_color('#02ff80')
                patch3.alpha=0.4
                ax.add_patch(patch3)
                
            # Jarmu vagy egyeb uton levo targy
            for patch4 in patches4:
                patch4.set_color('#02ff80')
                patch4.alpha=0.4
                ax.add_patch(patch4)

        ax.imshow(img1[:,:,0])
        #ax.imshow(img1[:,:,0], cmap= "Purples_r", interpolation = 'bicubic')
 

        fig2.savefig("test\\out\\" + files[position], dpi=dpi)
        fig3.savefig("test\\mer\\" + files[position], dpi=dpi)
        plt.show()
        #fig2.set_size_inches(30, fig.get_figheight(), forward=True)
        print("saved %dx%d" % (width, height) )
        
# Get file names
pathTest = "test\\inp\\"
pathVal = "val\\inp\\"
pathTrain = "train\\inp\\"
files = []
filesPath = []
position = 0
for (dirpath, dirnames, filenames) in walk(pathTest):
    files.extend(filenames)
    for _ in range(0,len(filenames)):
        filesPath.append(pathTest)
    break
for (dirpath, dirnames, filenames) in walk(pathVal):
    files.extend(filenames)
    filesPath.append(pathVal)
    break
for (dirpath, dirnames, filenames) in walk(pathTrain):
    files.extend(filenames)
    filesPath.append(pathTrain)
    break
def load_next_image(event):
    global position
    if position + 1 >= len(files) or position + 1 >= len(filesPath):
        print("No more files")

    else:
        global img1
        global fig, axes, plt
    
        position += 1
        print("Load next image: " + filesPath[position] + files[position])

        img1 = cv2.imread(filesPath[position] + files[position])
        img1 = img1[:,:,::-1]
        axes[0].imshow(img1, interpolation = 'bicubic')
        axes[1].cla()
        plt.setp(axes, xticks=[], yticks=[])
        axes[1].imshow(img1[:,:,0], cmap= "Purples_r", interpolation = 'bicubic')
        fig.canvas.set_window_title("Neural net image annotator - " + "Út megjelölése")
        
        linebuilder.clear()
        
def undo(event):
    axes[0].imshow(img1, interpolation = 'bicubic')
    axes[1].cla()
    plt.setp(axes, xticks=[], yticks=[])
    axes[1].imshow(img1[:,:,0], cmap= "Purples_r", interpolation = 'bicubic')
    
    linebuilder.undo()

fig, axes = plt.subplots(1, 2, figsize=(16,6))
plt.subplots_adjust(bottom=0.2)
img1 = cv2.imread(filesPath[position] + files[position])

print(filesPath[position] + files[position])

img1 = img1[:,:,::-1]
axes[0].imshow(img1, interpolation = 'bicubic')
axes[1].imshow(img1[:,:,0], cmap= "Purples_r", interpolation = 'bicubic')
fig.canvas.set_window_title("Neural net image annotator - " + "Út megjelölése")

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
axundo = plt.axes([0.05, 0.05, 0.1, 0.075])

bnextimage = Button(axnextimage, 'Next image')
bnextimage.on_clicked(load_next_image)
bundo = Button(axundo, 'Undo')
bundo.on_clicked(undo)
bnext = Button(axnext, 'Next annotation type')
bnext.on_clicked(linebuilder.next)
bprev = Button(axsave, 'Save')
bprev.on_clicked(linebuilder.save)

plt.show()

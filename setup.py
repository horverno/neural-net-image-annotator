import cx_Freeze
import os
import tkinter.filedialog

executables = [cx_Freeze.Executable("annotator.py")]

##Change these to your paths
include_files = [r"C:\Users\BB\AppData\Local\Programs\Python\Python36\DLLs\tcl86t.dll",
                 r"C:\Users\BB\AppData\Local\Programs\Python\Python36\DLLs\tk86t.dll"]
##Change these to your paths
os.environ['TCL_LIBRARY'] = r'C:\Users\BB\AppData\Local\Programs\Python\Python36\tcl\tcl8.6'
os.environ['TK_LIBRARY'] = r'C:\Users\BB\AppData\Local\Programs\Python\Python36\tcl\tk8.6'

cx_Freeze.setup(
    name="Deep Pilot Annotator",
    version = "0.1",
    options={"build_exe":{"packages":["cv2","matplotlib","numpy","tkinter"],
                          "include_files":include_files}},
    executables = executables
    )

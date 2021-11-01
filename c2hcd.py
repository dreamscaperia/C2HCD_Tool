# Auther: dreamscaperia
# Version: 1.0
# Title: C2HCD Tool
# Desc: Convert WICED Bluetooth firmware/RAM_patch from *.c format to *.hcd format.
import sys
#print(sys.argv)
if len(sys.argv) == 2:
    f = open(sys.argv[1], "r")
    fstr = f.read()
    fout = open('out.hcd', "wb")
    import re
    blockpattern = re.compile("brcm_patchram_buf.*\};", re.DOTALL)
    searchobj = re.findall('(?<=0x)(\w\w)(?!;)', blockpattern.findall(fstr)[0])
    for item in searchobj:
        fout.write(bytearray.fromhex(item))
    fout.close()
    f.close()
else:
    print("Param Error.\nUsage:\n   python c2hcd.py bt_firmware_controller.c")
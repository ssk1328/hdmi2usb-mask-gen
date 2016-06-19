The python functions should be able convert a image to streams of (1,0) which can be encoded using a suitable run length encoding function. 
Also able to generate the image back from rle encoded pixel data.

### repeat.py

This defines recursive repeat function which can be used to generate wipes in the manner as explained in the hardware fader design doc. Currently four function are defined to generate horizoantal, vertical, horizoantal_fuzzy and vertical_fuzzy wipe.


### mask_gen.py

This defines function to convert a standard jped image to a 1D list of size resolution og image

### rle2.py

This is a script that implements a very crude way of doing run length encoding. This starts with an image file, run length encodes it, decodes it using similar operation and returns the same image file.
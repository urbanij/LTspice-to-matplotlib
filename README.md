# LTspice to matplotlib plot
This code snippet allows exporting an LTspice plot to Python and visualize it using Matplotlib. <br>
This transposition is useful because it allows further manipulation over the dataset, which turns out to be often intricate within LTspice itself.

## Usage:
#### plot:
Once exported the data from LTspice in a `.txt` file, just type: 
```sh
python plot_LTspice.py dataset/dataset/Draft2.txt
```

#### fft plot:
Make sure to export the data as `(re,im)` and not `(mag, arg)` although the final plot will be of course a polar plot. Save the dataset as a `.txt` file as well – (actually `.fft.txt`) and type:
```sh
python plot_LTspice_fft.py dataset/dataset/Draft2.fft.txt
```
to visualize the plot.
<br>
<br>

## Screenshots:

![alt text](https://www.dropbox.com/s/0asc18k1w449z2p/plot_ltspice.png?raw=1)



![alt text](https://www.dropbox.com/s/t4uzaupe10hv2f1/plot_matplotlib.png?raw=1)

---

![alt text](https://www.dropbox.com/s/clr556ufmksr1o8/plot_ltspice_fft.png?raw=1)

![alt text](https://www.dropbox.com/s/jf8r0bit99pvo6v/plot_matplotlib_fft.png?raw=1)
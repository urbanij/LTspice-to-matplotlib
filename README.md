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


![alt text](https://raw.githubusercontent.com/urbanij/LTspice-to-matplotlib/master/img/plot_ltspice.png?raw=true)

![alt text](https://raw.githubusercontent.com/urbanij/LTspice-to-matplotlib/master/Draft2.txt.svg?raw=true)

---

![alt text](https://raw.githubusercontent.com/urbanij/LTspice-to-matplotlib/master/img/plot_ltspice_fft.png?raw=true)


![alt text](https://raw.githubusercontent.com/urbanij/LTspice-to-matplotlib/master/Draft2.fft.txt.svg?raw=true)

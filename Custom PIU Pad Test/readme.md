For testing a home-made, keyboard based, PIU pad.

By default, it has "V","R","D","M", and "U" as the inputs for UL, UR, C, DL, and DR, respectively, as for some reason that's how the pad I got had its buttons mapped. However, you can change this editing the file or running it through a command window:  

```python cpad_test.pyw UL UR C DL DR```

For example:  

```python cpad_test.pyw Q E S Z C``` works for the usual QESZC mapping.  

The ```.pyw``` extension makes it so a command prompt doesn't open by double clicking on it, and only the UI shows.  
The files in ```images/``` are essential, though they could be replaced by solid colors
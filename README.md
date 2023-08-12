## QR Code generator in Python
 
Easy QR Code generator totally customizable.

## Setup
To run this project check if you have Python installed and install the ``qrcode`` package locally using pip command.
```
pip install qrcode
```
For more image customization and functionality, make sure to install ``pil`` dependency so
that pillow is installed and can be used for generating images.
```
pip install "qrcode[pil]"
```
## Logo
You can change the logo in the middle of the image by simply modifying ``logo.png`` path or replacing the image.

```python
embeded_image_path=".\img\logo.png"
```
<p align="center">
<img src=https://github.com/FernaandoJr/python-qrcode-generator/assets/90939363/a5f871d0-a978-407c-9b32-7fb971ca0c61 width=300 height=300>
</p>
<p align="center">For a more easy scannable QR Code, try adding a stroke around the logo, like the example above</p>


## References
It's important to read the original repository documentation for more information about the package.

* [python-qrcode](https://github.com/lincolnloop/python-qrcode)
* [How to add logo](https://medium.com/codestorm/how-to-create-qr-code-using-python-2094dc7e3db6#:~:text=or%20place%20an%20image%20in%20the%20middle%20of%20the%20QR%20Code%20to%20be%20created%2C)

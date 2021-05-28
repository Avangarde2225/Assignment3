"""
File: bluescreen.py
----------------
Not part of the assignment. This was a lecture demo!
This is a fun algorithm to implement. It is not in the
assignment, but feel free to implement it as an extension.
Put the smaller foreground picture into the background.
Do not include any pixels that are sufficiently blue.
"""

from simpleimage import SimpleImage


def main():
    foreground = SimpleImage('images/tiefighter.jpg')
    background = SimpleImage('images/quad.jpg')
    # TODO: your code here
    #background.show()
    foreground.show()
    darker(foreground)
    foreground.show()
    print(foreground.width)
    print(foreground.height)



def darker(image):
    for pixel in image:
        pixel.blue = pixel.blue



if __name__ == '__main__':
    main()
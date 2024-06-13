# PandaRender

A simple collection of Python methods designed to be used with Panda3D that scale up the ShowBase window in order
to take higher resolution screenshots. These screenshots can (on Windows, at least) go beyond the bounds of your monitor
size and the method will handle sizing it back to what it was before.

I made this for a friend who wanted to grab some high-resolution images of some Toontown models.

> [!IMPORTANT]  
> These methods will not do anything if Panda3D fails to scale to the desired window size, for any reason. This mostly
> happens when you're scaling the window past the bounds of your monitor. I haven't tested this on any platform other 
> than Windows 10, and it's generally thrown together, so your mileage may vary.


## Methods

### resize_and_screenshot

Method that changes the active ShowBase window's width and height to w and h respectively, 
takes a screenshot, and saves it to screenshot_name, before returning to the previous size.

| Parameter       | Description                                         |
|-----------------|-----------------------------------------------------|
| w               | The desired width of the screenshot.                |
| h               | The desired height of the screenshot.               |
| screenshot_name | The name (and, optionally, path) of the screenshot. |

### scale_and_screenshot
Method that gets the current size of the window, scales the width and height by w and h respectively, 
takes a screenshot, and saves it to screenshot_name, before returning to the previous size.

| Parameter       | Description                                         |
|-----------------|-----------------------------------------------------|
| w               | The factor of which the width will be multiplied.                |
| h               | The factor of which the height will be multiplied.               |
| screenshot_name | The name (and, optionally, path) of the screenshot. |
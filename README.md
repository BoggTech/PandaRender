# PandaRender

A simple collection of Python methods designed to be used with Panda3D that scale up the ShowBase window in order
to take higher resolution screenshots. These screenshots can (on Windows, at least) go beyond the bounds of your monitor
size and the method will handle sizing it back to what it was before.

I made this for a friend who wanted to grab some high-resolution images of some Toontown models.

> [!IMPORTANT]  
> Some platforms will not allow the ShowBase instance to extend beyond the bounds of your monitor and, as a result,
> these methods may fail. Read the "Events" section for more information.


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

# Events

When the screenshot is (or is attempted to be) taken, the event ```pandarender-complete``` occurs. This event comes with
a boolean parameter that states whether or not the screenshot was taken. If this value is false, it means the screenshot
was not taken because the window was not scaled to the specified size. Usually this means the platform you are running
Panda3D stopped the window from scaling to the desired size, probably because you've gone beyond the bounds of your
monitor and it doesn't allow that. You can use this event to detect when this happens.
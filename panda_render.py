from panda3d.core import WindowProperties
from direct.task import Task
from direct.showbase.DirectObject import DirectObject


def __resize_window(w, h):
    """Method that resizes the ShowBase window.

    :param w: The desired width of the window.
    :param h: The desired height of the window.
    """
    props = WindowProperties()
    props.setSize(w, h)
    base.win.requestProperties(props)


def resize_and_screenshot(w, h, screenshot_name="PandaRender.png"):
    """Method that changes the active ShowBase window's width and height to w and h respectively,
    takes a screenshot, and saves it to screenshot_name, before returning to the previous size.

    :param w: The desired width of the screenshot.
    :param h: The desired height of the screenshot.
    :param screenshot_name: The name (and, optionally, path) of the screenshot.
    """
    prev_w, prev_h = base.win.getXSize(), base.win.getYSize()
    do = DirectObject()
    do.acceptOnce("window-event", __screenshot, extraArgs=[w, h, prev_w, prev_h, screenshot_name])
    __resize_window(w, h)


def scale_and_screenshot(w, h, screenshot_name):
    """Method that gets the current size of the window, scales the width and height by w and h respectively,
    takes a screenshot, and saves it to screenshot_name, before returning to the previous size.

    :param w: The factor of which the width will be multiplied.
    :param h: The factor of which the height will be multiplied.
    :param screenshot_name: The name (and, optionally, path) of the screenshot.
    """
    x, y = base.win.getXSize(), base.win.getYSize()
    resize_and_screenshot(x * w, y * h, screenshot_name)


def __screenshot(w, h, prev_w, prev_h, screenshot_name, *args):
    """Method that checks if the ShowBase window's bounds are [w, h] before rendering the frame and taking a screenshot.
    If this check fails, nothing is done. After taking a screenshot, the window is scaled to [prev_w, prev_h].

    :param w: The desired width of the screenshot.
    :param h: The desired height of the screenshot.
    :param prev_w: The width to revert to when the screenshot has been taken.
    :param prev_h: The height to revert to when the screenshot has been taken.
    :param screenshot_name: The name (and, optionally, path) of the screenshot."""

    curr_w, curr_h = base.win.getProperties().getXSize(), base.win.getProperties().getYSize()
    if curr_w == w and curr_h == h:
        base.graphicsEngine.renderFrame()
        base.screenshot(screenshot_name, False)
    __resize_window(prev_w, prev_h)

from direct.task import Task
from panda3d.core import WindowProperties


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
    __resize_window(w, h)
    # not sure why it's trying to pass an argument to the lambda so x does nothing but prevent error. tasks are weird
    taskMgr.add(__screenshot_task, "PandaRender", extraArgs=[w, h, screenshot_name],
                uponDeath=lambda x: __resize_window(prev_w, prev_h))


def scale_and_screenshot(w, h, screenshot_name):
    """Method that gets the current size of the window, scales the width and height by w and h respectively,
    takes a screenshot, and saves it to screenshot_name, before returning to the previous size.

    :param w: The factor of which the width will be multiplied.
    :param h: The factor of which the height will be multiplied.
    :param screenshot_name: The name (and, optionally, path) of the screenshot.
    """
    x, y = base.win.getXSize(), base.win.getYSize()
    resize_and_screenshot(x * w, y * h, screenshot_name)


def __screenshot_task(w, h, screenshot_name):
    """Task that waits for the ShowBase window's bounds to be [w, h] before taking a screenshot.

    :param w: The desired width of the screenshot.
    :param h: The desired height of the screenshot.
    :param screenshot_name: The name (and, optionally, path) of the screenshot."""
    curr_w, curr_h = base.win.getProperties().getXSize(), base.win.getProperties().getYSize()

    if curr_w != w or curr_h != h:
        return Task.cont
    else:
        base.graphicsEngine.renderFrame()
        base.screenshot(screenshot_name, False)
        return Task.done


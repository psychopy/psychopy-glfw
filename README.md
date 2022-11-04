# psychopy-wintype-glfw
GLFW window backend plugin for PsychoPy

This plugin adds GLFW as a supported `winType` for PsychoPy once loaded. You can enable using GLFW by specifying it as 
the `winType` when creating a new window. 

## Example

Creating a window using GLFW as the backend::

    import psychopy.visual as visual
    win = visual.Window(winType='gflw')

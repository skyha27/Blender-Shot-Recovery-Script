import os as OS
import bpy

# Global variables
output_folder = r"C:\Users\person\Desktop\folder" # example output folder path
seconds_to_render = 45 # amount of seconds to render frame
count = 1

print("--Starting viewport render.--")

# Function to screenshot viewport and save image
def screenshot():
    global count
    path = OS.path.join(output_folder, f"{count}.png")
    bpy.ops.screen.screenshot(filepath=path)
    print(f"Saved image {count}.png")
    bpy.context.scene.frame_current += 1
    count+=1

    # end capture after sequence end
    if count > bpy.context.scene.frame_end:
        print("--Finished viewport render.--")
        return None
    return seconds_to_render

# Swap window from scripting to viewport
bpy.context.window.workspace = bpy.data.workspaces['Layout']

#Run screenshot() after frame has finished rendering
bpy.app.timers.register(screenshot, first_interval=seconds_to_render)



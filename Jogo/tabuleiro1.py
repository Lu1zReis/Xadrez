"""
Example "Arcade" library code.

Showing how to do nested loops.

If Python and Arcade are installed, this example can be run from the command line with:
python -m arcade.examples.nested_loops_box
"""

# Library imports
import arcade

COLUMN_SPACING = 20
ROW_SPACING = 20
LEFT_MARGIN = 160
BOTTOM_MARGIN = 160

# Open the window and set the background
arcade.open_window(450, 450, "Xadrez - Box")

arcade.set_background_color(arcade.color.WHITE)

# Start the render process. This must be done before any drawing commands.
arcade.start_render()

# Loop for each row
for row in range(8):
    # Loop for each column
    aux = 0
    if row % 2 == 0:
        aux = 0
    else:
        aux = 1
    for column in range(8):
        # Calculate our location
        x = column * COLUMN_SPACING + LEFT_MARGIN
        y = row * ROW_SPACING + BOTTOM_MARGIN

        # Draw the item
        # arcade.draw_circle_filled(x, y, 7, arcade.color.AO)
        if column % 2 == aux:
            arcade.draw_point(x, y, arcade.color.AO, 20)
        else:
            arcade.draw_point(x, y, arcade.color.ARYLIDE_YELLOW, 20)

# Finish the render.
arcade.finish_render()

# Keep the window up until someone closes it.
arcade.run()

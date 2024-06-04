import arcade
import arcade.gui

resolucao_x = 400
resolucao_y = 400
"""
    CONFIGURAÇÕES
"""
# Open the window. Set the window title and dimensions (width and height)
arcade.open_window(resolucao_x, resolucao_y, "Xadrez")
# fundo
arcade.set_background_color(arcade.color.MOONSTONE_BLUE)

arcade.start_render()
manager = arcade.gui.UIManager()
manager.enable()

v_box = arcade.gui.UIBoxLayout()

entrada = arcade.gui.UITextArea(text="This is a Text Widget",
                                              width=450,
                                              height=40,
                                              font_size=24,
                                              font_name="Kenney Future")

v_box.add(entrada)
ui_flatbutton = arcade.gui.UIFlatButton(text="Flat Button", width=200)
v_box.add(ui_flatbutton.with_space_around(bottom=20))
arcade.finish_render()
arcade.run()

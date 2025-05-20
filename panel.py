from horizon import panel

class FlatPlugin(panel.Panel):
    name = "Flat"
    slug = "flat_plugin"

panel.Default.register(FlatPlugin)

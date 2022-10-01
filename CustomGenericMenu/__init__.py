bl_info = {
    "name" : "Custom Generic Menu",
    "author" : "Thanh Toan",
    "version": (1, 0),
    "blender": (2, 93, 1),
    "location": "Followed Hotkey Menu",
    "description": "ctrl + alt + shift + T",
    "warning": "",
    "wiki_url": "",
    "category": "3D View"
}



from symbol import shift_expr
import bpy
from bpy.props import *

from .CGM_UV_Ops import *
from .CGM_Menu import *
from .CGM_Rename_Ops import *
from .CGM_Normals_Ops import *

bpy.types.Scene.my_list = []

addon_keymaps = []

## REGISTER ##

classes = (
    # Menu classes
    customUVMenu,
    customRenameMenu,
    customNormalsMenu,
    customGenericMenu,

    # UV Ops classes
    activeUV,
    addUV,
    delUV,
    renameUV,

    # Rename Ops classes
    toCollection,
    toList,
    addSuffix,

    # Normals Ops classes
    clearCustomNormals,
    addCustomNormals
)

# register, unregister = bpy.utils.register_classes_factory(classes)

def register():
    for c in classes:
        bpy.utils.register_class(c)

    # handle the keymap
    wm = bpy.context.window_manager
    kc = wm.keyconfigs.addon

    if kc:
        km = kc.keymaps.new(name='3D View', space_type='VIEW_3D')
        kmi = km.keymap_items.new('wm.call_menu', type = 'T', value = 'PRESS', ctrl = True, shift = True, alt = True)
        kmi.properties.name = "MYMENU_MT_custom_genericMenu"

        addon_keymaps.append((km, kmi))

def unregister():
    for c in reversed(classes):
        bpy.utils.unregister(c)

    # handle the keymap
    for km, kmi in addon_keymaps:
        km.keymap_items.remove(kmi)

    addon_keymaps.clear()

# if __name__ == "__main__":
#     register()

bl_info = {
    "name" : "Batch Export",
    "author" : "Thanh Toan",
    "version": (1, 0),
    "blender": (2, 93, 1),
    "location": "Batch Export Panel",
    "description": "",
    "warning": "",
    "wiki_url": "",
    "category": "Import-Export"
}



import bpy

from bpy.props import *

from . BE_Panel import *
from . BE_Op import *

##
bpy.types.Scene.objWithUcx = {}

bpy.types.Scene.ucxObjects = []
##



bpy.types.Scene.export_folder = StringProperty  ( 
                                                name = "export folder",
                                                subtype = "DIR_PATH",
                                                description = "Directory to export FBX files into"
                                                )

## CUSTOM PROPERTIES ##

bpy.types.Scene.custom_prop = BoolProperty     (
                                                name = "custom properties",
                                                description = "Export Custom Properties",
                                                default = False
                                                )

## TRANSFORM ##

bpy.types.Scene.clear_transform = BoolProperty  (
                                                name = "clear transform",
                                                description = "Clear all Transformations",
                                                default = True
                                                )

bpy.types.Scene.forward_axis = EnumProperty     (
                                                name = "forward",
                                                description = "",
                                                items =   (
                                                            ('X', "X", "", 0),
                                                            ('Y', "Y", "", 1),
                                                            ('Z', "Z", "", 2),
                                                            ('-X', "-X", "", 3),
                                                            ('-Y', "-Y", "", 4),
                                                            ('-Z', "-Z", "", 5)
                                                        ),
                                                default = 'Y'
                                                )

bpy.types.Scene.up_axis = EnumProperty          (
                                                name = "up",
                                                description = "",
                                                items =   (
                                                            ('X', "X", "", 0),
                                                            ('Y', "Y", "", 1),
                                                            ('Z', "Z", "", 2),
                                                            ('-X', "-X", "", 3),
                                                            ('-Y', "-Y", "", 4),
                                                            ('-Z', "-Z", "", 5)
                                                        ),
                                                default = 'Z'
                                                )

bpy.types.Scene.use_space_transform = BoolProperty  (
                                                name = "use space transform",
                                                description = "More info in FBX Export Window",
                                                default = True
                                                    )

bpy.types.Scene.apply_transform = BoolProperty  (
                                                name = "apply transform",
                                                description = "More info in FBX Export Window",
                                                default = True
                                                )

## GEOMETRY ##

bpy.types.Scene.export_subdivision_surface = BoolProperty  (
                                                name = "export subdivision surface",
                                                description = "More info in FBX Export Window",
                                                default = False
                                                )

bpy.types.Scene.apply_modifiers = BoolProperty  (
                                                name = "apply modifiers",
                                                description = "Apply Modifiers.\nMore info in FBX Export Window",
                                                default = True
                                                )
        


## REGISTER ##

classes = (
    BATCH_EXPORT_PT_Panel,
    BATCH_EXPORT_OT_Operator
)

register, unregister = bpy.utils.register_classes_factory(classes)


# def register():
#     for c in classes:
#         bpy.utils.register_class(batchExportPanel_PT_Panel)


# def unregister():
#     for c in reversed(classes):
#         bpy.utils.unregister_class(batchExportPanel_PT_Panel)


if __name__ == "__main__":
    register()
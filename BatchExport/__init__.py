bl_info = {
    "name" : "Batch Export",
    "author" : "Thanh Toan",
    "version": (1, 0),
    "blender": (3, 2, 1),
    "location": "Function",
    "description": "",
    "warning": "",
    "wiki_url": "",
    "category": "Import-Export"
}



import bpy
from bpy.props import *



bpy.types.Scene.export_folder = StringProperty( 
                                                name="Export folder",
                                                subtype="DIR_PATH",
                                                description="Directory to export FBX files into"
                                              )



class exportPanel(bpy.types.Panel):
    bl_idname = "export.objects"
    bl_label =  "Batch Export Selected"
    bl_region_type = "UI"
    bl_space_type = "VIEW_3D"
    bl_category = "Batch Export"
    
    def draw(self, context):
        
        layout=self.layout
        scene=context.scene
        
        row=layout.row()
        col=layout.column()
        row.label(text="Export Folder:")
        
        col.prop(scene, "export_folder", text="")
        


# REGISTER #

classes = (
    exportPanel
)

def register():
#    for c in classes:
        bpy.utils.register_class(exportPanel)


def unregister():
#    for c in reversed(classes):
        bpy.utils.unregister_class(exportPanel)


if __name__ == "__main__":
    register()
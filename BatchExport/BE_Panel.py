import bpy
from bpy.types import Panel

class BATCH_EXPORT_PT_Panel(Panel):
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_label =  "Batch Export Selected"
    bl_category = "Batch Export"
    
    def draw(self, context):
        
        layout=self.layout
        scene=context.scene
        
        row=layout.row()
        row.label(text="Export Folder:")
        
        row=layout.row()
        row.prop(scene, "export_folder", text="")

        row=layout.row()
        row=layout.row()

        row=layout.row()
        row.label(text="Include:")

        row=layout.row()
        row.prop(scene, "custom_prop", text="Custom Properties")

        row=layout.row()
        row=layout.row()

        row=layout.row()
        row.label(text="Transform:")

        row=layout.row()
        row.prop(scene, "clear_transform", text="Clear Transformations")
        
        row=layout.row()
        row.prop(scene, "forward_axis", text="Forward")

        row=layout.row()
        row.prop(scene, "up_axis", text="Up")

        row=layout.row()
        row.prop(scene, "use_space_transform", text="Use Space Transform")

        row=layout.row()
        row.prop(scene, "apply_transform", text="Apply Transform")

        row=layout.row()
        row=layout.row()

        row=layout.row()
        row.label(text="Geometry:")

        row=layout.row()
        row.prop(scene, "export_subdivision_surface", text="Export Subdivision Surface")

        row=layout.row()
        row.prop(scene, "apply_modifiers", text="Apply Modifiers")

        row=layout.row()
        row.operator('object.be_ot_operator', text="Export")
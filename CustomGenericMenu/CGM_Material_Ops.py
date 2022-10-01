import bpy
from .CGM_Utils import *

# Merge Materials
class MergeMaterials(bpy.types.Operator):
    bl_label = "CGM Merge Materials"
    bl_idname = "merge.materials"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        all_materials = bpy.data.materials
        meshes = context.selected_objects
        
        bpy.ops.object.mode_set(mode='OBJECT') # Make sure in Object Mode before adjusting materials

        for current_mesh in meshes:

            for m in range(len(current_mesh.data.materials)) : # Check through all materials of current mesh
                if current_mesh.data.materials[m] != None :
                    current_mat_name = stripSuffix(current_mesh.data.materials[m])

                    for gm in all_materials : # Check through all materials in scene
                        if gm.name == current_mat_name :
                            current_mesh.data.materials[m] = gm
                        break

        
        return{'FINISHED'}
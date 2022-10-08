import bpy


# Clear Custom Normals #
class clearCustomNormals(bpy.types.Operator):
    bl_label = "CGM Clear Custom Normals"
    bl_idname = "clear.customnormals"
    bl_description = ""
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):

        objects = bpy.context.selected_objects

        for m in objects :
            bpy.context.view_layer.objects.active = m
            bpy.ops.mesh.customdata_custom_splitnormals_clear()
        return{"FINISHED"}


# Add Custom Normals #
class addCustomNormals(bpy.types.Operator):
    bl_label = "CGM Add Custom Normals"
    bl_idname = "add.customnormals"
    bl_description = ""
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):

        objects = bpy.context.selected_objects

        for m in objects :
            bpy.context.view_layer.objects.active = m
            bpy.ops.mesh.customdata_custom_splitnormals_add()
        return{"FINISHED"}
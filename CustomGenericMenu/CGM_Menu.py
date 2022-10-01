


# from tkinter import Menu
import bpy



class customUVMenu(bpy.types.Menu):
    bl_label = "UV Menu"
    bl_idname = "MYMENU_MT_custom_UVMenu"

    def draw(self, context):
        layout = self.layout

        layout.operator_context = 'INVOKE_DEFAULT'
        
        layout.operator("active.uv", text="Select UV Channel")
        
        layout.separator()
        
        layout.operator("add.uv", text="Add UV")
        layout.operator("del.uv", text="Delete UV")
        
        layout.separator()
        
        layout.operator("rename.uv", text="Rename UV")


class customRenameMenu(bpy.types.Menu):
    bl_label = "Rename Menu"
    bl_idname = "MYMENU_MT_custom_renameMenu"

    def draw(self, context):
        layout = self.layout

        layout.operator_context = 'INVOKE_DEFAULT'
        
        layout.operator("rename.to_collection", text="Rename to Collection")
        
        layout.operator("create.list", text="List Creation")
        
        layout.operator("add.suffix", text="Add Suffix")
        

class customNormalsMenu(bpy.types.Menu):
    bl_label = "Normals Menu"
    bl_idname = "MYMENU_MT_custom_normalsMenu"

    def draw(self, context):
        layout = self.layout
        
        layout.operator("add.customnormals", text="Add Custom Normals")
        layout.operator("clear.customnormals", text="Clear Custom Normals")


class CustomMaterialMenu(bpy.types.Menu):
    bl_label= "Material Menu"
    bl_idname = "MYMENU_MT_custom_materialMenu"

    def draw(self, context):
        layout = self.layout

        layout.operator("merge.materials", text="Merge Materials")


class customGenericMenu(bpy.types.Menu):
    bl_label = "Generic Menu"
    bl_idname = "MYMENU_MT_custom_genericMenu"
    
    def draw(self, context):
        layout = self.layout
        
        layout.menu("MYMENU_MT_custom_UVMenu", text="UV")
        layout.menu("MYMENU_MT_custom_renameMenu", text="Rename")
        layout.menu("MYMENU_MT_custom_normalsMenu", text="Normals")
        layout.menu("MYMENU_MT_custom_materialMenu", text="Material")
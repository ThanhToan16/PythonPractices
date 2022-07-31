bl_info = {
    "name" : "Custom Generic Menu",
    "author" : "Thanh Toan",
    "version": (1, 0),
    "blender": (2, 82, 7),
    "location": "Function",
    "description": "ctrl + alt + shift + T",
    "warning": "",
    "wiki_url": "",
    "category": "3D View"
}



import bpy



### Select UV ###
class activeUV(bpy.types.Operator):
    bl_label = "Select Index"
    bl_idname = "active.uv"
    bl_description = 'Select UV Channel by Index'
    bl_options = {'REGISTER', 'UNDO'}

    my_int : bpy.props.IntProperty(default=1, name="")


    def invoke(self, context, event):
        wm = context.window_manager
        return wm.invoke_props_dialog(self, width=150)


    def draw(self, context):
        row = self.layout
        row.prop(self, "my_int")


    def execute(self, context):
        meshes = [o.data for o in bpy.context.selected_objects]
        for m in meshes :
            if len(m.uv_layers) > self.my_int:
                m.uv_layers.active_index = self.my_int
        return{"FINISHED"}


### Add UV ###
class addUV(bpy.types.Operator):
    bl_label = "Name"
    bl_idname = "add.uv"
    bl_description = 'Add UV Channel with Name'
    bl_options = {'REGISTER', 'UNDO'}


    my_str : bpy.props.StringProperty(default="lightmap", name="")


    def invoke(self, context, event):
        wm = context.window_manager
        return wm.invoke_props_dialog(self, width=200)


    def draw(self, context):
        row = self.layout
        row.prop(self, "my_str")


    def execute(self, context):
        meshes = [o.data for o in bpy.context.selected_objects]
        for m in meshes :
            m.uv_layers.new(name = self.my_str)
        return{"FINISHED"}


### Delete UV ###
class delUV(bpy.types.Operator):
    bl_label = "Delete Index"
    bl_idname = "del.uv"
    bl_description = 'Delete UV Channel by Index'
    bl_options = {'REGISTER', 'UNDO'}


    my_int : bpy.props.IntProperty(default=1, name="")


    def invoke(self, context, event):
        wm = context.window_manager
        return wm.invoke_props_dialog(self, width=150)


    def draw(self, context):
        row = self.layout
        row.prop(self, "my_int")


    def execute(self, context):
        meshes = [o.data for o in bpy.context.selected_objects]
        for m in meshes :
            if len(m.uv_layers) > self.my_int:
                m.uv_layers.remove(m.uv_layers[self.my_int])
        return{"FINISHED"}


### Rename UV ###
class renameUV(bpy.types.Operator):
    bl_label = ""
    bl_idname = "rename.uv"
    bl_description = 'Rename UV Channel by Index'
    bl_options = {'REGISTER', 'UNDO'}


    my_int : bpy.props.IntProperty(default=0, name="Index")
    my_str : bpy.props.StringProperty(default="map1", name="New Name")


    def invoke(self, context, event):
        wm = context.window_manager
        return wm.invoke_props_dialog(self, width=300)


    def draw(self, context):
        row = self.layout
        row.prop(self, "my_int")
        row.prop(self, "my_str")


    def execute(self, context):
        meshes = [o.data for o in bpy.context.selected_objects]
        for m in meshes :
            if len(m.uv_layers) > self.my_int:
                m.uv_layers[self.my_int].name = self.my_str
        return{"FINISHED"}



# Rename to Collection #
class toCollection(bpy.types.Operator):
    bl_label = ""
    bl_idname = "rename.to_collection"
    bl_description = ""
    bl_options = {'REGISTER', 'UNDO'}


    def execute(self, context):

        meshes = bpy.context.selected_objects

        for m in meshes :
            n = m.users_collection[0].name
            m.name = n 
        return{"FINISHED"}


# List Definition #
class myList(bpy.types.PropertyGroup):
    my_list = []

# List Creation #
class toList(bpy.types.Operator):
    bl_label = "Create List"
    bl_idname = "create.list"
    bl_description = "Create a List for Renaming Order"
    bl_options = {'REGISTER', 'UNDO'}

    my_enum : bpy.props.EnumProperty(
        name = "Options",
        description = "Select Function",
        items= [('OP1', "Append", ""),
                ('OP2', "Remove", ""),
                ('OP3', "Clear", "")
        ]
    )

    def invoke(self, context, event):
        wm = context.window_manager
        return wm.invoke_props_dialog(self)

    def draw(self, context):
        layout = self.layout
        
        layout.prop(self, "my_enum", expand = True)

    def execute(self, context):
        
        enum = self.my_enum
        list = context.scene.my_tool.my_list
        object = bpy.context.active_object
        
        if enum == 'OP1':
            if object not in list:
                list.append(object)
            
        if enum == 'OP2':
            if object in list:
                list.remove(bpy.context.active_object)
            
        if enum == 'OP3':
            list.clear()
    
        print(list)
        
        return{"FINISHED"}



# Add suffix incremental number #
class addSuffix(bpy.types.Operator):
    bl_label = "Name"
    bl_idname = "add.suffix"
    bl_description = "Add suffix incremental number with a Name"
    bl_options = {'REGISTER', 'UNDO'}

    my_str : bpy.props.StringProperty(default="", name="")
    my_bool : bpy.props.BoolProperty(default=0, name=" With Inst")
    my_int : bpy.props.IntProperty(default=1, name="Start Number")
    
    def invoke(self, context, event):
        wm = context.window_manager
        return wm.invoke_props_dialog(self, width=300)

    def draw(self, context):
        row = self.layout
        row.prop(self, "my_str")
        row.separator()
        row.prop(self, "my_int")
        row.separator()
        row.prop(self, "my_bool")
    
    def execute(self, context):

        list = context.scene.my_tool.my_list
        meshes = bpy.context.selected_objects
        n = self.my_int
        
        if not list:
            
            if self.my_bool==1 :
                for m in meshes :
                    o = str(n)
                    n += 1
                    if n < 11 :
                        m.name = self.my_str + "_Inst0" + o
                    else :
                        m.name = self.my_str + "_Inst" + o
            else :
                for m in meshes :
                    o = str(n)
                    n += 1
                    if  n < 11 :
                        m.name = self.my_str + "_0" + o
                    else :
                        m.name = self.my_str + "_" + o
        else:
            
            if self.my_bool==1 :
                for m in list :
                    o = str(n)
                    n += 1
                    if n < 11 :
                        m.name = self.my_str + "_Inst0" + o
                    else :
                        m.name = self.my_str + "_Inst" + o
            else :
                for m in list :
                    o = str(n)
                    n += 1
                    if  n < 11 :
                        m.name = self.my_str + "_0" + o
                    else :
                        m.name = self.my_str + "_" + o
                        
            list.clear()
            print(list)
            
        return{"FINISHED"}



# Clear Custom Normals #
class clearCustomNormals(bpy.types.Operator):
    bl_label = ""
    bl_idname = "clear.customnormals"
    bl_description = ""
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):

        meshes = bpy.context.selected_objects

        for m in meshes :
            bpy.context.view_layer.objects.active = m
            bpy.ops.mesh.customdata_custom_splitnormals_clear()
        return{"FINISHED"}



# Add Custom Normals #
class addCustomNormals(bpy.types.Operator):
    bl_label = ""
    bl_idname = "add.customnormals"
    bl_description = ""
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):

        meshes = bpy.context.selected_objects

        for m in meshes :
            bpy.context.view_layer.objects.active = m
            bpy.ops.mesh.customdata_custom_splitnormals_add()
        return{"FINISHED"}



# CUSTOM MENU #


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


class customGenericMenu(bpy.types.Menu):
    bl_label = "Generic Menu"
    bl_idname = "MYMENU_MT_custom_genericMenu"
    
    def draw(self, context):
        layout = self.layout
        
        layout.menu("MYMENU_MT_custom_UVMenu", text="UV")
        layout.menu("MYMENU_MT_custom_renameMenu", text="Rename")
        layout.menu("MYMENU_MT_custom_normalsMenu", text="Normals")


# store keymaps here to access after registration
addon_keymaps = []


# REGISTER #

classes = (
    renameUV,
    delUV,
    addUV,
    activeUV,
    toCollection,
    myList,
    toList,
    addSuffix,
    addCustomNormals,
    clearCustomNormals,
    customUVMenu,
    customRenameMenu,
    customNormalsMenu,
    customGenericMenu,
)

def register():
    for c in classes:
        bpy.utils.register_class(c)

    # handle the keymap
    wm = bpy.context.window_manager
    kc = wm.keyconfigs.addon

    if kc:
        km = kc.keymaps.new(name='3D View', space_type='VIEW_3D')
        kmi = km.keymap_items.new("wm.call_menu", type = 'T', value = 'PRESS', ctrl = True, shift = True, alt=True)
        kmi.properties.name = "MYMENU_MT_custom_genericMenu"

        addon_keymaps.append((km, kmi))
        
    bpy.types.Scene.my_tool = bpy.props.PointerProperty(type= myList)


def unregister():
    for c in reversed(classes):
        bpy.utils.unregister_class(c)

    # handle the keymap
    for km, kmi in addon_keymaps:
        km.keymap_items.remove(kmi)

    addon_keymaps.clear()
    
    del bpy.types.Scene.my_tool


if __name__ == "__main__":
    register()
import bpy

### Select UV ###
class activeUV(bpy.types.Operator):
    bl_label = "CGM Select UV Channel by Index"
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
    bl_label = "CGM Add UV Channel with Name"
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
    bl_label = "CGM Delete UV Channel by Index"
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
    bl_label = "CGM Rename UV Channel by Index"
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
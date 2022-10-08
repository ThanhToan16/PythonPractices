from email.policy import default
from unicodedata import name
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
        objects = [o.data for o in bpy.context.selected_objects]
        for m in objects :
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
        objects = [o.data for o in bpy.context.selected_objects]
        for m in objects :
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
        objects = [o.data for o in bpy.context.selected_objects]
        for m in objects :
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
        layout = self.layout
        layout.prop(self, "my_int")
        layout.prop(self, "my_str")


    def execute(self, context):
        objects = [o.data for o in bpy.context.selected_objects]
        for m in objects :
            if len(m.uv_layers) > self.my_int:
                m.uv_layers[self.my_int].name = self.my_str
        return{"FINISHED"}


# Sequence Rename UV Channels
class PropertyCollection(bpy.types.PropertyGroup):
    name: bpy.props.StringProperty(name="", default="")
    index: bpy.props.IntProperty(name="", default=0)

class SequenceRename_UVChannels(bpy.types.Operator):
    bl_label = "CGM Sequence Rename UV Channels"
    bl_idname = "sequencerename.uvchannels"
    bl_options = {'REGISTER', 'UNDO'}

    prop_collection : bpy.props.CollectionProperty(type=PropertyCollection)# , override={'LIBRARY_OVERRIDABLE', 'USE_INSERTION'}


    def invoke(self, context, event):
        scene = context.scene
        wm = context.window_manager

        scene.uv_channel_amount = 6
        if len(self.prop_collection) != scene.uv_channel_amount :
            self.prop_collection.clear()

            for a in range(scene.uv_channel_amount):

                item = self.prop_collection.add()
                item.index = a

                if a == 0 :
                    item.name ="map1"
                elif a == 1 :
                    item.name ="lightmap"

        return wm.invoke_props_dialog(self, width = 300)


    def draw(self, context):
        layout = self.layout

        for prop in self.prop_collection:

            row = layout.row()
            column = row.column()

            row.prop(prop, "name", text=f'Index {prop.index}')



    def execute(self, context):
        objects = context.selected_objects

        for o in objects :
            for l in range(len(o.data.uv_layers)) :
                if self.prop_collection[l].name != "" :
                    o.data.uv_layers[l].name = self.prop_collection[l].name
            

        return {'FINISHED'}
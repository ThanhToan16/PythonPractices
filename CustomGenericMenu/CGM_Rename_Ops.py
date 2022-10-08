import bpy

# Rename to Collection #
class toCollection(bpy.types.Operator):
    bl_label = "CGM Rename To Collection"
    bl_idname = "rename.to_collection"
    bl_description = ""
    bl_options = {'REGISTER', 'UNDO'}


    def execute(self, context):

        objects = bpy.context.selected_objects

        for m in objects :
            n = m.users_collection[0].name
            m.name = n 
        return{"FINISHED"}


# List Creation #
class toList(bpy.types.Operator):
    bl_label = "CGM Create List"
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
        list = context.scene.my_list
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
    bl_label = "CGM Add Suffix"
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

        list = context.scene.my_list
        objects = bpy.context.selected_objects
        n = self.my_int
        
        if not list:
            
            if self.my_bool==1 :
                for m in objects :
                    o = str(n)
                    n += 1
                    if n < 11 :
                        m.name = self.my_str + "_Inst0" + o
                    else :
                        m.name = self.my_str + "_Inst" + o
            else :
                for m in objects :
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
from database import db


class Printer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), unique=True)
    val_print_x = db.Column(db.Float, unique=True)
    val_print_y = db.Column(db.Float, unique=True)
    val_print_z = db.Column(db.Float, unique=True)
    view_table = db.Column(db.String(127), unique=True)
    center_origin = db.Column(db.Boolean, unique=True)
    table_heating = db.Column(db.Boolean, unique=True)
    print_volume_heating = db.Column(db.Boolean, unique=True)
    type_g_code = db.Column(db.String(63), unique=True)
    min_x_head = db.Column(db.Float, unique=True)
    min_y_head = db.Column(db.Float, unique=True)
    max_x_head = db.Column(db.Float, unique=True)
    max_y_head = db.Column(db.Float, unique=True)
    height_portal = db.Column(db.Float, unique=True)
    displace_extruder = db.Column(db.Boolean, unique=True)
    count_extruder = db.Column(db.Integer, unique=True)
    start_g_code = db.Column(db.String(63), unique=True)
    end_g_code = db.Column(db.String(63), unique=True)
    extr_1_nozzle_diameter = db.Column(db.Float, unique=True)
    extr_1_filament_diameter = db.Column(db.Float, unique=True)
    extr_1_nozzle_displacement_x = db.Column(db.Float, unique=True)
    extr_1_nozzle_displacement_y = db.Column(db.Float, unique=True)
    extr_1_fan_number = db.Column(db.Integer, unique=True)
    extr_1_start_g_code = db.Column(db.String(63), unique=True)
    extr_1_end_g_code = db.Column(db.String(63), unique=True)
    extr_2_nozzle_diameter = db.Column(db.Float, unique=True)
    extr_2_filament_diameter = db.Column(db.Float, unique=True)
    extr_2_nozzle_displacement_x = db.Column(db.Float, unique=True)
    extr_2_nozzle_displacement_y = db.Column(db.Float, unique=True)
    extr_2_fan_number = db.Column(db.Integer, unique=True)
    extr_2_start_g_code = db.Column(db.String(63), unique=True)
    extr_2_end_g_code = db.Column(db.String(63), unique=True)

    def __init__(self, name, val_print_x, val_print_y, val_print_z, view_table, center_origin, table_heating,
                 print_volume_heating, type_g_code, min_x_head, min_y_head, max_x_head, max_y_head, height_portal,
                 displace_extruder, count_extruder, start_g_code, end_g_code, extr_1_nozzle_diameter,
                 extr_1_filament_diameter, extr_1_nozzle_displacement_x, extr_1_nozzle_displacement_y,
                 extr_1_fan_number, extr_1_start_g_code, extr_1_end_g_code, extr_2_nozzle_diameter,
                 extr_2_filament_diameter, extr_2_nozzle_displacement_x, extr_2_nozzle_displacement_y,
                 extr_2_fan_number, extr_2_start_g_code, extr_2_end_g_code, ):
        self.name = name
        self.val_print_x = val_print_x
        self.val_print_y = val_print_y
        self.val_print_z = val_print_z
        self.view_table = view_table
        self.center_origin = center_origin
        self.table_heating = table_heating
        self.print_volume_heating = print_volume_heating
        self.type_g_code = type_g_code
        self.min_x_head = min_x_head
        self.min_y_head = min_y_head
        self.max_x_head = max_x_head
        self.max_y_head = max_y_head
        self.height_portal = height_portal
        self.displace_extruder = displace_extruder
        self.count_extruder = count_extruder
        self.start_g_code = start_g_code
        self.end_g_code = end_g_code
        self.extr_1_nozzle_diameter = extr_1_nozzle_diameter
        self.extr_1_filament_diameter = extr_1_filament_diameter
        self.extr_1_nozzle_displacement_x = extr_1_nozzle_displacement_x
        self.extr_1_nozzle_displacement_y = extr_1_nozzle_displacement_y
        self.extr_1_fan_number = extr_1_fan_number
        self.extr_1_start_g_code = extr_1_start_g_code
        self.extr_1_end_g_code = extr_1_end_g_code
        self.extr_2_nozzle_diameter = extr_2_nozzle_diameter
        self.extr_2_filament_diameter = extr_2_filament_diameter
        self.extr_2_nozzle_displacement_x = extr_2_nozzle_displacement_x
        self.extr_2_nozzle_displacement_y = extr_2_nozzle_displacement_y
        self.extr_2_fan_number = extr_2_fan_number
        self.extr_2_start_g_code = extr_2_start_g_code
        self.extr_2_end_g_code = extr_2_end_g_code

    def __repr__(self):
        return '<Printer %r>' % self.name

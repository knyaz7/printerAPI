from flask import jsonify, request
from Models.Printer import Printer, db

def get_users():
    printers = Printer.query.all()
    output = {
        'message': "OK" if len(printers) > 0 else "Empty table",
        'data': []
    }
    for printer in printers:
        user_data = {'name': printer.name,
                     'login': printer.val_print_x,
                     'first_name': printer.val_print_y,
                     'val_print_z': printer.val_print_z,
                     'view_table': printer.view_table,
                     'center_origin': printer.center_origin,
                     'table_heating': printer.table_heating,
                     'print_volume_heating': printer.print_volume_heating,
                     'type_g_code': printer.type_g_code,
                     'min_x_head': printer.min_x_head,
                     'min_y_head': printer.min_y_head,
                     'max_x_head': printer.max_x_head,
                     'max_y_head': printer.max_y_head,
                     'height_portal': printer.height_portal,
                     'displace_extruder': printer.displace_extruder,
                     'count_extruder': printer.count_extruder,
                     'start_g_code': printer.start_g_code,
                     'end_g_code': printer.end_g_code,
                     'extr_1_nozzle_diameter': printer.extr_1_nozzle_diameter,
                     'extr_1_filament_diameter': printer.extr_1_filament_diameter,
                     'extr_1_nozzle_displacement_x': printer.extr_1_nozzle_displacement_x,
                     'extr_1_nozzle_displacement_y': printer.extr_1_nozzle_displacement_y,
                     'extr_1_fan_number': printer.extr_1_fan_number,
                     'extr_1_start_g_code': printer.extr_1_start_g_code,
                     'extr_1_end_g_code': printer.extr_1_end_g_code,
                     'extr_2_nozzle_diameter': printer.extr_2_nozzle_diameter,
                     'extr_2_filament_diameter': printer.extr_2_filament_diameter,
                     'extr_2_nozzle_displacement_x': printer.extr_2_nozzle_displacement_x,
                     'extr_2_nozzle_displacement_y': printer.extr_2_nozzle_displacement_y,
                     'extr_2_fan_number': printer.extr_2_fan_number,
                     'extr_2_start_g_code': printer.extr_2_start_g_code,
                     'extr_2_end_g_code': printer.extr_2_end_g_code
        }
        output['data'].append(user_data)
    return jsonify(output)


def get_user(item_id):
    printer = Printer.query.get(item_id)
    if printer:
        user_data = {'name': printer.name,
                     'login': printer.val_print_x,
                     'first_name': printer.val_print_y,
                     'val_print_z': printer.val_print_z,
                     'view_table': printer.view_table,
                     'center_origin': printer.center_origin,
                     'table_heating': printer.table_heating,
                     'print_volume_heating': printer.print_volume_heating,
                     'type_g_code': printer.type_g_code,
                     'min_x_head': printer.min_x_head,
                     'min_y_head': printer.min_y_head,
                     'max_x_head': printer.max_x_head,
                     'max_y_head': printer.max_y_head,
                     'height_portal': printer.height_portal,
                     'displace_extruder': printer.displace_extruder,
                     'count_extruder': printer.count_extruder,
                     'start_g_code': printer.start_g_code,
                     'end_g_code': printer.end_g_code,
                     'extr_1_nozzle_diameter': printer.extr_1_nozzle_diameter,
                     'extr_1_filament_diameter': printer.extr_1_filament_diameter,
                     'extr_1_nozzle_displacement_x': printer.extr_1_nozzle_displacement_x,
                     'extr_1_nozzle_displacement_y': printer.extr_1_nozzle_displacement_y,
                     'extr_1_fan_number': printer.extr_1_fan_number,
                     'extr_1_start_g_code': printer.extr_1_start_g_code,
                     'extr_1_end_g_code': printer.extr_1_end_g_code,
                     'extr_2_nozzle_diameter': printer.extr_2_nozzle_diameter,
                     'extr_2_filament_diameter': printer.extr_2_filament_diameter,
                     'extr_2_nozzle_displacement_x': printer.extr_2_nozzle_displacement_x,
                     'extr_2_nozzle_displacement_y': printer.extr_2_nozzle_displacement_y,
                     'extr_2_fan_number': printer.extr_2_fan_number,
                     'extr_2_start_g_code': printer.extr_2_start_g_code,
                     'extr_2_end_g_code': printer.extr_2_end_g_code
                     }
        return jsonify({'message': 'OK', 'data': user_data})
    else:
        return jsonify({'message': 'User not found'}), 404

"""
method=POST
POST body: login (unique), first_name, last_name, password

returns {
    status: true/false,
    message: OK / Error
    data = inserted user id if success
}
"""
def add_user():
    name = request.form.get('name')
    val_print_x = request.form.get('val_print_x')
    val_print_y = request.form.get('val_print_y')
    val_print_z = request.form.get('val_print_z')
    view_table = request.form.get('view_table')
    center_origin = request.form.get('center_origin')
    table_heating = request.form.get('table_heating')
    print_volume_heating = request.form.get('print_volume_heating')
    type_g_code = request.form.get('type_g_code')
    min_x_head = request.form.get('min_x_head')
    min_y_head = request.form.get('min_y_head')
    max_x_head = request.form.get('max_x_head')
    max_y_head = request.form.get('max_y_head')
    height_portal = request.form.get('height_portal')
    displace_extruder = request.form.get('displace_extruder')
    count_extruder = request.form.get('count_extruder')
    start_g_code = request.form.get('start_g_code')
    end_g_code = request.form.get('end_g_code')
    extr_1_nozzle_diameter = request.form.get('extr_1_nozzle_diameter')
    extr_1_filament_diameter = request.form.get('extr_1_filament_diameter')
    extr_1_nozzle_displacement_x = request.form.get('extr_1_nozzle_displacement_x')
    extr_1_nozzle_displacement_y = request.form.get('extr_1_nozzle_displacement_y')
    extr_1_fan_number = request.form.get('extr_1_fan_number')
    extr_1_start_g_code = request.form.get('extr_1_start_g_code')
    extr_1_end_g_code = request.form.get('extr_1_end_g_code')
    extr_2_nozzle_diameter = request.form.get('extr_2_nozzle_diameter')
    extr_2_filament_diameter = request.form.get('extr_2_filament_diameter')
    extr_2_nozzle_displacement_x = request.form.get('extr_2_nozzle_displacement_x')
    extr_2_nozzle_displacement_y = request.form.get('extr_2_nozzle_displacement_y')
    extr_2_fan_number = request.form.get('extr_2_fan_number')
    extr_2_start_g_code = request.form.get('extr_2_start_g_code')
    extr_2_end_g_code = request.form.get('extr_2_end_g_code')

    if not name:
        return jsonify({'message': 'Missing required fields'}), 400

    existing_printer = Printer.query.filter_by(name=name).first()
    if existing_printer:
        return jsonify({'message': 'Printer with this name already exists'}), 409

    new_printer = Printer(
        name=name,
        val_print_x=val_print_x,
        val_print_y=val_print_y,
        val_print_z=val_print_z,
        view_table=view_table,
        center_origin=center_origin,
        table_heating=table_heating,
        print_volume_heating=print_volume_heating,
        type_g_code=type_g_code,
        min_x_head=min_x_head,
        min_y_head=min_y_head,
        max_x_head=max_x_head,
        max_y_head=max_y_head,
        height_portal=height_portal,
        displace_extruder=displace_extruder,
        count_extruder=count_extruder,
        start_g_code=start_g_code,
        end_g_code=end_g_code,
        extr_1_nozzle_diameter=extr_1_nozzle_diameter,
        extr_1_filament_diameter=extr_1_filament_diameter,
        extr_1_nozzle_displacement_x=extr_1_nozzle_displacement_x,
        extr_1_nozzle_displacement_y=extr_1_nozzle_displacement_y,
        extr_1_fan_number=extr_1_fan_number,
        extr_1_start_g_code=extr_1_start_g_code,
        extr_1_end_g_code=extr_1_end_g_code,
        extr_2_nozzle_diameter=extr_2_nozzle_diameter,
        extr_2_filament_diameter=extr_2_filament_diameter,
        extr_2_nozzle_displacement_x=extr_2_nozzle_displacement_x,
        extr_2_nozzle_displacement_y=extr_2_nozzle_displacement_y,
        extr_2_fan_number=extr_2_fan_number,
        extr_2_start_g_code=extr_2_start_g_code,
        extr_2_end_g_code=extr_2_end_g_code
    )
    db.session.add(new_printer)
    db.session.commit()

    # Получаем ID вставленной записи
    inserted_printer_id = new_printer.id

    return jsonify({'message': 'Printer added successfully', 'printer_id': inserted_printer_id}), 201




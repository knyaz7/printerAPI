from flask import jsonify, request
from Models.Printer import Printer, PrinterSchema, db


class PrinterController:
    @staticmethod
    def get_printers():
        printers = Printer.query.all()
        printer_schema = PrinterSchema(many=True)
        return jsonify({'message': 'OK', 'data': printer_schema.dump(printers)})

    @staticmethod
    def get_printer(item_id):
        printer = Printer.query.get(item_id)
        if printer:
            printer_schema = PrinterSchema()
            return jsonify({'message': 'OK', 'data': printer_schema.dump(printer)})
        else:
            return jsonify({'message': 'Printer not found'}), 404

    @staticmethod
    def add_printer():
        printer_schema = PrinterSchema()
        new_printer_data = printer_schema.load(request.json)

        if isinstance(new_printer_data, dict):  # Проверяем, является ли new_printer_data словарем (десериализованные данные без ошибок валидации)
            # Создаем новый объект Printer, используя переданные данные и значения по умолчанию
            new_printer = Printer(
                name=new_printer_data['name'],
                val_print_x=new_printer_data.get('val_print_x'),
                val_print_y=new_printer_data.get('val_print_y'),
                val_print_z=new_printer_data.get('val_print_z'),
                view_table=new_printer_data.get('view_table'),
                center_origin=new_printer_data.get('center_origin'),
                table_heating=new_printer_data.get('table_heating'),
                print_volume_heating=new_printer_data.get('print_volume_heating'),
                type_g_code=new_printer_data.get('type_g_code'),
                min_x_head=new_printer_data.get('min_x_head'),
                min_y_head=new_printer_data.get('min_y_head'),
                max_x_head=new_printer_data.get('max_x_head'),
                max_y_head=new_printer_data.get('max_y_head'),
                height_portal=new_printer_data.get('height_portal'),
                displace_extruder=new_printer_data.get('displace_extruder'),
                count_extruder=new_printer_data.get('count_extruder'),
                start_g_code=new_printer_data.get('start_g_code'),
                end_g_code=new_printer_data.get('end_g_code'),
                extr_1_nozzle_diameter=new_printer_data.get('extr_1_nozzle_diameter'),
                extr_1_filament_diameter=new_printer_data.get('extr_1_filament_diameter'),
                extr_1_nozzle_displacement_x=new_printer_data.get('extr_1_nozzle_displacement_x'),
                extr_1_nozzle_displacement_y=new_printer_data.get('extr_1_nozzle_displacement_y'),
                extr_1_fan_number=new_printer_data.get('extr_1_fan_number'),
                extr_1_start_g_code=new_printer_data.get('extr_1_start_g_code'),
                extr_1_end_g_code=new_printer_data.get('extr_1_end_g_code'),
                extr_2_nozzle_diameter=new_printer_data.get('extr_2_nozzle_diameter'),
                extr_2_filament_diameter=new_printer_data.get('extr_2_filament_diameter'),
                extr_2_nozzle_displacement_x=new_printer_data.get('extr_2_nozzle_displacement_x'),
                extr_2_nozzle_displacement_y=new_printer_data.get('extr_2_nozzle_displacement_y'),
                extr_2_fan_number=new_printer_data.get('extr_2_fan_number'),
                extr_2_start_g_code=new_printer_data.get('extr_2_start_g_code'),
                extr_2_end_g_code=new_printer_data.get('extr_2_end_g_code')
            )
            db.session.add(new_printer)
            db.session.commit()
            return jsonify({'message': 'Printer added successfully', 'printer_id': new_printer.id}), 201
        else:
            # Если в new_printer_data есть ошибки валидации, возвращаем их
            return jsonify({'message': 'Validation error', 'errors': new_printer_data}), 400


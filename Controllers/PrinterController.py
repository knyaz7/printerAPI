from flask import jsonify, request
from Models.Printer import Printer, PrinterSchema, db
import requests


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

    @staticmethod
    def create_default_printers():
        # Принтеры по умолчанию
        default_printers = [
            {
                "name": "Default Printer 1",
                "val_print_x": 200.0,
                "val_print_y": 200.0,
                "val_print_z": 200.0,
                "view_table": "Glass",
                "center_origin": True,
                "table_heating": False,
                "print_volume_heating": False,
                "type_g_code": "G-code",
                "min_x_head": 0.0,
                "min_y_head": 0.0,
                "max_x_head": 200.0,
                "max_y_head": 200.0,
                "height_portal": 100.0,
                "displace_extruder": False,
                "count_extruder": 1,
                "start_g_code": "Start G-code",
                "end_g_code": "End G-code",
                "extr_1_nozzle_diameter": 0.4,
                "extr_1_filament_diameter": 1.75,
                "extr_1_nozzle_displacement_x": 0.0,
                "extr_1_nozzle_displacement_y": 0.0,
                "extr_1_fan_number": 1,
                "extr_1_start_g_code": "Extruder 1 Start G-code",
                "extr_1_end_g_code": "Extruder 1 End G-code",
                "extr_2_nozzle_diameter": None,  # Параметры для второго экструдера
                "extr_2_filament_diameter": None,
                "extr_2_nozzle_displacement_x": None,
                "extr_2_nozzle_displacement_y": None,
                "extr_2_fan_number": None,
                "extr_2_start_g_code": None,
                "extr_2_end_g_code": None
            },
            {
                "name": "Default Printer 2",
                "val_print_x": 250.0,
                "val_print_y": 250.0,
                "val_print_z": 250.0,
                "view_table": "Aluminum",
                "center_origin": False,
                "table_heating": True,
                "print_volume_heating": True,
                "type_g_code": "Custom G-code",
                "min_x_head": 10.0,
                "min_y_head": 10.0,
                "max_x_head": 240.0,
                "max_y_head": 240.0,
                "height_portal": 120.0,
                "displace_extruder": True,
                "count_extruder": 2,
                "start_g_code": "Custom Start G-code",
                "end_g_code": "Custom End G-code",
                "extr_1_nozzle_diameter": 0.4,
                "extr_1_filament_diameter": 1.75,
                "extr_1_nozzle_displacement_x": 10.0,
                "extr_1_nozzle_displacement_y": 5.0,
                "extr_1_fan_number": 1,
                "extr_1_start_g_code": "Extruder 1 Custom Start G-code",
                "extr_1_end_g_code": "Extruder 1 Custom End G-code",
                "extr_2_nozzle_diameter": 0.4,
                "extr_2_filament_diameter": 1.75,
                "extr_2_nozzle_displacement_x": -10.0,
                "extr_2_nozzle_displacement_y": -5.0,
                "extr_2_fan_number": 2,
                "extr_2_start_g_code": "Extruder 2 Custom Start G-code",
                "extr_2_end_g_code": "Extruder 2 Custom End G-code"
            }
            # Добавьте сколько угодно принтеров по умолчанию
        ]
        # Добавление принтеров по умолчанию в базу данных
        for printer_data in default_printers:
            new_printer = Printer(**printer_data)
            db.session.add(new_printer)
        db.session.commit()



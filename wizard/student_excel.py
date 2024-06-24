from odoo import models, fields
from odoo.exceptions import ValidationError
import io
from io import StringIO
import xlsxwriter
import xlwt
import base64
from xlsxwriter.utility import xl_rowcol_to_cell as to_cell
from odoo.http import request



class wizard(models.TransientModel):
    _name = "student.excel"
    _description = "This is a student fees wizard"
     
    standard_id=fields.Many2one("standard.detail", string="Standard")
    
    
    def action_download_excel(self):
        
        # active_ids = self._context.get("active_ids")
        # print("==========================================",active_ids)
        
        # record_ids = self.env['standard.detail'].
        # print("-------------------------------------",record_ids.id)
        
        attach_obj=self.env["ir.attachment"]
        fp=io.BytesIO()
        workbook = xlsxwriter.Workbook(fp)
        worksheet = workbook.add_worksheet('Student Excel')
        
        tbl_head_fmt = workbook.add_format({
                    'border': 1,
                    'font_name': 'Calibri',
                    'align': 'center',
                    'font_size': 10,
                    'bold': True,
                })
        table_row_fmt = workbook.add_format({
                    'border': 1,
                    'font_name': 'Calibri',
                    'align': 'center',
                    'font_size': 10,
                    'num_format':'dd-mm-yyyy'
                })
        table_row_fmt2 = workbook.add_format({
                    'border': 1,
                    'font_name': 'Calibri',
                    'align': 'center',
                    'font_size': 10,
                })
        main_head_fmt = workbook.add_format({
                    'bg_color': 'red', 'align': 'center', 'font_size': 20,
                    'font_color': 'white'})
        worksheet.merge_range(
            "A1:H2",
            "All Student Report",
            main_head_fmt        
        )
        
        worksheet.merge_range(
            "A3:G3",""
        )
        worksheet.set_column('A:A', 10)
        worksheet.set_column('B:B', 20)
        worksheet.set_column('C:C', 15)
        worksheet.set_column('D:D', 20)
        worksheet.set_column('E:E', 15)
        worksheet.set_column('F:F', 15)
        worksheet.set_column('G:G', 20)
        worksheet.set_column('H:H', 20)
        

        
        # worksheet.write('A4', '', tbl_head_fmt)
        worksheet.write('A4', 'Name', tbl_head_fmt)
        worksheet.write('B4', 'Roll No.', tbl_head_fmt)
        worksheet.write('C4', 'Standard', tbl_head_fmt)
        worksheet.write('D4', 'Medium', tbl_head_fmt)
        worksheet.write('E4', 'Gender', tbl_head_fmt)
        worksheet.write('F4', 'Birth-Date', tbl_head_fmt)
        worksheet.write('G4', 'Admission Date', tbl_head_fmt)
        worksheet.write('H4', 'Class Teacher', tbl_head_fmt)

        
        row = 5
        for record in self.standard_id:
            for student in record.student_ids:
                worksheet.write(row, 0, student.name, table_row_fmt)
                print ("\n student.roll ::::::::::::::;", student.roll)
                worksheet.write(row, 1, student.roll, table_row_fmt2)
                worksheet.write(row, 2, student.standard_id.std,table_row_fmt2)  # Accessing standard name from parent record
                worksheet.write(row, 3, student.medium_id, table_row_fmt)  # Accessing medium name from related record
                worksheet.write(row, 4, student.gender, table_row_fmt)  
                worksheet.write(row, 5, student.dob.strftime('%d-%m-%Y'), table_row_fmt)  # Formatting date
                worksheet.write(row, 6, student.admission, table_row_fmt)
                worksheet.write(row, 7, student.teacher, table_row_fmt)
                row += 1

    

        workbook.close()
        data=base64.b64encode(fp.getvalue())
        fp.close()
            
        report_name="Student Excel_%s.xlsx" %(
            self.standard_id
        )
        doc_id=attach_obj.create(
            {
                'name':"student_excel_test.xlsx",
                'datas':data,
                'res_model':"standard.detail",
                # 'datas_fname':report_name
            }
        )
        
        return {
                'type': 'ir.actions.act_url',
                'url': 'web/content/%s?download=true' % (doc_id.id),
                'target': 'new',
                }
    

from odoo import models, fields, api

class book(models.Model):
    _name = "book.detail"
    _description = "Book Detail"
    
    name = fields.Char(string = "Book Name",)
    author = fields.Char(string= "Author Name")
    public = fields.Date(string = "Publish Date")
    price = fields.Float(string= "Price")
    available= fields.Boolean(string="Is Available", required = True)
    image = fields.Binary(string = "image")
    

# ----------------------------------------------------------------------------------------------------------   
               
    # THIS IS A NAME SEARCH METHOD
    @api.model
    def _name_search(self, name, args=None, operator='ilike', limit=100):
        if name:
            args=['|',('name', operator, name)]
            print("'''''''''''''''''''''''''''''''''''''''''''''''''''''", args)
        return super()._name_search(name, args, operator, limit)
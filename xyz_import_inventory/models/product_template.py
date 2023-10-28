""" Import modules Product Template """
from odoo import _,api,models
from odoo.exceptions import UserError

class ProductTemplate(models.Model):
    """ Inherit Product Template Class """
    _inherit = 'product.template'

    @api.model
    def load(self, fields, data):
        """ 
        Override check default_code, if exists updated the values else insert the values.
        """
        if "import_file" in self.env.context:
            if 'default_code' not in fields:
                raise UserError(_("The import file must contain the 'default_code' column"))
            product_codes_ids = {}
            fields.append(".id")
            default_code_index = fields.index("default_code")
            product_default_codes = self.search_read(fields=["default_code"])
            for product in product_default_codes:
                product_codes_ids[product["default_code"]] = product["id"]
            for row in data:
                default_code = row[default_code_index]
                product_id = product_codes_ids.get(default_code)
                if product_id:
                    row.append(product_id)
        return super().load(fields, data)

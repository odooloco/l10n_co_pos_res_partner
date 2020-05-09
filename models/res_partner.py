# -*- coding: utf-8 -*-
###############################################################################
#                                                                             #
#                                                                             #
# Part of Odoo. See LICENSE file for full copyright and licensing details.    #
#                                                                             #
#                                                                             #
#                                                                             #
# Co-Authors    Odoo LoCo                                                     #
#               Localización funcional de Odoo para Colombia                  #
#                                                                             #
#                                                                             #
# This program is free software: you can redistribute it and/or modify        #
# it under the terms of the GNU Affero General Public License as published by #
# the Free Software Foundation, either version 3 of the License, or           #
# (at your option) any later version.                                         #
#                                                                             #
# This program is distributed in the hope that it will be useful,             #
# but WITHOUT ANY WARRANTY; without even the implied warranty of              #
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the               #
# GNU Affero General Public License for more details.                         #
#                                                                             #
# You should have received a copy of the GNU Affero General Public License    #
# along with this program.  If not, see <http://www.gnu.org/licenses/>.       #
###############################################################################


from odoo import models, fields, api, osv, _
from odoo import http
from odoo.http import request
import logging
_logger = logging.getLogger(__name__)
logger = logging.getLogger(__name__)
import json, sys



class res_partner(models.Model):
    _inherit = 'res.partner'

    @api.model
    def create_from_ui(self, partner):

        if('doctype' in partner):
            doctype = int(partner['doctype'])
            del partner['doctype']
            partner['doctype'] = doctype

        if('personType' in partner):
            personType = int(partner['personType'])
            del partner['personType']
            partner['personType'] = personType

        partner_id = partner.pop('id', False)
        if partner_id:  # Modifying existing partner
            self.browse(partner_id).write(partner)
        else:
            partner['lang'] = self.env.user.lang
            partner_id = self.create(partner).id

        return partner_id
    
    def pos_get_doctype(self,  context={'lang': 'es_CO'}):
        result = []
        try:            
            for item in self.env['res.partner'].with_context(context)._fields['doctype'].selection:
                result.append({'id': item[0], 'name': item[1]})
        except Exception as e:
            raise Warning(getattr(e, 'message', repr(e))+" ON LINE "+format(sys.exc_info()[-1].tb_lineno))
            pass
        return result

    def pos_get_persontype(self, context={'lang': 'es_CO'}):
        result = []
        try:
            for item in self.env['res.partner'].with_context(context)._fields['personType'].selection:
                result.append({'id': item[0], 'name': item[1]})
        except Exception as e:
            raise Warning(getattr(e, 'message', repr(e))+" ON LINE "+format(sys.exc_info()[-1].tb_lineno))
            pass
        return result
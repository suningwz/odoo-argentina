#############################################################
# THIS IS A PRODUCT OF A COOPERATION AGREEMENT BETWEEN
# AITIC S.A.S. AND MASTERCORE S.A.S.
#
# Maintainers: odoo-dev@mastercore.net
#############################################################
{
    'name': 'Argentinian Stock Voucher Report ALDYL',
    'version': '13.0.0.1',
    'description': """

    **Escríbenos** a info@mastercore.net
    """,
    'author': "MASTERCORE S.A.S., AITIC S.A.S.",
    'website': "https://mastercore.net",
    'license': 'Other OSI approved licence',
    'category': 'Localization / Argentina',
    'depends': [
        'stock_voucher',
    ],
    'data': [
        'report/paperformat.xml',
        'report/stock_picking_remittance.xml',
        'views/stock_book_views.xml',
    ],
    'auto_install': False,
    'application': False,
    'installable': True,
}

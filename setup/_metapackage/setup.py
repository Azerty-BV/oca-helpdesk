import setuptools

with open('VERSION.txt', 'r') as f:
    version = f.read().strip()

setuptools.setup(
    name="odoo11-addons-oca-helpdesk",
    description="Meta package for oca-helpdesk Odoo addons",
    version=version,
    install_requires=[
        'odoo11-addon-helpdesk_mgmt',
        'odoo11-addon-helpdesk_mgmt_rating',
        'odoo11-addon-helpdesk_mgmt_solution',
        'odoo11-addon-helpdesk_type',
    ],
    classifiers=[
        'Programming Language :: Python',
        'Framework :: Odoo',
        'Framework :: Odoo :: 11.0',
    ]
)

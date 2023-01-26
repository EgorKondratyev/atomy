from handlers.start_command import register_start_command_handlers
from handlers.client.slogan import register_slogan_handlers
from handlers.client.what_pay import register_what_pay_handlers
from handlers.client.about_company_product import register_about_company_product_handlers

register_start_command_handlers()
register_slogan_handlers()
register_what_pay_handlers()
register_about_company_product_handlers()

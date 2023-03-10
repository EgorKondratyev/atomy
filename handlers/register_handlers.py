from handlers.start_command import register_start_command_handlers
from handlers.client.slogan import register_slogan_handlers
from handlers.client.what_pay import register_what_pay_handlers
from handlers.client.about_company_product import register_about_company_product_handlers
from handlers.client.form import register_form_handlers
from handlers.stop_fsm import register_stop_fsm_handler

from handlers.admin.reload import register_change_admin_handlers
from handlers.admin.set_video_prezentation import register_set_video_handlers

register_start_command_handlers()
register_slogan_handlers()
register_what_pay_handlers()
register_about_company_product_handlers()
register_form_handlers()
register_stop_fsm_handler()

register_change_admin_handlers()
register_set_video_handlers()

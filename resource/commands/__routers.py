# здесь хранятся все роутеры
from .start import router as start_router
from .buyer_commands.buyer_start import router as buyer_start_router
from .admin_commands.user_management import router as user_management_router
from .admin_commands.plot_management import router as plot_management
from .admin_commands.changing_personal_data import router as changing_personal_data
from .admin_commands.first_name_changing import router as changing_first_name
from aiogram import Dispatcher

from loader import dp
from .owner_or_admin_filter import IsOwnerFilter, IsAdminFilter
from .member_can_restrict_filter import MemberCanRestrictFilter


if __name__ == "filters":
    # dp.filters_factory.bind(AdminFilter)
    pass

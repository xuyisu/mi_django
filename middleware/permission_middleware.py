from django.contrib.auth.mixins import PermissionRequiredMixin


from utils import result


class PermissionRequired(PermissionRequiredMixin):

    def has_permission(self):

        # 直接放行
        return True

    # 没有权限时候的报错回调
    def handle_no_permission(self):
        return R.failed("暂无操作权限")

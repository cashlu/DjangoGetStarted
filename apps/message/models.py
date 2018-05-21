from django.db import models


class UserMessage(models.Model):
    # primary_key字段必须有默认值
    object_id = models.CharField(primary_key=True, max_length=50,
                                 verbose_name='主键', default="")
    # verbose_name在后台显示字段名称时会用到
    name = models.CharField(max_length=20, null=True, blank=True,
                            verbose_name='用户名')
    email = models.EmailField(verbose_name='邮箱')
    address = models.CharField(max_length=100, verbose_name='联系地址')
    message = models.CharField(max_length=500, verbose_name='留言信息')

    # CharField必须指明默认最大长度。null = True, blank = True指明字段可以为空
    # defalut = " "指定默认值。

    class Meta:
        # verbose_name = '用户留言信息'
        verbose_name_plural = '用户留言信息'
        ordering = ('-object_id',)

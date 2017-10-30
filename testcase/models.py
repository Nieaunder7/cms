from django.db import models

# Create your models here.
class TestCaseList(models.Model):
    PASS_RESULT = 'PASS'
    FAIL_RESULT = 'FAIL'
    DEFAULT = 'NONE'

    RESULT_CHOICES=(
        (PASS_RESULT,'PASS'),
        (FAIL_RESULT,'FAIL'),
        (DEFAULT,'NONE'),
    )
    suite = models.CharField(verbose_name=u'대분류', max_length=50)
    case = models.CharField(verbose_name=u'중분류', max_length=50)
    task = models.CharField(verbose_name=u'소분류', max_length=100)
    priority = models.CharField(verbose_name=u'중요도', max_length=50)
    context = models.TextField(verbose_name=u'상세화면')
    result = models.CharField(verbose_name=u'측정결과', max_length=10, choices=RESULT_CHOICES, default=DEFAULT)

    def __str__(self):
        return self.suite + self.case + self.task
    
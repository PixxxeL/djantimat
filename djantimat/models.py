# -*- coding: utf-8 -*-

from django.db import models
import pymorphy2


class Slang(models.Model):

    morph = None

    word = models.CharField(
        verbose_name = u'Нормальная форма матерного слова',
        max_length = 64,
        unique = True,
        help_text = u'Можете вписать любое слово - оно будет нормализовано автоматически'
    )

    def __unicode__(self):
        return self.word

    def save(self, *args, **kwargs):
        if not Slang.morph:
            Slang.morph = pymorphy2.MorphAnalyzer()
        self.word = self.word.strip().lower()
        try:
            self.word = Slang.morph.parse(self.word)[0].normal_form
        except IndexError:
            pass
        super(Slang, self).save(*args, **kwargs)

    class Meta:
        verbose_name = u'Матерное слово'
        verbose_name_plural = u'Матерные слова'

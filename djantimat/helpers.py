# -*- coding: utf-8 -*-

import re

import pymorphy2

from .models import Slang


word_pattern = ur'[А-яA-z0-9\-]+'


class PymorphyProc(object):

    morph = pymorphy2.MorphAnalyzer()

    @staticmethod
    def test(text):
        return len([w for w in PymorphyProc._gen(text)])

    @staticmethod
    def replace(text, repl='[censored]'):
        words = {}
        for word in PymorphyProc._gen(text):
            text = text.replace(word, repl)
        return text

    @staticmethod
    def wrap(text, wrap=('<span style="color:red;">', '</span>',)):
        words = {}
        for word in PymorphyProc._gen(text):
            words[word] = u'%s%s%s' % (wrap[0], word, wrap[1],)
        for word, wrapped in words.items():
            text = text.replace(word, wrapped)
        return text

    @staticmethod
    def _gen(text):
        for word in re.findall(word_pattern, text):
            if len(word) < 3:
                continue
            normal_word = PymorphyProc.morph.parse(word.lower())[0].normal_form
            if normal_word in PymorphyProc.get_words():
                #print normal_word.encode('1251'), word.encode('1251')
                yield word

    @staticmethod
    def get_words():
        return Slang.objects.values_list('word', flat=True)


class RegexpProc(object):

    PATTERN_1 = ur''.join((
        ur'\w{0,5}[хx]([хx\s\!@#\$%\^&*+-\|\/]{0,6})',
        ur'[уy]([уy\s\!@#\$%\^&*+-\|\/]{0,6})[ёiлeеюийя]\w{0,7}|\w{0,6}[пp]',
        ur'([пp\s\!@#\$%\^&*+-\|\/]{0,6})[iие]([iие\s\!@#\$%\^&*+-\|\/]{0,6})',
        ur'[3зс]([3зс\s\!@#\$%\^&*+-\|\/]{0,6})[дd]\w{0,10}|[сcs][уy]',
        ur'([уy\!@#\$%\^&*+-\|\/]{0,6})[4чkк]\w{1,3}|\w{0,4}[bб]',
        ur'([bб\s\!@#\$%\^&*+-\|\/]{0,6})[lл]([lл\s\!@#\$%\^&*+-\|\/]{0,6})',
        ur'[yя]\w{0,10}|\w{0,8}[её][bб][лске@eыиаa][наи@йвл]\w{0,8}|\w{0,4}[еe]',
        ur'([еe\s\!@#\$%\^&*+-\|\/]{0,6})[бb]([бb\s\!@#\$%\^&*+-\|\/]{0,6})',
        ur'[uу]([uу\s\!@#\$%\^&*+-\|\/]{0,6})[н4ч]\w{0,4}|\w{0,4}[еeё]',
        ur'([еeё\s\!@#\$%\^&*+-\|\/]{0,6})[бb]([бb\s\!@#\$%\^&*+-\|\/]{0,6})',
        ur'[нn]([нn\s\!@#\$%\^&*+-\|\/]{0,6})[уy]\w{0,4}|\w{0,4}[еe]',
        ur'([еe\s\!@#\$%\^&*+-\|\/]{0,6})[бb]([бb\s\!@#\$%\^&*+-\|\/]{0,6})',
        ur'[оoаa@]([оoаa@\s\!@#\$%\^&*+-\|\/]{0,6})[тnнt]\w{0,4}|\w{0,10}[ё]',
        ur'([ё\!@#\$%\^&*+-\|\/]{0,6})[б]\w{0,6}|\w{0,4}[pп]',
        ur'([pп\s\!@#\$%\^&*+-\|\/]{0,6})[иeеi]([иeеi\s\!@#\$%\^&*+-\|\/]{0,6})',
        ur'[дd]([дd\s\!@#\$%\^&*+-\|\/]{0,6})[oоаa@еeиi]',
        ur'([oоаa@еeиi\s\!@#\$%\^&*+-\|\/]{0,6})[рr]\w{0,12}',
    ))

    PATTERN_2 = ur'|'.join((
        ur"(\b[сs]{1}[сsц]{0,1}[uуy](?:[ч4]{0,1}[иаakк][^ц])\w*\b)",
        ur"(\b(?!пло|стра|[тл]и)(\w(?!(у|пло)))*[хx][уy](й|йа|[еeё]|и|я|ли|ю)(?!га)\w*\b)",
        ur"(\b(п[oо]|[нз][аa])*[хx][eе][рp]\w*\b)",
        ur"(\b[мm][уy][дd]([аa][кk]|[oо]|и)\w*\b)",
        ur"(\b\w*д[рp](?:[oо][ч4]|[аa][ч4])(?!л)\w*\b)",
        ur"(\b(?!(?:кило)?[тм]ет)(?!смо)[а-яa-z]*(?<!с)т[рp][аa][хx]\w*\b)",
        ur"(\b[к|k][аaoо][з3z]+[eе]?ё?л\w*\b)",
        ur"(\b(?!со)\w*п[еeё]р[нд](и|иc|ы|у|н|е|ы)\w*\b)",
        ur"(\b\w*[бп][ссз]д\w+\b)",
        ur"(\b([нnп][аa]?[оo]?[xх])\b)",
        ur"(\b([аa]?[оo]?[нnпбз][аa]?[оo]?)?([cс][pр][аa][^зжбсвм])\w*\b)",            
        ur"(\b\w*([оo]т|вы|[рp]и|[оo]|и|[уy]){0,1}([пnрp][iиеeё]{0,1}[3zзсcs][дd])\w*\b)",
        ur"(\b(вы)?у?[еeё]?би?ля[дт]?[юоo]?\w*\b)",
        ur"(\b(?!вело|ски|эн)\w*[пpp][eеиi][дd][oaоаеeирp](?![цянгюсмйчв])[рp]?(?![лт])\w*\b)",
        ur"(\b(?!в?[ст]{1,2}еб)(?:(?:в?[сcз3о][тяaа]?[ьъ]?|вы|п[рp][иоo]|[уy]|р[aа][з3z][ьъ]?|к[оo]н[оo])?[её]б[а-яa-z]*)|(?:[а-яa-z]*[^хлрдв][еeё]б)\b)",            
        ur"(\b[з3z][аaоo]л[уy]п[аaeеин]\w*\b)",
    ))

    regexp = re.compile(PATTERN_1, re.U | re.I)

    @staticmethod
    def test(text):
        return bool(RegexpProc.regexp.findall(text))

    @staticmethod
    def replace(text, repl='[censored]'):
        return RegexpProc.regexp.sub(repl, text)

    @staticmethod
    def wrap(text, wrap=('<span style="color:red;">', '</span>',)):
        words = {}
        for word in re.findall(word_pattern, text):
            if len(word) < 3:
                continue
            if RegexpProc.regexp.findall(word):
                words[word] = u'%s%s%s' % (wrap[0], word, wrap[1],)
        for word, wrapped in words.items():
            text = text.replace(word, wrapped)
        return text

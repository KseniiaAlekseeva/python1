import string
from collections import Counter

text = ('Python (в русском языке встречаются названия питон или пайтон) - высокоуровневый '
        'язык программирования общего назначения с динамической строгой типизацией и автоматическим управлением '
        'памятью, ориентированный на повышение производительности разработчика, читаемости кода и его '
        'качества, а также на обеспечение переносимости написанных на нём программ. Язык является полностью '
        'объектно-ориентированным в том плане, что всё является объектами. Необычной особенностью языка является '
        'выделение блоков кода отступами. Синтаксис ядра языка минималистичен, за счёт чего на практике редко '
        'возникает необходимость обращаться к документации. Сам же язык известен как интерпретируемый и '
        'используется в том числе для написания скриптов. Недостатками языка являются зачастую более низкая '
        'скорость работы и более высокое потребление памяти написанных на нём программ по сравнению с аналогичным '
        'кодом, написанным на компилируемых языках, таких как C или C++.')

words = text.translate(text.maketrans('', '', string.punctuation)).lower().split()
print(Counter(words).most_common(10))



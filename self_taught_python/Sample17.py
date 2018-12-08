import re

text = """Giraffes have aroused
 the curiosity of __PLURAL_NOUN__
 since earliest times. The
 giraffe is the tallest of all
 living __PLURAL_NOUN__, but
 scientists are unable to
 explain how it got its long
 __PART_OF_THE_BODY__. The
 giraffe's tremendous height,
 which might reach __NUMBER__
 __PLURAL_NOUN__, comes from
 it legs and __BODYPART__.
"""


def mad_libs(text):
    """
        :param mls: String with parts the users hould fill out surrounded by double underscores.
        Underscores cannot be inside hint e.g., no __hint_hint__ only __hint__.
    """


hints = re.findall("__.*?__",text)
# isは同じobjectかどうかを判断する。
if hints is not None:
    for word in hints:
        q = "{} を入力:".format(word)
        new = input(q)
        text = text.replace(word,new)
    print('\n')
    text = text.replace("\n","　")
    print(text)
else:
    print("引数mlsが無効です")

mad_libs(text)


import mojimoji
import os
import re

SLOT_STR_LIST = [
    "スロ",
    "スロット",
    "s",
    "S",
    "Ｓ",
    "ｓ"
]

def _resist_goseki(goseki_str):
    # print(goseki_str)

    ### 文字列からスキル情報を取得
    m = re.split('(\d)', goseki_str)
    # 文字列を含まないリストを削除しとく
    m = [ s for s in m if len(s) > 0]

    ## 「スロ」のIndexを取得
    slot_idx = None
    _cnt = sum([m.count(l) for l in SLOT_STR_LIST])

    assert _cnt <= 1

    if _cnt == 1:
        slot_idx = m.index('スロ')
    elif _cnt == 0:
        slot_idx = None
        
    ### スキル・スロットで分離し, スキルシミュの規格に合うようにリストを一般化
    if slot_idx is None:
        skill = m
        slot = ['スロ', '', '', '']
    else:
        skill = m[:slot_idx]
        slot = m[slot_idx:]

        while len(slot) < 4:
            slot.append('')

    while len(skill) < 4:
        skill.append('')

    skill[0] = mojimoji.han_to_zen(skill[0])
    skill[2] = mojimoji.han_to_zen(skill[2])

    assert len(skill) == 4, f"Error : skill list length doesn't adopt simulator. list : {skill} len : {len(skill)}"
    assert len(slot) == 4, f"Error : slot list length doesn't adopt simulator. list : {slot} len : {len(slot)}"

    out_skill = ",".join(skill)
    out_slot = ",".join(slot[1:])

    out = f"{out_skill},{out_slot}"

    return out

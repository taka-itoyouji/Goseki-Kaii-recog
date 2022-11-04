from goseki_io import _resist_goseki

goseki_str = [
    "弱点特効2超会心2スロ321",
    "弱点特効2超会心2スロ32",
    "弱点特効2超会心2スロ3",
    # スキル1つのパターン
    "弱点特効2スロ321",
    "弱点特効2スロ32",
    "弱点特効2スロ3",
    # スロ0のパターン
    "弱点特効2超会心2",
    "弱点特効2",
    # スロ0のパターン
    "体力回復量UP2回避距離UP2スロ3",
    ]

for s in goseki_str:
    out = _resist_goseki(s)
    print(f"test OK : {s} -> {out}")
import os

def _resist_csv(ctx, csv_path, resist_str):

    if ~os.path.exists(f"./data/{ctx.author.id}"):
        os.makedirs(f"./data/{ctx.author.id}", exist_ok=True)
        
    csv_path = f"./data/{ctx.author.id}/goseki.csv"

    with open(csv_path, "a+", encoding='shift-jis') as fi:
        fi.write(f"\n{resist_str}")
        fi.seek(0)
        _tmp = fi.read()
        
    with open(csv_path, "w", encoding='shift-jis') as fi:
        fi.write(_tmp)

    return csv_path

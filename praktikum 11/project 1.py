from datetime import datetime,timedelta

def diffDate(x):
    sekarang = datetime.date(datetime.now())
    x = datetime.strptime(x, "%Y-%m-%d").date()
    return abs(x - sekarang)


print("selisih harinya adalah {0} hari".format(diffDate("2021-12-01").days))

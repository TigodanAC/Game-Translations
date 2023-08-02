init -1 python in pattern:
    import re

    nz_related = re.compile("^([A-H])_.*$")
    daily = re.compile("^([A-H])_daily_(\d{1,2})$")
    love = re.compile("^([A-H])_love_(\d{1,2})(|_bLine)$")
    intro = re.compile("^d(\d{1,2})_(\d{1,2})(|_bLine)$")






    nz = re.compile("^.*[A-H].*$")
    sj = re.compile("^.*sj.*$")
    day = re.compile("^.*d[0-9]+.*$")
    date = re.compile("^date_.*$")
    afterdate = re.compile("^ade_.*$")
    special = re.compile("^se_.*$")


    plot_patterns = [nz, sj, day, date, afterdate, special]

    def is_plot(str):
        for pattern in plot_patterns:
            if pattern.match(str):
                return True
        return False
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

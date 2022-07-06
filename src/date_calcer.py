from imports import dt
from imports import birthday, birthtime

bdate = dt.strptime(birthday + ' ' + birthtime, '%Y-%m-%d %H:%M:%S')


def date_calcer(new_dt):
    """Calculates varying time amounts between birthdate and input date."""
    bdate_curr_yr = bdate.replace(year=new_dt.year)
    bdate_curr_mo = bdate.replace(year=new_dt.year, month=new_dt.month)
    btime_curr_day = bdate.replace(year=new_dt.year, month=new_dt.month, day=new_dt.day)

    jan = new_dt.month == 1
    pre_btime = new_dt < btime_curr_day
    pre_bday = new_dt < bdate_curr_yr or (new_dt == bdate_curr_yr and pre_btime)
    pre_bmo = new_dt < bdate_curr_mo or (new_dt == bdate_curr_mo and pre_btime)

    yrs = new_dt.year - bdate.year - (1 if pre_bday else 0)
    mos = new_dt.month - bdate.month + (12 if pre_bday else 0) - (1 if pre_bmo else 0)
    mos_tot = mos + yrs * 12

    days_mo = (new_dt - bdate_curr_mo.replace(year=bdate_curr_mo.year-(1 if jan and pre_bmo else 0),
                                              month=(bdate_curr_mo.month-(0 if not pre_bmo
                                                                          else (-11 if jan else 1))))).days
    days_tot = (new_dt - bdate).days
    weeks = days_tot // 7
    days_wks = days_tot % 7

    diff_secs = (new_dt.replace(day=(new_dt.day + (1 if pre_btime else 0))) - btime_curr_day).seconds
    hrs = diff_secs // (60*60)
    mins = (diff_secs - hrs*60*60) // 60
    secs = diff_secs - hrs*60*60 - mins*60

    return yrs, mos, mos_tot, days_mo, days_tot, hrs, mins, secs, weeks, days_wks

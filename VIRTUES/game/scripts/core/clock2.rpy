define display_clock = False

style clock_text:
    size 29
    xalign 0.5
    font gui.clock_font
    color "#F0EEE9"
    outlines gui.clock_timeext_outlines











define clock_color_meta = {
        DayPeriod.Morning: (Color("#ff675c"), "hsv"),
        DayPeriod.Forenoon: (Color("#ffed78"), "hsv"),
        DayPeriod.Afternoon: (Color("#fbfbfb"), "rgb"), 
        DayPeriod.Evening: (Color("#7abacc"), "hsv"),
        DayPeriod.LateNight: (Color("#72a3d3"), "hsv"),
        DayPeriod.TimeToSleep: (Color("#a066bf"), "rgb")
    }


define clock_t = Time(0)
default clock_color = clock_color_meta[1][0]
default clock_ratio = 0.0
init python:

    def clock_thread():
        
        while(True):
            
            try:
                global t, clock_t, clock_color, clock_ratio
                
                if clock_t.period != t.period:
                    clock_ratio = 0.0
                    while(clock_ratio <= 1.0):
                        time.sleep(0.02)
                        clock_color = get_clock_color(clock_t.period, clock_ratio)
                        clock_ratio += 0.03
                    
                    clock_t.hard_proceed()
                
                else:
                    clock_color = clock_color_meta[clock_t.period][0]
                
                time.sleep(0.02)
            
            except NameError:
                pass
            except:
                traceback.print_exc()

    def clock_solid_func(screen_time, at, *args, **kwargs):
        return Solid(clock_color, *args, **kwargs), 0.01

    def get_clock_color(beg_period, ratio):
        end_period = beg_period+1 if beg_period!=6 else 1
        
        beg_color = clock_color_meta[beg_period][0]
        end_color = clock_color_meta[end_period][0]
        type = clock_color_meta[beg_period][1]
        
        color = get_gradient_color(beg_color, end_color, type, ratio)
        return color

    def get_gradient_color(beg_color, end_color, type, ratio): 
        if type == "rgb":
            color = beg_color.interpolate(end_color, ratio)
        elif type =="hsv":
            color = beg_color.interpolate_hsv(end_color, ratio)
        return color

    def dynamic_period_func(screen_time, at, *args, **kwargs):
        txt = _("{}").format(DAY_PERIOD_NAME[clock_t.period])
        kwargs = {
            "size": 29,
            "xalign": 0.5,
            "yalign": 0.70,
            "font": gui.clock_font,
            "color": "#F0EEE9",
            "outlines": gui.clock_timeext_outlines
        }
        return Text(txt, **kwargs), 0.01

    def dynamic_date_func(screen_time, at, *args, **kwargs):
        txt =  _("Week {}, {}").format(clock_t.week, str(clock_t.day))
        kwargs = {
            "size": 29,
            "xalign": 0.5,
            "yalign": 0.86,
            "font": gui.clock_font,
            "color": "#F0EEE9",
            "outlines": gui.clock_timeext_outlines
        }
        return Text(txt, **kwargs), 0.01

    renpy.invoke_in_thread(clock_thread)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

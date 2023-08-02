label pauser:
    while True:
        pause
    return

label pauser_map:
    $ show_map()
    jump pauser

label pauser_run(func):
    $ func()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

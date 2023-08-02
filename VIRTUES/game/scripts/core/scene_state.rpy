default state = None

init python:

    def is_scene(state):
        return store.state == state

    def set_scene(state):
        store.state = state
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

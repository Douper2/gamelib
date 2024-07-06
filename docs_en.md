# Gamelib documentation

> Disclaimer: The structure of a program in gamelib is the same as pygame because the library is, well, based on pygame.
> Second disclaimer: The library is still a WiP library, so expect things that are in pygame to not be in gamelib.

**Window**
Using the `window_res()` function, you can change the window's resolution.

If you want to change the game's fps, you can with the `game_fps()` function.

With `init()` you initialize everything that you're gonna have in your program.

Using `close_window()` is just a shorter way to say to the program "Hey, if the user clicked the X button, close the program", instead of having to write the normal pygame way.

The `quit()` function is just the `init()` but it uninitializes everything.

The `quit_prg()` function quits the entire program.

The `set_window_size()`, `get_window_size()`,  `set_window_caption()`,  `get_window_caption()` and `set_window_fullscreen()` do exactly what you think. First one, sets the window size, the second, gets the size, the third, sets a window caption (i.e. the text on a window), the forth, gets the caption (e.g. if you wanna check if a caption is "x", if it is, then do something)

**Music in game**

The `play.music()`, `stop.music()`, `pause.music()` and `unpause.music()` functions are pretty straightforward when it comes to what they do.

**Sprites**

As of right now, you can only draw four geometric shapes using the `draw_rectangle()`, `draw_polygon()`, `draw_circle()` and `draw_sline()` functions (P.S. sline in `draw_sline()` means straight line)

**Talking about time in game**

As of (yet again) right now, there are two functions about time. The `time_wait()` and `delay_time()` functions, there will be more functions added later on as the project grows.

**And this is the end of the documentation.**
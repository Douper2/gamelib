# Documentație gamelib

> Notă: Structura unui program în gamelib este aceeași ca cea din pygame pentru că, gamelib e bazat pe pygame.

> A doua notă: Încă se mai lucrează la bibliotecă, deci să te aștepți că nu poți face câteva lucruri.

**Fereastra**
Folosind funcția `window_res()`, poți schimba rezoluția ferestrei.

Dacă vrei să schimbi câte cps (cadre pe secundă) are un joc, poți face asta cu funcția `game_fps()`.

Cu `init()` inițializezi totul ce vei avea în program.

Folosind funcția `close_window()` este un mod mai ușor de a spune programului "Hei, dacă utilizatorul a apăsat butonul X, închide programul", în loc să o faci cum ai face în pygame.

Funcția `quit()` e doar funcția `init()` doar că nu mai inițializeaza totul.

Funcțiile `set_window_size()`, `get_window_size()`,  `set_window_caption()`,  `get_window_caption()` și `set_window_fullscreen()` fac exact ceea ce crezi. Prima, setează dimensiunea ferestrei, a doua, obține dimensiunea, a treia, setează titlul ferestrei (i.e. textul de pe o fereastră), a patra, obține titlul (ex. dacă vrei să verifici dacă titlul ferestrei este "x", și dacă este, atunci fă ceva)

**Muzică în joc**

Funcțiile `play_music()`, `stop_music()`, `pause_music()` și `unpause_music()` sunt destul de clare când vine vorba de ce fac.

**Sprite-uri (imaginile din joc)**

Deocamdată, poți desena doar patru forme geometrice folosind funcțiile `draw_rectangle()`, `draw_polygon()`, `draw_circle()` și `draw_sline()` (P.S. sline în `draw_sline()` înseamnă linie dreaptă)

**Talking about time in game**

Deocamdată (din nou), există două funcții despre timp. Funcțiile `time_wait()` și `delay_time()`, mai târziu vor fi adăugate și alte funcții pe măsură ce proiectul crește.

**Și aici e sfârșitul documentației.**

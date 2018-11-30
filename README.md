Advent of Code 2018
===================

Lösningar för #aoc2017 i Python 3 (testat mot 3.7.1).

Hjälpscript
-----------

För att köra alla lösningar:

    python aoc.py
    

För att starta en ny dag (skapar och populerar filerna `inputs/<dagnummer>.txt`, `solutions/day_<dagnummer>.py` och
`tests/day_<dagnummer>_tests.py`):

    python aoc.py <dagnummer> "<namn på dag>"

Öppna puzzle input manuellt och kopiera innehållet till `inputs/<dagnummer>.txt` som ett sista manuellt steg.


För att köra separat lösning (ersätt `XX` med dagens nummer):

    PYTHONPATH=$(pwd) python solutions/day_XX.py

    
Starta automatisk testkörare (ersätt `XX` med dagens nummer):

    export PYTHONPATH=$(pwd)
    ls solutions/**/*.py | entr -c -r python tests/day_XX_tests.py

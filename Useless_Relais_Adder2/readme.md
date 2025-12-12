Mikrocontroller und Relais Addierer für 16 bit Zahlen.<br/>

yC übernimmt die Ansteuerung der beiden Daten Bytes, serieller Eingang der Bits über Schieberegister in einen Relaisaddierer.<br/>





02.12.2025  Ei verbessertes Model zur 1. Version muss her, erste Überlegungen zur Umsetzung <br/>
06.12.2025  Anlage Ordners struktur, wir bauen die Ordnerstruktur auf den bekannten Addierer auf <br/>
10.12.2025  Probleme mit Wayland und Kicad, keine Lösung in Sicht, werde keinen anderen Displayserver verwenden. Überlegungen zu nötigen Anzahl der Pins und zum Microcontroler, es soll kein PiPico werden. Am besten auch kein Modul.<br/>
12.12.2025  Unter X11 keine Probleme mit KIcad, naja, etwas langsam ales nach letztem Update. Arbeiten an den Schieberegistern<br/>

Hintergrund:

Ein designziel der ersten Version war ein schönes klickendes Gerät für Schreibtisch oder die Wand zu bekommen. Das funktionierte aber nur mit dem Umweg die Daten nacheinander einzuspeisen. Die Reilais klicken mehr oder weniger sonst alle zusammen und nur einmal kurz, das macht keinen Spaß. Hat man nur einen Addierer und füttert die Daten seriell ein, sollte das mehr her machen. Ebenfalls will ich von den Drehschaltern weg und 2 davon sind eh zuviel, könnte ja fast als Nützlich durchgehen, das darf nicht sein. Mit nur 4 Relais klappt wohl auch die VErsorgung per USB  recht einfach und ich habe mehr  LEDs zum zusehen.  <br/>
<br/>


Erkenntnisse:








Bedienung:<br/>






<br/>

Benötigt werden 

3  Schieberegister a 16 Bit für Bit A, Bit B, Ergebnis. Genutzt werden sollen hierzu 74HC595 (Eingangsbits sollen Syncron behandelt werden 1xSRCLR, 1xSRCLK, 1x RCKL, 2x SER Eingang) Ausgangsstufe belibt immer  eingeschaltet.
   Ergebnisregister einen Schritt später als die Eingangsregister, Löschen vermutlich immer zeitgleich mit Eingangsregistern (1x SRCLK, 1x RCKL)  
1  Schieberegister 74HC595 als Zwischenspeicher für den Carry Ausgang, geht auch anders, der Chip ist aber schon da. (1x SRCLK, 1x RCKL)
1  SPI Display   (1x SCA 1x SCL)
1  Microcontroller (1x Eingang für das Ergebnis)


Kombination aus Mikrocontroller und 8-Bit Relais Addierer.<br/>

yC übernimmt die Ansteuerung der beiden Daten Bytes, die über die Relais Addiert werden und sorgt für die Ausgabe.<br/>


![Frontplatte](https://github.com/apxco/Kicad/blob/b3da3c4c3133e040013c6d495d997889dfc1a202/Useless%20Relais%20Addierer/RelaisAddierer/Bildschirmfoto_20250908_125710.png)


04.09.2025  Initiale Idee zum Projekt, Erstellung Schaltbild und Leiterplatte Version 0.1. <br/>
05.09.2025  Weiter an Leiterplatte, grobe Positionierung der Elemente, erste Schritte bei der Programmierung<br/>
06.09.2025  Bauteile zurecht gerückt, klappt nicht gut mit KiCad muss ich sagen.<br/>
07.09.2025  Layout steht soweit, keine wesentlichen Änderungen mehr vorgesehen an der Platine, jetzt Fehlersuche und Polieren.<br/>
08.09.2025  Fehlerkorrekturen im Layout. Wesentlich noch 3,3V zu 5V Pegelwandler für die GPIO Pins eingesetzt.<br/>


Hintergrund:

Ob Röhren oder Relais, die alten Rechner und Steuerungen haben schon etwas faszinierendes. Das beweisen auch jede menge Projekte auf YouTube oder im Netz in denen Leute erstaunliche Maschinen aus diesen alten Konzepten bauen. Der Nutzen der gebauten Maschine selbst, natürlich lernt man viel und hat Spaß beim Bauen, daran kann man natürlich zweifeln. Damit es hier keinen Zweifel gibt, die Idee ist hieraus eine Art Useless Maschine zu machen, ein schönes Stück für den Schreibtisch der ab und an Geräusche macht. Nebenbei ein wenig programmieren und möglichst ein paar Bauteile aus der Bastelkiste aufbrachen.<br/>
<br/>
Mal sehen wie ich weiter komme, der Anfang war erstaunlich schnell gemacht.<br/>




Für die genaue Umsetzung für mich einige Punkte zur Strukturierung der Aufgabe<br/>

Maximale Geschwindigkeit ist nicht erforderlich, es darf gemütlich zugehen.<br/>



Bedienung:<br/>

Drehgeber SW1 Byte A Wert einstellen.<br/>

Drehgeber SW2 Byte B Wert einstellen.<br/>

2 Betriebsarten Normalbetrieb und Zufallsbetrieb<br/>

Tastendruck SW1: Daten Byte 1 und Byte 2 Werden eingeladen Berechnung startet, einmalig (Normalbetrieb).<br/>

Tastendruck SW2: Zufallswerte werden in Byte A und Byte B eingeladen und berechnet, wiederholend (Zufallsbetrieb). Stopp bei weiterem sonstigen Tastendruck.<br/>


Über das Display soll Byte A, Byte B und das Ergebnis als dezimale Werte Angezeigt werden. Ebenfalls ein optische Kontrolle Ergebnis korrekt/nicht korrekt.
Die Ergebnisanzeige und Kontrolle ist fortlaufend in beiden Betriebsarten.<br/>

Im Normalbetrieb werden die Werte Byte A und Byte B über die Drehgeber eingestellt, im Display angezeigt, auf Tastendruck SW1 werden die Daten an die Relais ausgegeben.<br/>

Bis zum Abschluss der Berechnung soll die Ergebnisanzeige ständig aktualisiert werden bis Datenübertagung abgeschlossen ist.<br/>

Im Zufallsbetrieb werden die Werte Byte A und Byte B durch den yC gesetzt, im Display angezeigt, nach kurzer Wartezeit werden die Daten an die Relais ausgegeben.<br/>

Bis zum Abschluss der Berechnung soll die Ergebnisanzeige ständig aktualisiert werden bis Datenübertagung abgeschlossen ist. Wiederholt sich nach kurzer Zeit.<br/>

<br/>

Programmablauf:<br/>

Initialisieren<br/>

Grundwerte einladen<br/>




Kombination aus Mikrocontroller und 8-Bit Relais Addierer.<br/>

yC übernimmt die Ansteuerung der beiden Daten Bytes, die über die Relais Addiert werden und sorgt für die Ausgabe.<br/>


![Frontplatte](https://github.com/apxco/Kicad/blob/b3da3c4c3133e040013c6d495d997889dfc1a202/Useless%20Relais%20Addierer/RelaisAddierer/Bildschirmfoto_20250908_125710.png)


https://www.youtube.com/watch?v=YAB79SiROqY

04.09.2025  Initiale Idee zum Projekt, Erstellung Schaltbild und Leiterplatte Version 1.0 <br/>
05.09.2025  Weiter an Leiterplatte, grobe Positionierung der Elemente, erste Schritte bei der Programmierung<br/>
06.09.2025  Bauteile zurecht gerückt, klappt nicht gut mit KiCad muss ich sagen.<br/>
07.09.2025  Layout steht soweit, keine wesentlichen Änderungen mehr vorgesehen an der Platine, jetzt Fehlersuche und Polieren.<br/>
08.09.2025  Fehlerkorrekturen im Layout. Wesentlich noch 3,3V zu 5V Pegelwandler für die GPIO Pins eingesetzt. Im Endstadium des Wahnsinns Platine bestellt, ab morgen Software <br/>
12.09.2025  vielleicht ab heute Software<br/>
23.9.2025 Platine Version 1.0 wurde geliefert, aufgebaut ohne Relais für Fehlersuche. Zu kleiner Fußabdruck bei den Freilaufdioden, Kurzschluss an den Multiplexern zwischen +5V und SDA, Ausgänge der Multiplexer empfindlich für statische Aufladung. Bauteilwerte scheinen OK zu sein soweit. Lötpasstenschablone ist scharfkantig.<br/>
20.10.2025 Nach der schmerzlichen Erkenntnis, dass nicht alle PiPico bords die gleiche Pinbelegung haben, gibt es einen Fortschritt bei der Programmierung. Kann den TCA9534 jetzt ohne zusätzliche Bibliotheken ansprechen, zumindest beim Schreiben. Ansteuerung der Relais funktioniert trotz Open Collector Ausgang.<br/>
21.10.2025 Platine Version 1.0 weitere Fehler bei der Relaisverschaltung, wird in Version 2.0 korrigiert. <br/>
23.10.2025 Soweit ist die SW fertig. Umsetzen der Ergebnis OK Anzeige mittels Inversion der Anzeige. Die verwendete Bibliothek kommt mit 2 Drehschaltern scheinbar nicht gut klar, immer einer der Schalter wird nicht richtig ausgewertet. Lasse es jetzt so, die Art der Bedienung, x10 wenn Druck auf SW1 für beide Bytes gefällt mir auch. Platine V2.0 Angefangen und erste Korrrekturen vorgenommen. Version 1.0 konnte ich mit zusätzlichen Leitungen zur Mitarbeit bewegen, funktioniert damit. Werde die Version 2.0 mit allen Korrekturen online stellen, aber nur Bestellen und Aufbauen wenn ich eine 2. Maschine baue. <br/>
24.10.2025 Ich definiere die Software als fertig. Für den Zufallsmodus werden die Eingangswerte in 10 Schritten nacheinander eingegeben, ganz witzig anzusehen. 


Hintergrund:

Ob Röhren oder Relais, die alten Rechner und Steuerungen haben schon etwas faszinierendes. Das beweisen auch jede Menge Projekte auf YouTube oder im Netz in denen Leute erstaunliche Maschinen aus diesen alten Konzepten bauen. Den Nutzen der gebauten Maschine selbst, natürlich lernt man viel und hat Spaß beim Bauen, daran kann man aber zweifeln. Damit es hier keinen Zweifel gibt, die Idee ist hieraus eine Art Useless Maschine zu machen, ein schönes Stück für den Schreibtisch der ab und an Geräusche macht. Nebenbei ein wenig programmieren und möglichst ein paar Bauteile aus der Bastelkiste aufbrauchen.<br/>
<br/>


Erkenntnisse:

Trotz zusätzlich notwendiger Verbindungen auf der Rückseite, zu kleinen Pads und der nicht korrekten Ausgangsbeschaltung der TCA9534 funktioniert die Platine auf anhieb. Man muss einfach Glück haben.<br/>
Ich bin kein guter Programmierer. Python macht es jedem recht einfach auch sowas umzusetzen. Insbesondere die Programmierumgebung kommt einem solchen Projet sehr entgegen. Allerdings wird es schnell zeitkritisch bzw. Dinge die man gerne über Interupts lösen würde, gehen so nicht. Zumindest ich bekomme es nicht hin.<br/>

Für mein nächstes Projekt würde ich eine andere Spannungsversorgung vorsehen. Genaugenommen mag ich die Buchse nicht. USBC wäre eleganter und in dem Leistungsbereich möglich gewesen. Die maximal Stromaufnahme beträgt bei 12V um 1A. Die Schaltung funktioniert noch bis etwa 10V, danach gibt es rechenfehler durch faule Relais ;).<br/>

Es soll ja useless sein und damit ist Übertreibung sozusagen Teil des Spiels. Da aber noch Ports am PiPico frei sind, würde ich die Auswertung der Ausgangs Bytes über den PiPico direkt machen und nicht mehr über einen TCA9534. Spart kosten, macht die Schaltung einfacher und hat hier keinen Nachteil. Für das Carry Bit ist es hier sowieso so gemacht.



Für die genaue Umsetzung für mich einige Punkte zur Strukturierung der Aufgabe<br/>

Maximale Geschwindigkeit ist nicht erforderlich, es darf gemütlich zugehen.<br/>



Bedienung:<br/>

Drehgeber SW1 Byte A Wert 1x einstellen. Bei Druck auf SW1 10x <br/>

Drehgeber SW2 Byte B Wert einstellen. Bei Druck auf SW1 10x <br/>

3 Betriebsarten Normalbetrieb und Zufallsbetrieb<br/>

Tastendruck SW2: Daten Byte 1 und Byte 2 Werden eingeladen Berechnung startet, einmalig. Ohne weiteren Tastendruck läuft Timer für Zufallsbetrieb (wiederholend).  <br/>


Über das Display soll Byte A, Byte B und das Ergebnis als dezimale Werte Angezeigt werden. Ebenfalls ein optische Kontrolle Ergebnis korrekt/nicht korrekt.
Die Ergebnisanzeige und Kontrolle ist fortlaufend in beiden Betriebsarten.<br/>

Im Normalbetrieb werden die Werte Byte A und Byte B über die Drehgeber eingestellt, im Display angezeigt, auf Tastendruck SW2 werden die Daten an die Relais ausgegeben.<br/>

Bis zum Abschluss der Berechnung soll die Ergebnisanzeige ständig aktualisiert werden bis Datenübertagung abgeschlossen ist.<br/>

Im Zufallsbetrieb werden die Werte Byte A und Byte B durch den yC gesetzt, im Display angezeigt, und nacheinander augegeben <br/>

Bis zum Abschluss der Berechnung soll die Ergebnisanzeige ständig aktualisiert werden bis Datenübertagung abgeschlossen ist. Wiederholt sich nach kurzer Zeit.<br/>

<br/>

V1.0 Hack auf fast 2.0 ;-)

![Rückseite](https://github.com/apxco/Kicad/blob/886e481ea10ae2acfe101e60ca78e179da667744/Useless%20Relais%20Addierer/RelaisAddierer/Adder1_0_hinten.jpg)

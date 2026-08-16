# Designprinzipien der produktiven App

Diese Leitlinien sind direkt aus der produktiven `index.html` abgeleitet. Sie
bilden die visuelle Grundlage für künftige Layouts. Ein Mockup darf Anordnung
und Navigation erproben, soll aber die hier beschriebenen Merkmale nicht ohne
bewusste Designentscheidung ersetzen.

## 1. Charakter: freundlich, haptisch und spielzeugnah

Die Oberfläche übersetzt das physische Brettspiel in eine warme, leicht
dreidimensionale Browseransicht. Sie ist nicht minimalistisch-flach. Abgerundete
Formen, weiche Schatten, farbige Kanten und kurze Bewegungen vermitteln
Materialität und direkte Bedienbarkeit.

## 2. Feste visuelle Identität

- Der Hintergrund ist warm und hell, im Standard ein sanftes Creme (`#fbf4e4`)
  mit dezenter Aufhellung am oberen Rand.
- Fließtext und wichtige Werte verwenden ein dunkles, warmes Braun (`#33291b`)
  statt Schwarz.
- Die Schriftfamilie ist rund und freundlich; Systemschriften mit abgerundeter
  Anmutung werden bevorzugt.
- Überschriften, Buttons und kleine Beschriftungen sind kräftig gesetzt.
- Zeitwerte und Würfelkoordinaten verwenden eine Monospace-Schrift, weil ihre
  Zeichen dabei ruhig und gut vergleichbar bleiben.
- Die Wortmarke „Genius Square“ bleibt zweifarbig. Die kleine Kennzeichnung
  „Trainer“ steht darüber in Versalien mit deutlicher Laufweite.

## 3. Physische Spielelemente bleiben themenunabhängig

### Würfel

- Würfel sind quadratisch, deutlich abgerundet und elfenbeinfarben.
- Ein heller Verlauf, eine beige Unterkante und ein weicher Schatten erzeugen
  den Eindruck eines echten Spielsteins.
- Koordinaten stehen groß, dunkel und kräftig in der Mitte.
- Beim Würfeln ist eine kurze, federnde Bewegung vorgesehen.

### Brett und Vertiefungen

- Das Brett ist eine große, eigenständige farbige Fläche mit stark gerundeten
  Ecken.
- Eine dunklere Unterkante und ein Außenschatten geben ihm sichtbare Tiefe.
- Die 36 Positionen sind kreisrunde, nach innen schattierte Vertiefungen – keine
  quadratischen Rasterfelder.
- Spalten `A–F` und Zeilen `1–6` bleiben direkt am Brett sichtbar.

### Holzblocker

- Blocker sind runde Holzdübel und ein zentrales Wiedererkennungsmerkmal.
- Mehrere radiale Verläufe bilden Holzfarbe, Lichtreflex, Maserung und dunklere
  Kanten nach.
- Außen- und Innenschatten lassen die Dübel auf dem Brett aufliegen.
- Beim Erscheinen fallen sie kurz federnd in die Vertiefung.
- Elfenbein-Würfel und Holzdübel werden durch Farbthemen nicht verändert.

## 4. Farbthemen ändern Farbe, nicht Form

Die Themen „Standard“, „Koralle“ und „Mint“ steuern nur:

- Seitenhintergrund
- Brettfarbe, Brettkante und Brettbeschriftung
- Farben und Kanten der beiden Hauptaktionen
- Akzentfarbe sowie Farben der Wortmarke

Geometrie, Abstände, Würfelmaterial, Holzblocker und Informationshierarchie
bleiben gleich. Themen werden als kompakte, abgerundete Chips mit kleinen
Farbpunkten dargestellt. In einer kompakteren Navigation dürfen diese Chips in
ein Zahnrad-Menü wandern, ihr Aussehen und ihre Funktion bleiben aber erhalten.

## 5. Flächen, Radien und Tiefe

- Karten für Steuerung und Historie sind weiß, weich beschattet und ungefähr
  `20px` abgerundet.
- Das Brett ist mit ungefähr `26px` noch etwas stärker abgerundet.
- Würfel (`16px`) und Aktionsbuttons (`15px`) nutzen etwas kleinere Radien.
- Primäraktionen haben eine farblich dunklere Unterkante. Beim Drücken bewegen
  sie sich sichtbar nach unten; diese Haptik gehört zur Designsprache.
- Haarlinien und Tabellenunterteilungen sind sehr zurückhaltend und warmgrau.

## 6. Informationshierarchie

Die primäre Aufgabe ist das laufende Spiel. Folgende Elemente gehören deshalb
inhaltlich zusammen und sollten auf einer mobilen Spielansicht möglichst ohne
vertikales Scrollen erreichbar sein:

1. die sieben Würfelergebnisse,
2. das Brett mit Blockern und Koordinaten,
3. „Neue Kombination“ und „Fertig",
4. die laufende Zeit.

Knapp ist dabei die Höhe, nicht die Breite. Deshalb gilt: **Das Brett ist der
nachgebende Block.** Es bekommt, was nach Würfeln und Steuerung übrig bleibt,
und bleibt dabei immer quadratisch. Würfel, Buttons und Zeitanzeige haben feste
Obergrenzen und schrumpfen nur mit der bespielbaren Höhe – gerechnet ohne die
Safe-Area-Ränder, die auf dem Gerät rund 90px kosten.

Die Historie ist sekundär. Sie darf auf eine eigene, horizontal erreichbare
Ansicht ausgelagert werden. Die Themenwahl ist eine seltene Einstellung und
eignet sich für ein kleines Zahnrad-Menü statt einer permanenten Hauptseite.

## 7. Sprache und Bedienung

- Beschriftungen bleiben kurz, direkt und deutsch.
- Hauptaktionen sind groß, farbig und klar voneinander unterscheidbar.
- Deaktivierte Aktionen bleiben sichtbar, werden aber stark abgeblendet.
- Bestzeiten erhalten Akzentfarbe und Sternmarkierung.
- Animationen sind kurz und funktional; bei `prefers-reduced-motion` werden sie
  abgeschaltet.
- Safe-Area-Abstände werden für Android-/PWA- und andere Vollbildgeräte
  berücksichtigt.

## 8. Leitplanken für Layout-Mockups

Layoutänderungen dürfen die verfügbare Displayhöhe besser nutzen, Bereiche
kompakter anordnen und zwischen Spiel und Historie wischen lassen. Dabei gelten
folgende Elemente als unveränderliche visuelle Anker:

- zweifarbige Wortmarke und runde Typografie,
- cremefarbene Grundstimmung,
- elfenbeinfarbene, haptische Würfel,
- blaues beziehungsweise themenfarbenes Brett mit runden Vertiefungen,
- realistisch wirkende Holzblocker,
- grüne und orange Hauptaktionen mit sichtbarer Unterkante,
- große Monospace-Zeitanzeige,
- weiße, weich abgerundete Karten.

Neue Navigationselemente sollen zurückhaltend bleiben und dürfen nicht stärker
wirken als Brett, Timer und Spielaktionen.

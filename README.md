# Genius Square Trainer (Web-App / PWA)

Würfel-Trainer für *Genius Square*: Kombination würfeln, Zeit stoppen, Historie
der letzten 10 Spiele führen. Läuft komplett im Browser – ohne Server, ohne
Installation nötig. Als PWA lässt sie sich auf Android „installieren" und
funktioniert danach auch offline.

## Funktionen

- **7 echte Genius-Square-Würfel** (Original-Seiten) mit einem Klick werfen
- **6×6-Brett**, das die Blocker-Positionen direkt anzeigt – das Plus gegenüber
  reinen Würfeln
- **3 Farbthemen** (Aktuell, Koralle, Mint) per Umschalter oben; die Wahl wird
  gespeichert
- **Timer** (MM:SS.d), startet beim Würfeln, stoppt bei „Fertig"
- **Historie** der letzten 10 Spiele mit Zeit + Kombination, **Bestzeit** wird
  hervorgehoben
- **Dauerhaftes Speichern** im Browser (übersteht Neustart) – über `localStorage`
- **Offline-fähig** dank Service Worker

## Dateien

```
index.html              die komplette App (HTML/CSS/JS in einer Datei)
manifest.webmanifest    PWA-Manifest (Name, Icons, Farben)
sw.js                   Service Worker (Offline-Cache)
icons/                  App-Icons (192, 512, maskable)
make_icons.py           erzeugt die Icons neu (optional, braucht Python + Pillow)
paletten-mockup.html    Entwicklungsansicht zum Vergleichen der Farbpaletten
```

## Lokal testen

Wegen des Service Workers am besten über einen kleinen Webserver statt per
Doppelklick öffnen:

```bash
cd genius-square-trainer
python3 -m http.server 8000
# dann im Browser: http://localhost:8000
```

## Über GitHub Pages hosten

1. Diese Dateien in das bestehende Repository committen und hochladen:

   ```bash
   cd genius-square-trainer
   git add .
   git commit -m "Genius Square Trainer als Web-App/PWA"
   git push -u origin main
   ```

2. Im Repository: **Settings → Pages**.
3. Unter *Build and deployment* bei *Source* **„Deploy from a branch"** wählen,
   Branch **`main`**, Ordner **`/ (root)`**, dann **Save**.
4. Nach ein bis zwei Minuten ist die App erreichbar unter:

   ```
   https://andreas-luehning.github.io/genius-square-trainer/
   ```

> Wichtig: Alle Pfade in der App sind **relativ** (`sw.js`, `manifest.webmanifest`,
> `icons/...`). Dadurch funktioniert sie in diesem Unterordner ohne Anpassung.
> HTTPS liefert GitHub Pages automatisch – das braucht die PWA.

## Als App auf Android installieren

1. Die GitHub-Pages-URL in **Chrome** auf dem Handy öffnen.
2. Menü (drei Punkte) → **„App installieren"** bzw. **„Zum Startbildschirm
   hinzufügen"**.
3. Das Icon liegt danach im App-Drawer; die App startet im Vollbild (ohne
   Browser-Leiste) und läuft auch offline.

## Updates ausrollen

Wenn du an der App etwas änderst, im `sw.js` die Cache-Version erhöhen
(z. B. `gs-trainer-v1` → `gs-trainer-v2`) und neu pushen. So laden installierte
PWAs die neue Version, statt die alte aus dem Cache zu zeigen.

## Icons neu erzeugen (optional)

```bash
python3 -m pip install pillow
python3 make_icons.py
```

Das Skript erzeugt alle Dateien unter `icons/`. Die normale Variante greift das
Standardtheme der App auf; die maskierbare Variante hält das Motiv in der von
Android benötigten Sicherheitszone.

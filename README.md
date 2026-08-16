# Genius Square Trainer (Web-App / PWA)

Würfel-Trainer für *Genius Square*: Kombination würfeln, Zeit stoppen, Statistik
führen. Läuft komplett im Browser – ohne Server, ohne Installation nötig. Als PWA
lässt sie sich auf Android „installieren" und funktioniert danach auch offline.

## Aufbau

Drei Seiten, per Pillen-Menü **und** horizontalem Wischen erreichbar:

1. **Spiel** – Würfel, Brett, Aktionen, Timer
2. **Statistik** – Kennzahlen und die letzten Spiele
3. **Einstellungen** – Farbprofil, Bildschirm-Wachhaltung, Daten löschen

## Funktionen

- **7 echte Genius-Square-Würfel** (Original-Seiten) mit einem Klick werfen
- **6×6-Brett**, das die Blocker-Positionen direkt anzeigt – das Plus gegenüber
  reinen Würfeln
- **Timer** (MM:SS.d), startet beim Würfeln, stoppt bei „Fertig"
- **Statistik**: Bestzeit, Durchschnitt, Gespielt (gesamt) und Heute; darunter die
  letzten 10 Spiele mit Zeit + Kombination, **Bestzeit** hervorgehoben
- **3 Farbprofile**: Standard, Koralle und Mint (ein viertes Profil „Original" mit
  den Farben der echten Spielkomponenten liegt auskommentiert in `index.html`
  bereit – samt Herleitung aus der offiziellen Anleitung)
- **Bildschirm immer an** über die Screen-Wake-Lock-API (braucht HTTPS; Browser
  ohne Unterstützung zeigen den Schalter deaktiviert)
- **Dauerhaftes Speichern** im Browser (übersteht Neustart) – über `localStorage`
- **Offline-fähig** dank Service Worker

## Gespeicherte Daten (`localStorage`)

| Schlüssel | Inhalt |
| --- | --- |
| `gs-trainer-runs-v1` | die letzten 50 Läufe `{t, combo, ts}`, neueste zuerst |
| `gs-trainer-stats-v1` | Gesamtwerte `{count, sumSeconds, bestSeconds}` – bleiben erhalten, auch wenn die Liste gekürzt wird |
| `gs-trainer-theme` | gewähltes Farbprofil |
| `gs-trainer-wakelock` | `1`/`0` für „Bildschirm immer an" |

Eine ältere `gs-trainer-history-v1` wird beim ersten Start automatisch übernommen
(ohne Zeitstempel, zählt daher nicht für „Heute") und danach entfernt.
„Statistik löschen" auf der Einstellungsseite entfernt Läufe und Gesamtwerte,
lässt Farbprofil und Wake-Lock-Schalter aber unberührt.

## Dateien

```
index.html              die komplette App (HTML/CSS/JS in einer Datei)
manifest.webmanifest    PWA-Manifest (Name, Icons, Farben)
sw.js                   Service Worker (Offline-Cache)
icons/                  App-Icons (192, 512, maskable)
icon-512.png            Quelldatei für die App-Icons
make_icons.py           erzeugt die Icons neu (optional, braucht Python + Pillow)
DESIGNPRINZIPIEN.md     Designleitlinien der App
mockup/                 Layout- und Palettenentwürfe (nicht Teil der App)
ressources/             offizielle Spielanleitung als PDF (Farbquelle für Themen)
```

## Lokal testen

Wegen des Service Workers am besten über einen kleinen Webserver statt per
Doppelklick öffnen:

```bash
cd genius_square_trainer
python3 -m http.server 8000
# dann im Browser: http://localhost:8000
```

## Über GitHub Pages hosten

1. Auf GitHub ein neues Repository anlegen, z. B. `genius-square-trainer`.
2. Diese Dateien hochladen (per Website „Add file → Upload files" oder per Git):

   ```bash
   cd genius_square_trainer
   git init
   git add .
   git commit -m "Genius Square Trainer als Web-App/PWA"
   git branch -M main
   git remote add origin https://github.com/DEIN-NAME/genius-square-trainer.git
   git push -u origin main
   ```

3. Im Repository: **Settings → Pages**.
4. Unter *Build and deployment* bei *Source* **„Deploy from a branch"** wählen,
   Branch **`main`**, Ordner **`/ (root)`**, dann **Save**.
5. Nach ein bis zwei Minuten ist die App erreichbar unter:

   ```
   https://DEIN-NAME.github.io/genius-square-trainer/
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

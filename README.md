# Team5
Im Frühlingssemester 2025 wurden wir beauftragt, ein Anwendungsszenario für ein Hotelreservierungssystem zu entwickeln. Dieses Projekt baut auf der Arbeit des vorangegangenen Semesters auf, in dem wir eine Datenbank für den Kurs "Datenbasierte Unternehmensanwendung" entworfen haben.
Wie in den Projektrichtlinien beschrieben, verwenden wir verschiedene Werkzeuge, um unseren Entwicklungsprozess zu unterstützen:
- Visual Paradigm für das Klassendiagramm
- SQLite für die Datenbank
- Jupyter Notebook für die Dokumentation sowie Ausführung der Codes
- GitHub für die Versions Controlle und Projekt Management

## How to use
### Voraussetzungen:
- VS Code oder Pycharm als Applikation
- `requirements.txt` ausführen während der Installation (siehe Schritt 3)

1. ### Virtuelle Umgebung erstellen
```
python -m venv ./.venv
```

2. ### Script aktivieren
#### Windows:
```
.\.venv\Scripts\activate
```

#### MacOS:
```
source .venv/bin/activate
```


3. ### Jetzt das Requirement installieren
#### Windows:
```
pip install -r .\requirements.txt
```

#### MacOS:
```
pip install -r ./requirements.txt
```


## Projekt Management
### Vorgehensweise
Nachdem wir das Klassendiagramm erstellt hatten, haben wir das Projekt in zwei Hauptbereiche aufgeteilt:
##### Fokus Hotel:
- `Facility`
- `Room`
- `Room Type`
- `Hotel`

##### Fokus Gast:
- `Booking`
- `Invoice`
- `Guest`
- `Address`

Die Aufgaben wurden entsprechend dieser Aufteilung im Team verteilt. Zum Coden haben wir uns letztendlich für Visual Studio Code entschieden, da wir die praktische Erfahrung in einem sehr verbreiteten und bekannten Programm als sehr hoch einschätzen.
Für die Organisation und Kommunikation haben wir hauptsächlich unseren WhatsApp-Gruppenchat genutzt. Darüber haben wir besprochen, bis wann welche Teile fertiggestellt werden sollen, und regelmässig Herausforderungen und offene Fragen diskutiert. Zusätzlich haben wir uns in regelmässigen online oder vor Ort ausgetauscht.
Im Verlauf des Projekts haben wir ausserdem entdeckt, dass GitHub ein integriertes Kanban-Board anbietet. Dieses haben wir gegen Ende des Projektabschnitts ergänzend verwendet, um Aufgaben visuell zu organisieren und den Fortschritt besser nachverfolgen zu können.

Insgesamt haben wir also ein **hybrides** Planungssystem verwendet – bestehend aus WhatsApp-Kommunikation für schnelle Absprachen und GitHub Kanban für strukturierte Aufgabenverteilung.

## Projektüberblick und Teamdynamik:
Im Laufe des Projekts zeigte sich , dass zwei Teammitglieder aus unterschiedlichen Gründen nicht aktiv zum Projekt beitrugen. Nach Rücksprache mit den Dozierenden wurde gemeinsam entschieden, das Projekt im verbleibenden kleineren Team weiterzuführen. Diese Entscheidung war nicht nur notwendig, sondern auch eine wertvolle Lernerfahrung im Hinblick auf Eigenverantwortung, Projektorganisation und Kommunikation im Team.

### Saliou Dieng - *Architekt der Unterkunftsstruktur und Basisstruktur*
<br> Verantwortliche Klassen (Model, Data Access, Business Logic, UI):
- `Facility`
- `Room`
- `Room Type`
- `Hotel`

<br> Entsprechende Userstories implementiert:
- 1 - 1.4
- 1.5 und 1.6
- 2 und 2.1
- 3 - 3.3
- 9
- 10
- 11.1


#### Technische Umsetzung:
Zu meinen Aufgabenbereichen zählten unter anderem die Modellierung und Implementierung der Klassen Facility, Room, RoomType und Hotel. Anfangs fiel es mir noch schwer, die genaue Trennung zwischen den einzelnen Schichten (Model, Data Access, Business Logic, UI) konsequent einzuhalten. Viele Funktionen wurden zunächst direkt in die Model-Klassen eingebaut. Doch im weiteren Verlauf entwickelte ich ein besseres Verständnis für die Architektur, wodurch ich die Logik gezielter auslagern und die Zuständigkeiten klarer strukturieren konnte.

Bei der Modellierung war mir wichtig, sinnvolle Abhängigkeiten zu berücksichtigen – zum Beispiel kann ein Room-Objekt nur erstellt werden, wenn es ein zugehöriges Hotel sowie einen gültigen RoomType gibt. Auch Typüberprüfungen wurden direkt in den Klassen umgesetzt, um Datensicherheit und Fehlerprävention zu gewährleisten.

#### Business Logic und Data Access:
Ein zentrales Prinzip meines Vorgehens war: Die Data Access Layer (DAL) liefert stets alle vorhandenen Daten (z. B. alle Hotels oder alle Zimmer), während die gezielte Filterung ausschließlich in der Business Logic erfolgt. Diese Trennung war für mich eingängiger, da ich so alle Daten an einem Ort sammeln und später bedarfsgerecht filtern konnte. Dadurch war die Business Logic zwar aufwendiger, aber auch flexibler.

Zur Strukturierung nutzte ich unter anderem einen RoomManager und einen HotelManager, die als zentrale Schnittstellen zwischen DAL und UI dienten. Sie übernahmen Validierungen, Filterungen (z. B. nach Ort, Personenanzahl oder Preis) und die Geschäftsregeln. Ich habe bewusst nur zwei zentrale Manager implementiert, um die Komplexität im ersten Durchlauf überschaubar zu halten.

#### User Interface:
Im Frontend konzentrierte ich mich auf die Implementierung der HotelUI. Hier lag mein Fokus darauf, eine möglichst benutzerfreundliche Bedienung zu ermöglichen – unter anderem durch gezielte Eingabehilfen (z. B. für Städte, Zimmergrößen oder Preiskategorien). Ich habe versucht, Fehlerquellen wie falsche Eingabetypen durch gezielte Abfragen und Validierungen frühzeitig zu vermeiden. Bei individuellen Wünschen arbeitete ich mit dem Input helper y_n, in den Funktionen sind die Parameter als None gesetzt, so muss der User nicht zwingend nach etwas filtern und kann es individuell aussuchen.

Dabei fiel mir rückblickend auf, dass ich manche wiederverwendbaren Logiken noch stärker hätte auslagern können. Trotzdem konnte ich durch die modulare Struktur bereits viele Elemente mehrfach einsetzen.

#### Persönliche Reflexion
Durch das Projekt habe ich nicht nur mein Verständnis für die Softwarearchitektur in Python deutlich verbessert, sondern auch gelernt, worauf es bei der sauberen Trennung von Zuständigkeiten ankommt. Wäre ich nochmals am Anfang, würde ich die Schichten von Anfang an klarer aufbauen, die Data Access Layer eventuell stärker mit gezielten SQL-Abfragen optimieren (z. B. per Joins), und noch häufiger testen.

Besonders stolz bin ich darauf, wie sich mein Umgang mit Python im Laufe des Projekts entwickelt hat – von ersten Experimenten bis hin zu einer durchdachten, funktionsfähigen Anwendung mit nachvollziehbarer Struktur. Auch wenn noch Verbesserungspotenzial besteht (z. B. bei der Wiederverwendung von UI-Elementen), überwiegt für mich klar das Gefühl, viel gelernt und ein solides Ergebnis erarbeitet zu haben.

Ich hätte gerne mehr und tiefer mit modernen Libaries wie pandas und SQLAlchemy gearbeitet, dafür reichte die Zeit aber leider nicht aus. 




### Anna Müller - *Architektin des Gasterlebnisses*
<br> Zugeteilte Klassen in Model, Data Access, Business Logic und UI Layer umgesetzt:
- `Booking`
- `Invoice`
- `Guest`
- `Address`

<br> Entsprechende Userstories implementiert:
- 1.4
- 2.2
- 4 - 8
<br>

#### Technische Umsetzung
Neben der Modellierung und Implementierung der Klassen Booking, Invoice, Guest und Address habe ich auch die Beziehungen zwischen diesen Klassen modelliert. Das war zwar herausfordernd, aber letztlich sehr lohnend, weil man am Ende ein klares Gesamtbild der Struktur erkennen konnte. Das Modell bildet eine zentrale Grundlage für alle weiteren Schichten der Architektur – besonders für die Business Logic und die Datenzugriffe. Ich habe ausserdem auf eine saubere Trennung zwischen Modell, Data Access, Business Logic und UI geachtet. Viele Funktionen waren anfangs noch in den Modellklassen, wurden aber mit wachsendem Architekturverständnis an die passenden Stellen verschoben. Dabei habe ich gelernt, typische Fehler in der Business Logic besser zu erkennen und zu vermeiden.

#### Business Logic und Data Access:
Im Logic- und Data-Access-Layer habe ich versucht, alle sinnvollen Datenabfragen abzudecken – etwa Buchungen nach bestimmten Kunden, sämtliche Buchungen insgesamt oder alle Hotels in einer bestimmten Stadt. In der Business Logic war es mir besonders wichtig, kritisch zu denken: Welche Prüfungen sind hier wirklich notwendig? Wo muss ich zusätzliche Validierungen ergänzen, die der Data Access Layer nicht übernehmen kann? Während die Data Access Layer vor allem auf die Datentypen achtet – also etwa prüft, ob Eingaben wirklich Integer oder String sind – konzentriert sich die Business Logic auf inhaltliche Regeln. Zum Beispiel: Das Check-In-Datum darf nicht nach dem Check-Out-Datum liegen. Diese Trennung war für mich ein wichtiger Lernprozess, um eine saubere, logische Architektur aufzubauen

#### User Interface:
Ich habe darauf geachtet, alle möglichen Pfade im System abzudecken – insbesondere im Hinblick auf unterschiedliche Nutzereingaben. Das bedeutet zum Beispiel, was passiert, wenn statt einer Zahl ein String eingegeben wird. Aber auch funktionale Szenarien wie: ‚Ich möchte noch eine Buchung hinzufügen‘, ‚Ich will eine weitere Buchung stornieren‘ oder ‚Ich möchte eine weitere Buchung fakturieren‘. Solche Überlegungen haben meine Entscheidungen in der UI beeinflusst. Ich habe intensiv mit den UI-Komponenten gearbeitet, besonders mit dem UI-Booking und dem UI-Input-Helper, und teilweise auch mit der Hotel UI, um die Nutzung möglichst benutzerfreundlich zu gestalten. Mein Fokus lag dabei stark auf der Frage: Was würde ich mir als Nutzer von einem Hotelreservierungssystem am meisten wünschen?

#### Persönliche Reflexion
Durch dieses Projekt habe ich wirklich viel gelernt – nicht nur fachlich, sondern auch persönlich. Ich habe verstanden, wie ich in einem solchen Projekt strukturiert vorgehen kann.

Gleichzeitig habe ich auch gelernt, besser mit Frustration umzugehen. Wenn ein Fehler auftrat, den ich nicht sofort verstanden habe, bin ich konsequent Zeile für Zeile durchgegangen und habe mich gefragt: Was funktioniert hier nicht? Was macht der Code genau? Warum passiert das so? Diese Vorgehensweise hat mir geholfen, die wahren Ursachen zu erkennen.

Diese Strategie hat mir letztlich nicht nur geholfen, konkrete Probleme zu lösen, sondern auch mein Verständnis für Python insgesamt deutlich zu vertiefen. Ich habe gemerkt: Mit Ausdauer, systematischem Denken und einer "gewissen" Ruhe lassen sich auch komplexe Herausforderungen meistern. Das hat mir Mut gemacht für dieses Projekt und für künftige Aufgaben.


## UML

![image](https://github.com/user-attachments/assets/4b941f4b-ab1e-47da-bd5d-bf659b77275c)

Das UML haben wir mit Visual Paradigm erstellt und das UML bildet die Beziehung zwischen den Klassen Hotel, Booking, Invoice, Room, Guest, Address, Room Type und Facility. Wir sind nach dem gleichen Schema gegangen wie das von der Datenbank.


![image](https://github.com/user-attachments/assets/88c00dcb-0977-4137-ad5d-8224df509808)

## Abschluss
Die Umsetzung dieses Projekts ermöglichte es uns, unsere Kenntnisse in Python und objektorientierter Programmierung praxisnah zu vertiefen – gleichzeitig war es auch eine wertvolle Lernerfahrung in Bezug auf Teamarbeit, Kommunikation und Projektorganisation.

Zu Beginn hatten wir Schwierigkeiten, überhaupt in das Projekt hineinzufinden. Es fiel uns nicht leicht, die ersten Schritte zu machen, da vieles neu und komplex wirkte. Zusätzlich gab es technische Hürden: Wir begannen in Deepnote, hatten jedoch anfangs grosse Schwierigkeiten, dies korrekt auf GitHub zu pushen. Das führte zu Unsicherheiten und Zeitverlust.

Erst als wir gemeinsam beschlossen, eine feste Struktur zu definieren und Rollen aufzuteilen, kam das Projekt in Bewegung. Durch die Erstellung eines Klassendiagramms gewannen wir Klarheit über die Architektur und konnten die Aufgaben sinnvoll aufteilen. Ab der Verbindung der Datenbank mit dem Projekt hatten wir unser "Aha" Moment und der Stein begann zu rollen.

Die Trennung in zwei Verantwortungsbereiche – Hotelstruktur und Gastprozess – ermöglichte es uns, effizient und parallel zu arbeiten. Trotzdem wurde schnell klar, dass eine enge Abstimmung notwendig war, da viele Klassen miteinander interagieren. Regelmässige Meetings, kontinuierliche Kommunikation über WhatsApp sowie spätere Organisation über ein GitHub-Kanban-Board haben sich dabei als sehr hilfreich erwiesen.

Technisch konnten wir durch die Arbeit mit mehrschichtigen Strukturen (Model, Data Access, Business Logic, UI) ein tiefes Verständnis für modulare Programmierung entwickeln. Besonders herausfordernd war die saubere Fehlerbehandlung und Validierung der Eingaben – Themen, die wir im Laufe des Projekts stark verbessern konnten.

Auch die Verwendung von Jupyter Notebook zur Dokumentation hat sich als äusserst nützlich erwiesen. Es ermöglichte uns, unsere Gedanken, Zwischenschritte und Testläufe direkt im Code zu dokumentieren, was sowohl bei der Zusammenarbeit als auch beim späteren Reflektieren sehr hilfreich war.

Abschliessend können wir sagen, dass uns dieses Projekt nicht nur fachlich weitergebracht hat, sondern uns auch gezeigt hat, wie wichtig klare Kommunikation, strukturierte Planung und Teamzusammenhalt für den Projekterfolg sind.
Wir sind stolz auf das Ergebnis – und würden bei zukünftigen Projekten definitiv wieder auf eine ähnliche Arbeitsweise setzen: mit noch mehr Voraussicht, technischer Klarheit und agilem Mindset.

### Verwendung von ChatGPT
ChatGPT wurde in unseren Projekt unterstützend eingesetzt. Es diente dazu, unsere Lösungen gegen die Aufgabenstellung abzugleichen und sicherzustellen, dass alle Anforderungen erfüllt wurden. Vor allem nutzten wir das Tool, um sprachliche Fehler zu vermeiden und eine präziseren, klareren Schreibstil in unserer Dokumentation zu erreichen.

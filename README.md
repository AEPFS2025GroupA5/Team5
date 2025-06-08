# Team5
Im Frühjahrssemester wurden wir beauftragt, ein Anwendungsszenario für ein Hotelreservierungssystem zu entwickeln. Dieses Projekt baut auf der Arbeit des vorangegangenen Semesters auf, in dem wir eine Datenbank für den Kurs "Datenbasierte Unternehmensanwendung" entworfen haben.

Wie in den Projektrichtlinien beschrieben, verwenden wir verschiedene Werkzeuge, um unseren Entwicklungsprozess zu unterstützen:
- Visual Paradigm für das Klassendiagramm
- SQLite für die Datenbank
- Jupyter Notebook für die Dokumentation sowie Ausführung der Codes
- GitHub für die Versions Controlle und Projekt Management

Wir haben versucht, DeepNote zu verwenden, aber um mehr Praxisbezug zu bekommen, haben wir Visual Studio Code verwendet. Codes auszuführen, zu pushen und in unser Repository zu ziehen.

### Projekt Management
#### Vorgehensweise
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

Die Aufgaben wurden entsprechend dieser Aufteilung im Team verteilt.

Für die Organisation und Kommunikation haben wir hauptsächlich unseren WhatsApp-Gruppenchat genutzt. Darüber haben wir besprochen, bis wann welche Teile fertiggestellt werden sollen, und regelmässig Herausforderungen und offene Fragen diskutiert. Zusätzlich haben wir uns in regelmässigen online oder vor Ort ausgetauscht.

Im Verlauf des Projekts haben wir ausserdem entdeckt, dass GitHub ein integriertes Kanban-Board anbietet. Dieses haben wir gegen Ende des Projektabschnitts ergänzend verwendet, um Aufgaben visuell zu organisieren und den Fortschritt besser nachverfolgen zu können.

> Insgesamt haben wir also ein **hybrides** Planungssystem verwendet – bestehend aus WhatsApp-Kommunikation für schnelle Absprachen und GitHub Kanban für strukturierte Aufgabenverteilung.

### Teamübersicht & Aufgabenverteilung
(Documenter - Chirakkal Fenlin)
(Documenter - Seidel Ivan)


Dieng Saliou - *Architekt der Unterkunftsstruktur*
Verantwortliche Klassen (Model, Data Access, Business Logic, UI):
- `Facility`
- `Room`
- `Room Type`
- `Hotel`

Entsprechende Userstories implementiert:
- 1 - 1.4
- 1.5 und 1.6
- 2 und 2.1
- 3 - 3.3
- 9
- 10
- 11.1


Müller Anna - *Architektin des Gasterlebnisses*
Zugeteilte Klassen in Model, Data Access, Business Logic und UI Layer umgesetzt:
- `Booking`
- `Invoice`
- `Guest`
- `Address`

Entsprechende Userstories implementiert:
- 1.4
- 2.2
- 4 - 8

Beide Teammitglieder arbeiteten eng zusammen und führten regelmässige Code-Reviews durch, um eine einheitliche Codebasis und konsistente Logik sicherzustellen.
Zusätzlich wurde die Dokumentation sowohl im Jupyter Notebook als auch in diesem README gepflegt.

## How to use
Hier erklären was der Nutzer tun soll, damit er Zugriff auf das Notebook hat.


### UML
![image](https://github.com/user-attachments/assets/36cdc1f8-5d7e-4562-be27-18b6bcd21edf)

Das UML haben wir mit Visual Paradigm erstellt und das UML bildet die Beziehung zwischen den Klassen Hotel, Booking, Invoice, Room, Guest, Address, Room Type und Facility. Wir sind nach dem gleichen Schema gegangen wie das von der Datenbank

Hier Bild eifügen


### Abschluss
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
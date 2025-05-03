# Team5
During the spring semester, we were assigned to develop an application scenario for a hotel reservation system. This project builds on work from the previous semester, where we designed a database for the course "Datenbasierte Unternehmensanwendung".

As outlined in the project guidelines, we are using several tools to support our development process:
- Visual Paradigm for system modeling
- SQLite for the database
- DeepNote for documentation
- GitHub for version control and project management

In addition, we have been using Visual Studio Code (and Pycharm) to execute, push and pull codes into our repository.

You can access our DeepNote project via the following link: [enter link here].

### methodology/project management
*gotta ask coaches what they mean by that*

### Project members and their roles
documenter - Chirakkal Fenlin
<br>coder - Dieng Saliou
<br>coder - Müller Anna
<br>documenter - Seidel Ivan

#### Role description
*only if needed*

## User Stories
### minimal user stories
1. Als Gast möchte ich die verfügbaren Hotels durchsuchen, damit ich dasjenige auswählen kann, welches meinen Wünschen entspricht. Wünsche sind:

      1.1. Ich möchte alle Hotels in einer Stadt durchsuchen, damit ich das Hotel nach meinem bevorzugten Standort (Stadt) auswählen kann.

      1.2. Ich möchte alle Hotels in einer Stadt nach der Anzahl der Sterne (z.B. mindestens 4 Sterne) durchsuchen.

      1.3. Ich möchte alle Hotels in einer Stadt durchsuchen, die Zimmer haben, die meiner Gästezahl entsprechen (nur 1 Zimmer pro Buchung).

      1.4. Ich möchte alle Hotels in einer Stadt durchsuchen, die während meines Aufenthaltes ("von" (check_in_date)und "bis" (check_out_date)) Zimmer zur Verfügung haben, damit ich nur relevante Ergebnisse sehe.

      1.5. Ich möchte Wünsche kombinieren können, z.B. die verfügbaren Zimmer zusammen mit meiner Gästezahl und der mindest Anzahl Sterne.

      1.6. Ich möchte die folgenden Informationen pro Hotel sehen: Name, Adresse, Anzahl der Sterne.
   
2. Als Gast möchte ich Details zu verschiedenen Zimmertypen (Single, Double, Suite usw.), die in einem Hotel verfügbar sind, sehen, einschliesslich der maximalen Anzahl von Gästen für dieses Zimmer, Beschreibung, Preis und Ausstattung, um eine fundierte Entscheidung zu treffen.

      2.1. Ich möchte die folgenden Informationen pro Zimmer sehen: Zimmertyp, max. Anzahl der Gäste, Beschreibung, Ausstattung, Preis pro Nacht und Gesamtpreis.

      2.2. Ich möchte nur die verfügbaren Zimmer sehen, sofern ich meinen Aufenthalt (von – bis) spezifiziert habe.

3. Als Admin des Buchungssystems möchte ich die Möglichkeit haben, Hotelinformationen zu pflegen, um aktuelle Informationen im System zu haben.

      3.1. Ich möchte neue Hotels zum System hinzufügen

      3.2. Ich möchte Hotels aus dem System entfernen

      3.3. Ich möchte die Informationen bestimmter Hotels aktualisieren, z. B. den Namen, die Sterne usw.

4. Als Gast möchte ich ein Zimmer in einem bestimmten Hotel buchen, um meinen Urlaub zu planen.

5. Als Gast möchte ich nach meinem Aufenthalt eine Rechnung erhalten, damit ich einen Zahlungsnachweis habe. Hint: Fügt einen Eintrag in der «Invoice» Tabelle hinzu.

6. Als Gast möchte ich meine Buchung stornieren, damit ich nicht belastet werde, wenn ich das Zimmer nicht mehr benötige. Hint: Sorgt für die entsprechende Invoice. 

7. Als Gast möchte ich eine dynamische Preisgestaltung auf der Grundlage der Nachfrage sehen, damit ich ein Zimmer zum besten Preis buchen kann. Hint: Wendet in der Hochsaison höhere und in der Nebensaison niedrigere Tarife an. 

8. Als Admin des Buchungssystems möchte ich alle Buchungen aller Hotels sehen können, um eine Übersicht zu erhalten.

9. Als Admin möchte ich eine Liste der Zimmer mit ihrer Ausstattung sehen, damit ich sie besser bewerben kann.

10. Als Admin möchte ich in der Lage sein, Stammdaten zu verwalten, z.B. Zimmertypen, Einrichtungen, und Preise in Echtzeit zu aktualisieren, damit das Backend-System aktuelle Informationen hat. Hint: Stammdaten sind alle Daten, die nicht von anderen Daten
abhängen.

### User stories with DB schema change
(choose min. 2 User Story on Page 4)

### User stories with data visualization
(choose only one User Story on Page 4)

### optional user stories
*can be removed if wished*

## Documentation
(only document the milestones)

### Class Diagram
[picture of finished Class diagram]

### Reflection



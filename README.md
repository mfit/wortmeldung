wortmeldung
===========

=== Beschreibung ===

Extraktion der Redebeiträge der Abgeordneten und Minister des österreichischen Parlaments.

Die Protokolle der Sitzungen stehen zwar zur Verfügung [1], allerdings nicht in strukturiertem, maschinenlesbarem Format.
Als erster Schritt sollen also aus den Stenographischen Protokollen einzlene Redebeiträge (Wortmeldung plus Meta-Daten wie 
RednerIn, Zeitpunkt, Sitzung) der Abgeordneten extrahiert werden. (Siehe Datenformate/Wortmeldung).

Die daraus entstehendne stukturierten und "gesäuberten" könnten in ihrer Gesamtheit (etwa als XML-Datensatz) oder als API, etwa mit
Suchfunktion öffentlich zur Verfügung gestellt werden.



=== Wozu & Ausblick ===

* Testen von NLP Bibliotheken Pattern [2], Nltk [4] usw.

* Bessere Erschliessung der Redebeiträge der ParlamentarierInnen durch Möglichkeit zur Suche, Keyword Extraction,
 Dokument-Ähnlichkeiten etc. auf Basis einzelner Redebeiträge

* Öffentliche Diskussion durch Verknüpfung mit einer Kommentar-Funktion

Weiters: 

* Offene "Pipeline" , bzw NLP-Plugins zur Textanalyse (Filtersysteme, Suchfunktion, Klassifikation)

* Web-Frontend zur visualisierung der Analysen und evt. Kommentarfunktion

* API nach dem Muster Congress-API von Sunlight Labs [5]


=== Referenzen ===

[1] http://www.parlament.gv.at/PAKT/STPROT/
[2] http://www.clips.ua.ac.be/pages/pattern
[3] http://scrapy.org/
[4] http://www.nltk.org/
[5] http://services.sunlightlabs.com/





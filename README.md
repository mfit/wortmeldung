wortmeldung
===========

### Beschreibung ###

Extraktion der Redebeiträge der Abgeordneten und Minister des österreichischen Parlaments.

Die Protokolle der Sitzungen stehen zwar zur Verfügung [1], allerdings nicht in strukturiertem, maschinenlesbarem Format.
Als erster Schritt sollen also aus den Stenographischen Protokollen einzlene Redebeiträge (Wortmeldung plus Meta-Daten wie 
RednerIn, Zeitpunkt, Sitzung) der Abgeordneten extrahiert werden. (Siehe Datenformate/Wortmeldung).

Die daraus entstehendne stukturierten und "gesäuberten" könnten in ihrer Gesamtheit (etwa als XML-Datensatz) oder als API, etwa mit
Suchfunktion öffentlich zur Verfügung gestellt werden.



### Wozu & Ausblick ###

* Testen von NLP Bibliotheken Pattern [2], Nltk [4] usw.

* Bessere Erschliessung der Redebeiträge der ParlamentarierInnen durch Möglichkeit zur Suche, Keyword Extraction,
 Dokument-Ähnlichkeiten etc. auf Basis einzelner Redebeiträge

* Öffentliche Diskussion durch Verknüpfung mit einer Kommentar-Funktion

Weiters: 

* Offene "Pipeline" , bzw NLP-Plugins zur Textanalyse (Filtersysteme, Suchfunktion, Klassifikation)

* Web-Frontend zur visualisierung der Analysen und evt. Kommentarfunktion

* API nach dem Muster Congress-API von Sunlight Labs [5]


### Datenstruktur ###
* Sitzung : Kürzel der Sitzung zb NRSITZ_00046 (unique)
* Datum	: Datum der Sitzung
* Gesetzgebungsperiode : zb XXIV
* TypeTags : Kürzel für "Ausschuss" - Art, zb NRSITZ, ..

#### Wortmeldung  ####

##### Rohdaten #####
* sitzung : link zur sitzungs-collection oder specherung des kürzels (zb NRSITZ_00046)
* content-raw : gesamter inhalt des "WordSection" - DIVs
* order : 	reihenfolge der wortmeldungen (position des wordsection-divs 0..n)

##### Cleaned #####
* paragraphs: P-Tags der relevaten Klassen (html)
* paragraphs-cleaned : paragraphen, tag-stripped
* paragraphs-processed : paragraphen, tag-stripped & "metadaten" entfernt (anrede/person, zwischenrufe - zwischenrufe ersetzt durch platzhalter ? )

##### Processed #####
* speaker		
* party
* speaker-title
* type 	: a,b,m für Abgeordneter, Präsident/Wortführer, Minister/Regierungsmitglied
* timestamp  : minute/sekunde bzw volle timestamp  (beginnzeit)
* links		: vorhandene links 
* reaktionen 	: zwischenrufe 
* timestamps  :

Evt. RDF Vokabular verwenden , zB an Schema.org [6] orientieren . 

### Referenzen ###

[1] http://www.parlament.gv.at/PAKT/STPROT/
[2] http://www.clips.ua.ac.be/pages/pattern
[3] http://scrapy.org/
[4] http://www.nltk.org/
[5] http://services.sunlightlabs.com/
[6] http://schema.org/docs/full.html





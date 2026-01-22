## Eigen playbook-experiment (webserver)

## Beschrijving
Dit experiment installeert Apache2 op de webserver(s), zet een custom webpagina (`index.html`)
en (optioneel) configureert Apache om op een andere poort te luisteren.

## Doel
- Ansible via SSH kan communiceren met een webserver
- Software-installatie (Apache2) geautomatiseerd kan worden
- Configuratiebestanden automatisch aangepast kunnen worden
- Variabelen (zoals poortnummer) flexibel kunnen worden meegegeven
- Een custom webpagina automatisch uitgerold kan worden
# Eigen pipeline-experiment

## Beschrijving
Dit experiment bouwt voort op de Jenkins CI/CD lab. In dit project wordt een eenvoudige Flask webapplicatie automatisch gebouwd, getest en (optioneel) gedeployed met behulp van een Jenkins Pipeline (Jenkinsfile).

De pipeline gebruikt Docker om de applicatie te containeriseren en voert een automatische HTTP-test uit om te controleren of de applicatie correct draait voordat deze wordt gedeployed.

## Doel van het experiment
Het doel van dit experiment is om:
- te begrijpen hoe een Jenkinsfile wordt gebruikt voor Pipeline as Code 
- het **CI/CD-proces** (Build → Test → Deploy) te automatiseren  
- te laten zien hoe Jenkins automatisch kan stoppen bij fouten met behulp van een quality gate
- ervaring op te doen met Docker binnen een Jenkins pipeline  

# Analys

#### Funktionallitet
Programmet i sig fungerar stort sett felfritt. De funktionaliteter som jag har laggt till fungerar.
För tillfället finns det inga kända buggar.

När värderna för ett objekt visas upp valde jag att använda mig utav QLineEdits. Detta då det ger 
ett lätt och snyggt sätt att visa värderna samtidigt som det ger ett sätt att ändra dessa värden på. 
Det blir även ett mer användarvänligt och lättläsligt GUI där det inte blir licka tjockt med olika ställen 
där användern måste hitta i.

Alla värden är inte acceptabla som värden hos fordonen. t.ex. att man har ett negativt pris eller en 
årsmodell över 2015. Därför har jag lagt till att om man försöker skapa ett objekt eller ändra ett objekt 
med felaktiga värden så skapas helt enkelt ett litet fönster där de värden som är acceptabla skrivs upp. 
Det är här jag har laggt till mina test funktioner. De kallas på när användaren vill lägga till ett
fordon eller ändra ett fordons värden. Funktionerna kollar då om värderna som är inmatade är acceptabla
eller inte. Är de acceptabla returneras True och det användaren vill göra funkar. Om värderna är oacceptabla 
returneras False och fönstret öppnas

I sökmetoden används linjär sökning. Detta görs för att listan kan både vara sorterad eller osorterad.
Då användaren själv väljer när en sortering ska ske gick det lättast att implementera en linjär sökning.
Nackdelarna med linjär sökning är att det inte är en effektiv sökmetod om man arbetar med längre listor.
Detta blir dock inte ett jättestort problem i detta program då programmet inte arbetar med så stora listor 
då användaren själv måste lägga till varenda objekt i listan manuellt. 

En förbätringsmöjlighet är att man skulle kunna lägga till en binär sökning som enbart söker om listan 
är sorterad. Då får den linjära sökningen ske om listan är osorterad.

För att spara undan listan så krävs det att man trycker på spara knappen. Jag har gjort en manuell knapp 
istället för att det ska ske automatiskt eftersom användaren ska kunna spara när denne vill.
Anledningen till att jag inte har en automatisk sparfunktion är för att om användaren råkar göra ett misstag
och ändrar ett värde hos ett fordon som denne inte vill ändra så ska inte denna ändring sparas undan. 
Det finns alltid en risk för att användaren råkar stänga ned programmet utan att ha sparat men jag anser
att det är bättre att ge användern den friheten att kunna spara undan de ändringar som denne är nöjd med.

Jag har haft lite problem med knapparna där en knapp vill komma åt ett värde som inte finns. 
T.ex. att man trycker på knappen som tar bort fordon utan att faktiskt ha valt ett fordon. 
Detta problem har jag löst genom att låsa vissa knappar som inte ska användas innan andra 
saker har gjorts först. T.ex så är knappen för att välja fordon låst om listan av fordon är 
tom fram tills att användaren använder lägger till ett fordon. 


#### Extra tillägg
Jag valde att som extra funktionallitet att lägga till en sorteringsmetod. Först får användaren
välja vad denne vill sortera efter, om det är skapare, modell, pris eller årsmodell. Sen körs
en simpel bubbelsortering där listan sorteras efter det valda variablet i bokstavsording.

Anledningen till att jag använde mig utav bubbelsortering är för att det är relativt lite kod och 
det är relativt lätt att implementera. Nackdelar som att bubbelsortering tar lång tid motarbetas av det 
faktum att listan som programmet använder inte kommer vara särskillt lång. Anledningen till detta är att 
användaren själv måste lägga till varenda enskilt objekt i listan. 


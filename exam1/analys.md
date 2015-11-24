# Analys

#### Funktionallitet
Programmet i sig fungerar stort sett felfritt. De funktionaliteter som jag har laggt till fungerar.
För tillfället finns det inga kända buggar.

När värderna för ett objekt visas upp valde jag att använda mig utav QLineEdits. Detta då det ger 
ett lätt och snyggt sätt att visa värderna men samtidigt kunna ändra dessa värden. Det blir även
ett mer användarvänligt GUI där det inte blir licka tjockt med olika ställen där användern måste hitta.

Alla värden är inte acceptabla som värden hos fordonen t.ex. att man har ett negativt pris eller en 
årsmodell över 2015. Därför har jag lagt till att om man försöker skapa ett objekt eller ändra ett objekt 
med felaktiga värden så skapas helt enkelt ett litet fönster där de värden som är acceptabla skrivs upp.  

I sökmetoden används linjär sökning. Detta görs för att listan kan både vara sorterad eller osorterad.
Då användaren själv väljer när en sortering ska ske gick det lättast att implementera en linjär sökning.
Nackdelarna med linjär sökning är att det inte är en effektiv sökmetod om man arbetar med längre listor.
Detta blir dock inte ett jättestort problem i detta program då programmet inte arbetar med så stora listor 
då användaren själv måste lägga till varenda objekt i listan manuellt. 

En förbätringsmöjlighet är att man skulle kunna lägga till en binär sökning som enbart söker om listan 
är sorterad. Då får den linjära sökningen ske om listan är osorterad.

#### Extra tillägg
Jag valde att som extra funktionallitet att lägga till en sorteringsmetod. Först får användaren
välja vad denne vill sortera efter, om det är skapare, modell, pris eller årsmodell. Sen körs
en simpel bubbelsortering där listan sorteras efter det valda variablet i bokstavsording.

Anledningen till att jag använde mig utav bubbelsortering är för att det är relativt lite kod och 
det är relativt lätt att implementera. Nackdelar som att bubbelsortering tar lång tid motarbetas av det 
faktum att listan som programmet använder inte kommer vara särskillt lång. Anledningen till detta är att 
användaren själv måste lägga till varenda enskilt objekt i listan. 


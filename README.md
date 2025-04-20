# Vocea României - AutoVoter
Mic program în Python care automatizează votul pentru un concurent ales pe https://voteazavocea.protv.ro/, validându-l cu adrese temporare de mail.
## Requirements
```
pip install selenium
pip install beautifulsoup4
pip install tempmail-python
```
## Common errors
- Asigură-te că descarci o versiune de Chrome Driver compatibilă cu versiunea de Chrome instalată.
Chrome îşi mai face auto update, există mai multe moduri de a opri update-urile. Una (destul de primitivă) pe care am folosit-o este de a redenumi fişierele .exe responsabile de update-uri din folderul ``C:\Program Files (x86)\Google``

## Eficienţă
În formatul actual, votul durează aprox. 15 secunde, dar duratele de sleep pot fi ajustate.
## DISCLAIMER
Nu îmi asum responsabilitatea pentru scopurile în care este utilizat programul. Este făcut în scop pur educaţional şi demonstrativ, realist vorbind aduce un număr neglijabil de voturi, având în vedere timpul necesar fiecărei iteraţii şi numărul mare de voturi reale din partea audienţei.
-> Testat în decembrie 2024

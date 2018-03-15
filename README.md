# deep_bortox

## Risorse necessarie
### auditok
con auditok si spezzetta un file audio in tanti file audio (tramite un comando da prompt)
https://github.com/amsehili/auditok/blob/master/README.md

### speech recognition
con speech recognitiion dato un file audio ottieni il testo corrispondente usando vari speech recognition systems, quello offline non è molto accurato, meglio google (ci vorrebbe l'api key ma si può fare anche senza)
https://github.com/Uberi/speech_recognition/

## cosa si fa
quindi mettendo insieme i due hai per ogni parola/frase la traccia audio e viceversa, così si può trasformare un testo arbitrario in audio cercando tra le tracce che hai secondo le parole corrispondenti

Con auditok si invoca da riga di comando: auditok -i <inputFilePath> -o {N}<outputFile>


